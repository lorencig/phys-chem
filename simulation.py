import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from utils import get_download_link, create_3d_surface, langmuir_isotherm

def app():
    st.title("Advanced Adsorption Simulation")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Model Selection")
        model_type = st.selectbox("Choose Adsorption Model", ["Langmuir", "Freundlich", "BET", "Temkin"])
        if model_type == "Langmuir":
            st.latex(r"\theta = \frac{K_a \cdot p}{1 + K_a \cdot p}")
            st.markdown("**Langmuir Model:** Assumes monolayer adsorption on a homogeneous surface.")
        elif model_type == "Freundlich":
            st.latex(r"q = K_d \cdot C^{1/n}")
            st.markdown("**Freundlich Model:** Empirical model for heterogeneous surfaces.")
        elif model_type == "BET":
            st.latex(r"\frac{P}{V(P_0 - P)} = \frac{1}{V_m \cdot C} + \frac{C - 1}{V_m \cdot C} \cdot \frac{P}{P_0}")
            st.markdown("**BET Model:** Typically used for multilayer adsorption on porous materials.")
        elif model_type == "Temkin":
            st.latex(r"q_e = \frac{RT}{b_T} \ln(K_T \cdot C_e)")
            st.markdown("**Temkin Model:** Accounts for adsorbate-adsorbent interactions and assumes a linear decrease in adsorption heat.")
    
    with col2:
        st.subheader("System Properties")
        adsorbent = st.selectbox("Select Adsorbent Material", ["Activated Carbon", "Zeolite", "Silica Gel", "Custom"])
        predefined_materials = {
            "Activated Carbon": {"surface_area": 1000, "pore_volume": 0.5},
            "Zeolite": {"surface_area": 750, "pore_volume": 0.3},
            "Silica Gel": {"surface_area": 500, "pore_volume": 0.4}
        }
        if adsorbent == "Custom":
            custom_surface_area = st.number_input("Surface Area (m²/g)", 0.0, 5000.0, 1000.0, help="Enter custom surface area.")
            custom_pore_volume = st.number_input("Pore Volume (cm³/g)", 0.0, 2.0, 0.5, help="Enter custom pore volume.")
            material_props = {"Custom": {"surface_area": custom_surface_area, "pore_volume": custom_pore_volume}}
        else:
            material_props = {adsorbent: predefined_materials[adsorbent]}
        st.write(f"Surface Area: {material_props[adsorbent]['surface_area']} m²/g")
        st.write(f"Pore Volume: {material_props[adsorbent]['pore_volume']} cm³/g")
    
    st.sidebar.header("Simulation Parameters")
    with st.sidebar.expander("Temperature Effects"):
        T_range = st.slider("Temperature Range (K)", 0, 1000, (298, 323))
        T_fixed = np.mean(T_range)
        deltaH = st.number_input("ΔH (kJ/mol)", value=-20.0, help="Enter ΔH (negative for exothermic).")
        deltaS = st.number_input("ΔS (J/mol·K)", value=-60.0, help="Enter ΔS.")
    with st.sidebar.expander("Pressure Settings"):
        P_max = st.slider("Maximum Pressure (bar)", 1, 200, 100)
        P_points = st.slider("Number of Points", 10, 300, 100)
    
    pressures = np.linspace(0, P_max, P_points)
    st.subheader("Adsorption Isotherm")
    fig_iso = go.Figure()
    K_fixed = np.exp((-deltaH * 1000)/(8.314 * T_fixed) + deltaS/8.314)
    
    # Calculate Q based on the selected model
    if model_type == "Langmuir":
        Q = langmuir_isotherm(pressures, K_fixed)
    elif model_type == "Freundlich":
        n = 2  # Example value for Freundlich exponent
        Q = K_fixed * pressures**(1/n)
    elif model_type == "BET":
        P0 = 1000  # Saturation pressure
        Q = (K_fixed * pressures) / (1 - pressures/P0) * (1 / (1 + (K_fixed - 1) * pressures/P0))
    elif model_type == "Temkin":
        b_T = 100  # Heat of adsorption parameter
        K_T = 1.0  # Equilibrium binding constant
        C_e = pressures  # Assuming equilibrium concentration is proportional to pressure
        Q = (8.314 * T_fixed / b_T) * np.log(K_T * C_e)
    
    fig_iso.add_trace(go.Scatter(x=pressures, y=Q, mode='lines', name=f"T = {T_fixed:.1f} K"))
    fig_iso.update_layout(title="Adsorption Isotherm", xaxis_title="Pressure (bar)", yaxis_title="Amount Adsorbed (mol/kg)")
    st.plotly_chart(fig_iso, use_container_width=True)
    
    st.subheader("Material Comparison")
    st.markdown("Comparing isotherms for different materials (scaled by surface area).")
    all_materials = predefined_materials.copy()
    if adsorbent == "Custom":
        all_materials["Custom"] = material_props["Custom"]
    fig_material = go.Figure()
    
    # Use the same model for material comparison
    for mat, props in all_materials.items():
        scale = props["surface_area"] / 1000.0
        if model_type == "Langmuir":
            Q_mat = langmuir_isotherm(pressures, K_fixed) * scale
        elif model_type == "Freundlich":
            Q_mat = K_fixed * pressures**(1/n) * scale
        elif model_type == "BET":
            Q_mat = (K_fixed * pressures) / (1 - pressures/P0) * (1 / (1 + (K_fixed - 1) * pressures/P0)) * scale
        elif model_type == "Temkin":
            Q_mat = (8.314 * T_fixed / b_T) * np.log(K_T * C_e) * scale
        fig_material.add_trace(go.Scatter(x=pressures, y=Q_mat, mode='lines', name=f"{mat} (scale: {scale:.2f})"))
    
    fig_material.update_layout(title="Material Specific Adsorption Isotherms", xaxis_title="Pressure (bar)", yaxis_title="Scaled Adsorption (mol/kg)")
    st.plotly_chart(fig_material, use_container_width=True)
    
    st.subheader("Parameter Sensitivity Analysis")
    psa_active = st.checkbox("Activate Parameter Sensitivity Analysis")
    if psa_active:
        st.info("PSA examines how changes in parameters affect adsorption behavior.")
        sensitivity_param = st.selectbox("Select Parameter", ["ΔH", "ΔS", "K"])
        fig_sens = go.Figure()
        if sensitivity_param == "ΔH":
            deltaH_range = st.slider("ΔH Range (kJ/mol)", -100, 0, (-50, -10))
            for dH in np.linspace(deltaH_range[0], deltaH_range[1], 5):
                K_val = np.exp((-dH * 1000)/(8.314 * T_fixed) + deltaS/8.314)
                Q_sens = langmuir_isotherm(pressures, K_val)
                fig_sens.add_trace(go.Scatter(x=pressures, y=Q_sens, mode='lines', name=f"ΔH = {dH:.1f}"))
        elif sensitivity_param == "ΔS":
            deltaS_range = st.slider("ΔS Range (J/mol·K)", -200, 0, (-120, -20))
            for dS in np.linspace(deltaS_range[0], deltaS_range[1], 5):
                K_val = np.exp((-deltaH * 1000)/(8.314 * T_fixed) + dS/8.314)
                Q_sens = langmuir_isotherm(pressures, K_val)
                fig_sens.add_trace(go.Scatter(x=pressures, y=Q_sens, mode='lines', name=f"ΔS = {dS:.1f}"))
        else:
            for K_val in np.linspace(0.5*K_fixed, 1.5*K_fixed, 5):
                Q_sens = langmuir_isotherm(pressures, K_val)
                fig_sens.add_trace(go.Scatter(x=pressures, y=Q_sens, mode='lines', name=f"K = {K_val:.2f}"))
        fig_sens.update_layout(title="Sensitivity Analysis", xaxis_title="Pressure (bar)", yaxis_title="Adsorption (mol/kg)")
        st.plotly_chart(fig_sens, use_container_width=True)
    else:
        st.info("PSA is inactive. Activate the checkbox to view sensitivity analysis.")
    
    st.subheader("3D Visualization")
    if st.checkbox("Show 3D Plot"):
        fig_3d = go.Figure(data=[create_3d_surface(np.linspace(0, P_max, 50), np.linspace(T_range[0], T_range[1], 50), deltaH, deltaS)])
        fig_3d.update_layout(scene=dict(xaxis_title="Pressure (bar)", yaxis_title="Temperature (K)", zaxis_title="Adsorption (mol/kg)"), title="3D Adsorption Surface")
        st.plotly_chart(fig_3d, use_container_width=True)
    
    st.subheader("Export Results")
    if st.button("Generate CSV"):
        import pandas as pd
        results_df = pd.DataFrame({'Pressure': pressures, 'Temperature': [T_fixed]*len(pressures), 'Adsorption': Q})
        st.markdown(get_download_link(results_df, 'adsorption_results.csv', 'Download Results CSV'), unsafe_allow_html=True)