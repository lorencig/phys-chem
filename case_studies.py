import streamlit as st

def app():
    st.title("Industrial Case Studies: Problem & Solution Exercises")
    
    case_study = st.selectbox("Select Case Study", 
                            ["Gas Storage"])
                            #["Gas Storage", "Water Treatment", "Air Purification", "Carbon Capture"])

    # -------------------------------------------------------------------------
    # CASE STUDY: Hydrogen Storage in Metal-Organic Frameworks (MOFs)
    if case_study == "Gas Storage":
        
        # Title and Introduction
        st.markdown("## Hydrogen Storage in Metal-Organic Frameworks (MOFs)")
        st.write("""
        In this case study, we aim to design a hydrogen (H₂) storage system using MOFs.
        The problem is divided into three main objectives:
        
        1. **Determine the H₂ Storage Capacity:**  
        Calculate the maximum amount of H₂ (by weight percentage) that the chosen MOF can store at a given temperature and pressure.
        
        2. **Compute the Required MOF Amount:**  
        Figure out how many kilograms of the MOF material are needed to store a specified mass of H₂.
        
        3. **Estimate the Material Cost:**  
        Determine the total cost of the MOF material required for the storage system.
        
        We will adjust a base capacity using a formula that accounts for deviations in pressure and temperature from the reference conditions.
        """)
        
        # Problem Statement Section with Clear Objectives
        st.markdown("### 🎯 Problem Statement")
        st.markdown("""
        **Objective:**  
        Design a hydrogen storage system using MOFs and compute:
        
        - The maximum H₂ storage capacity at given operating conditions.
        - The required amount of MOF to store a predetermined amount of H₂.
        - The total material cost of the system.
        
        **Key Questions:**
        1. *Storage Capacity:* What is the maximum H₂ storage capacity (wt\\%) of the selected MOF at the given temperature and pressure?
        2. *MOF Requirement:* How many kilograms of the MOF are required to store a specified amount of H₂?
        3. *Cost Analysis:* What is the total material cost for the system?
        """)
        
        # Explanation of the Formula
        st.markdown("### 📝 Formula Explanation")
        st.markdown(r"""
        We use the following formula to adjust the base H₂ storage capacity of a MOF:
        
        $$
        \text{Capacity (wt\%)} = \text{Reference Capacity} \times \frac{\text{Pressure}}{50} \times \frac{77}{\text{Temperature}}
        $$
        
        **Where:**
        - **Reference Capacity:** The base H₂ storage capacity of the MOF at the standard conditions (77 K and 50 bar).
        - **Pressure Adjustment ($\frac{\text{Pressure}}{50}$)**: Scales the capacity based on the actual operating pressure relative to the reference pressure.
        - **Temperature Adjustment ($\frac{77}{\text{Temperature}}$)**: Scales the capacity based on the actual operating temperature relative to the reference temperature (77 K).
        
        This formula assumes that the storage capacity increases linearly with pressure and decreases with increasing temperature.
        """)
        
        # Input Parameters for the Students to Work With
        st.markdown("### 📝 Input Parameters")
        
        # MOF Selection and Their Properties
        mof_type = st.selectbox("Select MOF Type", ["HKUST-1", "MOF-5", "UiO-66"])
        mof_properties = {
            "HKUST-1": {"surface_area": 1800, "pore_volume": 0.86, "h2_capacity": 2.3},
            "MOF-5":   {"surface_area": 3800, "pore_volume": 1.55, "h2_capacity": 4.5},
            "UiO-66":  {"surface_area": 1200, "pore_volume": 0.5,  "h2_capacity": 1.8}
        }
        props = mof_properties[mof_type]
        
        # Sliders for Operating Conditions and System Scale
        col1, col2, col3 = st.columns(3)
        with col1:
            temperature = st.slider("Temperature (K)", 77, 298, 77,
                                    help="Operating temperature of the storage system. Lower temperatures favor higher storage capacities.")
        with col2:
            pressure = st.slider("Pressure (bar)", 1, 100, 50,
                                help="Operating pressure of the storage system. Higher pressures generally increase storage capacity.")
        with col3:
            system_scale = st.number_input("System Scale (kg H₂)", 1, 1000, 100,
                                        help="Total mass of H₂ (in kg) that the system should store.")
        
        # Additional Theoretical Background for Context
        with st.expander("📚 Theoretical Background"):
            st.markdown(r"""
            **Fundamentals of H₂ Storage in MOFs:**
            
            - **Modified Langmuir Behavior:**  
            H₂ storage in MOFs can often be approximated by a model that adapts Langmuir adsorption, where capacity increases with pressure up to a saturation point.
            
            - **Temperature Influence:**  
            Lower temperatures enhance the adsorption capacity because the kinetic energy of H₂ molecules is reduced, leading to more effective adsorption.
            
            - **Reference Conditions:**  
            The reference capacity is measured at 77 K and 50 bar, making these conditions the baseline for our calculations.
            
            - **Volumetric Conversion:**  
            A conversion factor of 0.08988 kg/m³ is used to convert weight percentage (wt\\%) to a volumetric capacity.
            """)
        
        # Economic Considerations for the MOF Materials
        with st.expander("💰 Economic Considerations"):
            st.markdown(r"""
            **Material Costs (\$/kg):**
            
            - **HKUST-1:** \$200 per kg (copper-based, moderate cost)
            - **MOF-5:**   \$300 per kg (zinc-based, high purity)
            - **UiO-66:**  \$150 per kg (zirconium-based, economical)
            """)
        
       # Detailed Step-by-Step Solution with Expanded Explanations
    if st.checkbox("Show Detailed Solution"):
        st.markdown("### 🔍 Detailed Step-by-Step Solution")
        
        # Step 1: Calculate the Adjusted H₂ Storage Capacity
        st.markdown("#### Step 1: Calculate H₂ Storage Capacity")
        capacity = props["h2_capacity"] * (pressure / 50) * (77 / temperature)
        volumetric_capacity = capacity * 0.08988  # Conversion from wt% to kg/m³
        
        st.write("We start with the reference capacity of the selected MOF and adjust it based on the actual operating conditions.")
        st.write(f"- **Reference Capacity:** {props['h2_capacity']} wt% (for {mof_type} at 77K and 50 bar)")
        st.write(f"- **Pressure Adjustment:** Current pressure is {pressure} bar, so the factor is $\\frac{{{pressure}}}{{50}}$.")
        st.write(f"- **Temperature Adjustment:** Current temperature is {temperature} K, so the factor is $\\frac{{77}}{{{temperature}}}$.")
        
        st.latex(r"\text{Capacity} = " + f"{props['h2_capacity']} \\times \\frac{{{pressure}}}{{50}} \\times \\frac{{77}}{{{temperature}}} = {capacity:.2f}\\,wt\%")
        st.write(f"This result means that under the given conditions, the MOF can store **{capacity:.2f} wt%** of its weight as H₂.")
        
        st.write("Additionally, multiplying by the conversion factor (0.08988) gives the volumetric capacity:")
        st.latex(r"\text{Volumetric Capacity} = " + f"{capacity:.2f} \\times 0.08988 = {volumetric_capacity:.2f}\\,kg/m^3")
        st.write("This value indicates the mass of H₂ that can be stored per cubic meter of MOF material.")
        
        # Step 2: Determine the Amount of MOF Required and Its Cost
        st.markdown("#### Step 2: Calculate Required MOF Material and Material Cost")
        # Calculate the MOF required by dividing the desired mass of H₂ by the fraction (capacity/100)
        mof_required = system_scale / (capacity / 100)
        mof_costs = {"HKUST-1": 200, "MOF-5": 300, "UiO-66": 150}
        material_cost = mof_required * mof_costs[mof_type]
        
        st.write(f"To store **{system_scale} kg** of H₂, the amount of MOF required is computed as:")
        st.latex(r"\text{MOF Required (kg)} = \frac{\text{System Scale (kg H₂)}}{\text{Capacity (wt\%)} / 100}")
        st.latex(r"\text{MOF Required} = \frac{" + f"{system_scale}" + r"}{" + f"{capacity/100:.2f}" + r"} = " + f"{mof_required:.1f}\\,kg")
        st.write(f"This means you need **{mof_required:.1f} kg** of {mof_type}.")
        
        st.write("Next, we calculate the material cost using the cost per kilogram for the selected MOF:")
        st.latex(r"\text{Material Cost} = \text{MOF Required} \times \text{Cost per kg}")
        st.latex(r"\text{Material Cost} = " + f"{mof_required:.1f} \\times {mof_costs[mof_type]} = \\${material_cost:,.2f}")
        st.write(f"The total material cost for {mof_type} is **${material_cost:,.2f}**.")
        
        # Step 3: Summarize the Results
        st.markdown("#### Step 3: Summary of Results")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Gravimetric Capacity", f"{capacity:.2f} wt%")
            st.metric("Volumetric Capacity", f"{volumetric_capacity:.2f} kg/m³")
        with col2:
            st.metric("Required MOF", f"{mof_required:.1f} kg")
            st.metric("Material Cost", f"${material_cost:,.2f}")
        
        st.markdown("**Conclusion:**")
        st.write(f"""
        - **Storage Capacity:**  
        The selected MOF (**{mof_type}**) has an adjusted hydrogen storage capacity of **{capacity:.2f} wt%** at {temperature} K and {pressure} bar.
        
        - **MOF Material Requirement:**  
        To store **{system_scale} kg** of H₂, you need **{mof_required:.1f} kg** of the MOF.
        
        - **Cost Analysis:**  
        The material cost for the required amount of {mof_type} is **${material_cost:,.2f}**.
        
        - **Volumetric Efficiency:**  
        The volumetric capacity is **{volumetric_capacity:.2f} kg/m³**, which helps evaluate the space utilization of the storage system.
        """)

    # -------------------------------------------------------------------------
    # WATER TREATMENT
    elif case_study == "Water Treatment":
        st.markdown("## Advanced Water Treatment System")

        st.markdown("🎯 Problem Definition & Formulas")
        st.write("""
        Calculate contaminant removal efficiency and system economics for a water treatment process.
        """)
        st.latex(r"Removal\ (\%) = \left(1 - \frac{C}{C_0}\right) \times 100")
        st.latex(r"C = \frac{C_0}{1 + K_F \times D^{1/n}}")
        st.markdown("""
        **Formula Components:**
        1. **C₀:** Initial concentration.
        2. **C:** Final concentration.
        3. **KF:** Freundlich constant.
        4. **D:** Adsorbent dosage.
        5. **n:** Intensity parameter.
        """)

        st.markdown("### 📝 Input Parameters")
        col1, col2, col3 = st.columns(3)
        with col1:
            initial_conc = st.number_input("Initial Concentration (mg/L)", 1, 1000, 100)
        with col2:
            adsorbent_dose = st.number_input("Adsorbent Dose (g/L)", 0.1, 10.0, 2.0)
        with col3:
            treatment_volume = st.number_input("Treatment Volume (m³/day)", 10, 10000, 1000)

        with st.expander("📚 Theoretical Background"):
            st.markdown("""
            **Process Fundamentals:**
            - Follows Freundlich isotherm in dilute solutions.
            - Mass transfer limited by diffusion.
            - Surface adsorption mechanism.
            
            **Key Parameters:**
            - Contact time: 15-30 minutes.
            - Typical dosage: 0.5-5 g/L.
            - pH range: 4-8.
            """)

        with st.expander("💰 Economic Considerations"):
            st.markdown("""
            **Material Costs ($/kg):**
            - Activated Carbon: 2-5.
            - Ion Exchange Resin: 8-15.
            - Zeolites: 5-10.
            
            **Operating Costs:**
            - Energy: 0.1-0.3 kWh/m³.
            - Chemical regeneration: $0.5-1.5/m³.
            - Disposal: $50-100/ton.
            """)

        if st.checkbox("Show Detailed Solution"):
            # Calculate results using Freundlich model
            kf = 20  # Example Freundlich constant
            n = 2.5  # Example intensity parameter
            final_conc = initial_conc / (1 + kf * (adsorbent_dose**(1/n)))
            removal = (1 - final_conc/initial_conc) * 100
            
            adsorbent_cost = adsorbent_dose * treatment_volume * 3  # Assuming $3/kg
            operating_cost = treatment_volume * 0.2  # $0.2/m³ operating cost
            
            st.markdown("### 🔍 Solution Analysis")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Removal Efficiency", f"{removal:.1f}%")
                st.metric("Final Concentration", f"{final_conc:.2f} mg/L")
            with col2:
                st.metric("Daily Adsorbent Cost", f"${adsorbent_cost:.2f}")
                st.metric("Daily Operating Cost", f"${operating_cost:.2f}")

    # -------------------------------------------------------------------------
    # AIR PURIFICATION
    elif case_study == "Air Purification":
        st.markdown("## VOC Removal System")
        

        st.markdown("🎯 Problem Definition & Formulas")
        st.write("""
        Design an air purification system for VOC removal and calculate performance metrics.
        """)
        st.latex(r"Removal\ (\%) = 100 \times \left(1 - e^{-k \tau}\right)")
        st.markdown("""
        **Formula Components:**
        1. **k:** Rate constant.
        2. **τ:** Contact time.
        3. **Flow rate impact on removal.**
        """)

        st.markdown("### 📝 Input Parameters")
        col1, col2, col3 = st.columns(3)
        with col1:
            flow_rate = st.number_input("Air Flow Rate (m³/h)", 100, 10000, 1000)
        with col2:
            voc_conc = st.number_input("VOC Concentration (ppm)", 1, 1000, 100)
        with col3:
            contact_time = st.slider("Contact Time (s)", 1, 10, 3)
        
        with st.expander("📚 Theoretical Background"):
            st.markdown("""
            **Process Fundamentals:**
            - VOC adsorption follows Tóth isotherm.
            - Mass transfer zone concept applies.
            - Dynamic breakthrough behavior.
            
            **Key Parameters:**
            - Contact time: 1-5 seconds.
            - Operating temperature: 20-40°C.
            - Relative humidity: 30-70%.
            """)

        with st.expander("💰 Economic Considerations"):
            st.markdown("""
            **Material Costs ($/kg):**
            - Activated Carbon: 3-8.
            - Molecular Sieves: 10-20.
            - Polymeric Adsorbents: 15-25.
            
            **Operating Costs:**
            - Fan power: 0.2-0.5 kWh/1000m³.
            - Replacement: Every 6-12 months.
            - Maintenance: 5% of capital/year.
            """)
        if st.checkbox("Show Detailed Solution"):
            import math
            k = 0.5  # Example rate constant
            removal = 100 * (1 - math.exp(-k * contact_time))
            pressure_drop = contact_time * 0.1  # Example pressure drop calculation
            power_consumption = flow_rate * pressure_drop * 0.000278  # kWh
            
            operating_cost = power_consumption * 0.1  # Assuming $0.1/kWh
            
            st.markdown("### 🔍 Solution Analysis")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("VOC Removal", f"{removal:.1f}%")
                st.metric("Pressure Drop", f"{pressure_drop:.2f} kPa")
            with col2:
                st.metric("Power Consumption", f"{power_consumption:.2f} kWh")
                st.metric("Operating Cost", f"${operating_cost:.2f}/h")

    # -------------------------------------------------------------------------
    # CARBON CAPTURE
    elif case_study == "Carbon Capture":
        st.markdown("## CO₂ Capture System")
   
        st.markdown("🎯 Problem Definition & Formulas")
        st.write("""
        Design a carbon capture system and calculate capture efficiency and costs.
        """)
        st.latex(r"CO_2\ Captured = Flow \times Concentration \times Efficiency \times \rho_{CO_2}")
        st.latex(r"Regeneration\ Energy = CO_2\ Captured \times Specific\ Energy")
        st.markdown("""
        **Formula Components:**
        1. **Flow:** Flue gas flow rate (m³/h).
        2. **Concentration:** CO₂ concentration (vol%).
        3. **ρ_CO₂:** CO₂ density (1.98 kg/m³ at STP).
        4. **Efficiency:** Capture efficiency (%).
        5. **Specific Energy:** Regeneration energy requirement (GJ/ton CO₂).
        """)

        st.markdown("### 📝 Input Parameters")
        col1, col2, col3 = st.columns(3)
        with col1:
            flue_gas = st.number_input("Flue Gas Flow (m³/h)", 1000, 100000, 10000)
        with col2:
            co2_conc = st.slider("CO₂ Concentration (vol%)", 5, 20, 12)
        with col3:
            capture_eff = st.slider("Target Capture Efficiency (%)", 50, 95, 90)

        adsorbent = st.selectbox("Select Adsorbent", ["Zeolite 13X", "Activated Carbon", "Amine-modified Silica"])
        adsorbent_props = {
            "Zeolite 13X": {"regeneration_energy": 3.2, "cost": 2.0},
            "Activated Carbon": {"regeneration_energy": 2.4, "cost": 1.5},
            "Amine-modified Silica": {"regeneration_energy": 2.8, "cost": 3.0}
        }
        with st.expander("📚 Theoretical Background"):
            st.markdown("""
            **Process Fundamentals:**
            - Follows temperature swing adsorption (TSA).
            - CO₂ selectivity over N₂ crucial.
            - Heat of adsorption determines energy needs.
            
            **Key Parameters:**
            - Adsorption temperature: 40-60°C.
            - Regeneration temperature: 100-150°C.
            - CO₂ concentration: 10-15 vol%.
            """)  

        with st.expander("💰 Economic Considerations"):
            st.markdown("""
            **Material Costs ($/kg):**
            - Zeolite 13X: 2-4.
            - Activated Carbon: 1.5-3.
            - Amine-modified Silica: 3-6.
            
            **Operating Costs:**
            - Regeneration energy: 2.5-4 GJ/ton CO₂.
            - Steam cost: $15-25/ton.
            - Maintenance: 3% of capital/year.
            """)

        if st.checkbox("Show Detailed Solution"):
            co2_flow = flue_gas * (co2_conc/100)  # m³/h of CO₂
            co2_captured = co2_flow * (capture_eff/100) * 1.98  # kg/h, using CO₂ density
            regen_energy = co2_captured * adsorbent_props[adsorbent]["regeneration_energy"] / 1000  # GJ/h
            energy_cost = regen_energy * 8  # Assuming $8/GJ
            material_cost = co2_captured * adsorbent_props[adsorbent]["cost"] / 1000  # $/h
            total_operating_cost = energy_cost + material_cost
            
            st.markdown("### 🔍 Solution Analysis")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("CO₂ Captured", f"{co2_captured:.1f} kg/h")
                st.metric("Regeneration Energy", f"{regen_energy:.2f} GJ/h")
            with col2:
                st.metric("Energy Cost", f"${energy_cost:.2f}/h")
                st.metric("Material Cost", f"${material_cost:.2f}/h")
            
            st.write("#### Step 1: CO₂ Capture Calculation")
            st.latex(rf"CO_2\ Captured = {flue_gas} \times \frac{{{co2_conc}}}{{100}} \times \frac{{{capture_eff}}}{{100}} \times 1.98 \approx {co2_captured:.1f}\ kg/h")
            
            st.write("#### Step 2: Economic Analysis")
            st.latex(rf"Total\ Operating\ Cost = {energy_cost:.2f} + {material_cost:.2f} = {total_operating_cost:.2f}\ $/h")

if __name__ == "__main__":
    app()