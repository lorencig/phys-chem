import streamlit as st
import numpy as np
import plotly.graph_objects as go
from utils import get_download_link, create_3d_surface, langmuir_isotherm

def app():
    st.title("Advanced Adsorption Simulation")
    
    # ============================================================
    # ROW 1: Model Selection and Material Properties
    # ============================================================
    row1_cols = st.columns(2)
    
    with row1_cols[0]:
        st.header("Model Selection")
        model_type = st.selectbox("Choose Adsorption Model", 
                                  ["Langmuir", "Freundlich", "BET", "Temkin"])
        if model_type == "Langmuir":
            st.latex(r"\theta = \frac{K \cdot p}{1 + K \cdot p}")
            st.markdown("**Langmuir Model:** Assumes monolayer adsorption on a homogeneous surface.")
        elif model_type == "Freundlich":
            st.latex(r"q = K \cdot p^{\frac{1}{n}}")
            st.markdown("**Freundlich Model:** Empirical model for heterogeneous surfaces.")
        elif model_type == "BET":
            st.latex(r"\frac{p}{q(p_0 - p)} = \frac{1}{q_{max} \cdot C} + \frac{C - 1}{q_{max} \cdot C} \cdot \frac{p}{p_0}")
            st.markdown("**BET Model:** Typically used for multilayer adsorption on porous materials.")
        elif model_type == "Temkin":
            st.latex(r"q = \frac{RT}{b} \ln(K \cdot p)")
            st.markdown("**Temkin Model:** Accounts for adsorbate–adsorbent interactions with a linear decrease in adsorption heat.")

    with row1_cols[1]:
        st.header("Material Properties")
        adsorbent = st.selectbox("Select Adsorbent Material", 
                                 ["Activated Carbon", "Zeolite", "Silica Gel", "Custom"])
        predefined_materials = {
            "Activated Carbon": {"surface_area": 1000, "pore_volume": 0.5},
            "Zeolite": {"surface_area": 750, "pore_volume": 0.3},
            "Silica Gel": {"surface_area": 500, "pore_volume": 0.4}
        }
        if adsorbent == "Custom":
            surface_area = st.number_input("Surface Area (m²/g)", 0.0, 5000.0, 1000.0, step=50.0)
            pore_volume = st.number_input("Pore Volume (cm³/g)", 0.0, 2.0, 0.5, step=0.1)
        else:
            surface_area = predefined_materials[adsorbent]["surface_area"]
            pore_volume = predefined_materials[adsorbent]["pore_volume"]
        st.write(f"Surface Area: {surface_area} m²/g")
        st.write(f"Pore Volume: {pore_volume} cm³/g")
    
    # ============================================================
    # ROW 2: Default and Advanced Simulation Parameters
    # ============================================================
    row2_cols = st.columns(2)
    
    with row2_cols[0]:
        st.header("Default Parameters")
        T = st.number_input("Temperature (K)", min_value=1, max_value=2000, value=298, step=1)
        P_max = st.number_input("Maximum Pressure (bar)", min_value=1, max_value=500, value=1, step=1)
        qmax = st.number_input("Maximum Adsorption Capacity qₘₐₓ (mol/kg)", min_value=0.1, max_value=100.0, value=10.0, step=0.1)
    
    with row2_cols[1]:
        st.header("Advanced Parameters")
        deltaH = st.number_input("Enthalpy (ΔH, kJ/mol)", min_value=-200.0, max_value=0.0, value=-20.0, step=1.0,
                                 help="Negative for exothermic processes.")
        deltaS = st.number_input("Entropy (ΔS, J/mol·K)", min_value=-300.0, max_value=300.0, value=-60.0, step=1.0)
        R = 8.314  # J/mol·K
        K = np.exp((-deltaH * 1000) / (R * T) + deltaS / R)
        st.write(f"Calculated Equilibrium Constant (K): {K:.3f}")
        if model_type == "Freundlich":
            n = st.number_input("Freundlich Exponent (n)", min_value=0.1, max_value=10.0, value=2.0, step=0.1)
        else:
            n = 2.0
        if model_type == "BET":
            C_BET = st.number_input("BET Constant (C)", min_value=1.0, max_value=100.0, value=10.0, step=0.1)
        else:
            C_BET = 10.0
        if model_type == "Temkin":
            b = st.number_input("Temkin Constant (b)", min_value=0.1, max_value=1000.0, value=100.0, step=1.0)
        else:
            b = 100.0
    
    # ============================================================
    # ADSORPTION ISOTHERM CALCULATION
    # ============================================================
    pressure_points = 100
    pressures = np.linspace(0, P_max, pressure_points)
    
    if model_type == "Langmuir":
        # q = qmax * (K * p) / (1 + K * p)
        Q = qmax * (K * pressures) / (1 + K * pressures)
    elif model_type == "Freundlich":
        # q = qmax * (K * p^(1/n)) / (1 + K * p^(1/n))
        Q = qmax * (K * pressures**(1/n)) / (1 + K * pressures**(1/n))
    elif model_type == "BET":
        # Simplified BET model
        Q = qmax * (C_BET * pressures) / ((1 - pressures / P_max) * (1 + (C_BET - 1) * pressures / P_max))
    elif model_type == "Temkin":
        Q = np.zeros_like(pressures)
        positive = pressures > 0
        Q[positive] = qmax * ((R * T / b) * np.log(K * pressures[positive])) / (1 + (R * T / b) * np.log(K * pressures[positive]))
    else:
        Q = np.zeros_like(pressures)
    
    # Apply material scaling (normalize to 1000 m²/g)
    scale = surface_area / 1000.0
    Q_scaled = Q * scale

    # ============================================================
    # PLOT: ADSORPTION ISOTHERM (SINGLE CURVE)
    # ============================================================
    st.header("Adsorption Isotherm")
    fig_iso = go.Figure()
    fig_iso.add_trace(go.Scatter(x=pressures, y=Q_scaled, mode='lines', name=f"{adsorbent}"))
    fig_iso.update_layout(title="Adsorption Isotherm",
                          xaxis_title="Pressure (bar)",
                          yaxis_title="Adsorption (mol/kg)")
    st.plotly_chart(fig_iso, use_container_width=True)
    
    # ============================================================
    # MATERIAL COMPARISON: OVERLAPPING CURVES FOR DIFFERENT MATERIALS
    # ============================================================
    st.header("Material Comparison")
    all_materials = predefined_materials.copy()
    if adsorbent == "Custom":
        all_materials["Custom"] = {"surface_area": surface_area, "pore_volume": pore_volume}
    fig_material = go.Figure()
    for mat, props in all_materials.items():
        scale_mat = props["surface_area"] / 1000.0
        if model_type == "Langmuir":
            Q_mat = qmax * (K * pressures) / (1 + K * pressures)
        elif model_type == "Freundlich":
            Q_mat = qmax * (K * pressures**(1/n)) / (1 + K * pressures**(1/n))
        elif model_type == "BET":
            Q_mat = qmax * (C_BET * pressures) / ((1 - pressures / P_max) * (1 + (C_BET - 1) * pressures / P_max))
        elif model_type == "Temkin":
            Q_mat = np.zeros_like(pressures)
            positive = pressures > 0
            Q_mat[positive] = qmax * ((R * T / b) * np.log(K * pressures[positive])) / (1 + (R * T / b) * np.log(K * pressures[positive]))
        else:
            Q_mat = np.zeros_like(pressures)
        fig_material.add_trace(go.Scatter(x=pressures, y=Q_mat * scale_mat,
                                          mode='lines', name=f"{mat} (scale: {scale_mat:.2f})"))
    fig_material.update_layout(title="Material-Specific Adsorption Isotherms",
                               xaxis_title="Pressure (bar)",
                               yaxis_title="Adsorption (mol/kg)")
    st.plotly_chart(fig_material, use_container_width=True)
    
    # ============================================================
    # 3D VISUALIZATION WITH TIME RANGE SELECTION
    # ============================================================
    st.header("3D Visualization")
    if st.checkbox("Show 3D Plot"):
        # Ask for the temperature range only when the 3D plot is activated.
        temp_range_3d = st.slider("Select Temperature Range for 3D Plot (K)", 0, 1000, (273, 298))
        
        # Define ranges for pressure and temperature based on the selected temperature range.
        P_range = np.linspace(0, P_max, 50)
        T_range = np.linspace(temp_range_3d[0], temp_range_3d[1], 50)
        
        # Create the base surface using your provided function.
        # Expected: create_3d_surface returns a NumPy array of adsorption values with shape (len(T_range), len(P_range))
        surface = create_3d_surface(P_range, T_range, deltaH, deltaS)
        
        # Ensure that we have numeric data in a NumPy array for further arithmetic.
        if isinstance(surface, go.Surface):
            try:
                z_data = np.array(surface.z)
            except Exception as e:
                st.error("Error extracting z data from surface: " + str(e))
                z_data = np.zeros((len(T_range), len(P_range)))
        elif not isinstance(surface, np.ndarray):
            try:
                z_data = np.array(surface)
            except Exception as e:
                st.error("Error converting surface to numpy array: " + str(e))
                z_data = np.zeros((len(T_range), len(P_range)))
        else:
            z_data = surface

        # (Optional) Apply any additional modifications to z_data here.
        # In this example, we simply use z_data as the 3D surface.
        
        # Create and display the 3D surface plot.
        fig_3d = go.Figure(data=[go.Surface(z=z_data, x=P_range, y=T_range)])
        fig_3d.update_layout(
            scene=dict(xaxis_title="Pressure (bar)",
                    yaxis_title="Temperature (K)",
                    zaxis_title="Adsorption (mol/kg)"),
            title="3D Adsorption Surface"
        )
        st.plotly_chart(fig_3d, use_container_width=True)

    
    # ============================================================
    # EXPORT RESULTS
    # ============================================================
    st.header("Export Results")
    if st.button("Generate CSV"):
        import pandas as pd
        results_df = pd.DataFrame({
            'Pressure (bar)': pressures,
            'Temperature (K)': [T] * len(pressures),
            'Adsorption (mol/kg)': Q_scaled
        })
        st.markdown(get_download_link(results_df, 'adsorption_results.csv', 'Download Results CSV'),
                    unsafe_allow_html=True)

if __name__ == '__main__':
    app()
