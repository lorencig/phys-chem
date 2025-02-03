import streamlit as st
import math

def app():
    st.title("Industrial Case Studies: Problem & Solution Exercises")
    
    case_study = st.selectbox("Select Case Study", 
                              ["Gas Storage", "Water Treatment", "Air Purification", "Carbon Capture"])

    # -------------------------------------------------------------------------
    if case_study == "Gas Storage":
    
        # Title and Introduction
        st.markdown("## Hydrogen Storage in Metal-Organic Frameworks (MOFs)")
        st.write("""
        This case study focuses on designing a hydrogen (H₂) storage system using MOFs. The problem is divided into three main objectives:
        
        1. **Determine the H₂ Storage Capacity:**  
        Calculate the maximum amount of H₂ (by weight percentage) that the chosen MOF can store at a given temperature and pressure.
        
        2. **Compute the Required MOF Amount:**  
        Determine the mass of MOF material needed to store a specified amount of H₂.
        
        3. **Estimate the Material Cost:**  
        Calculate the total cost of the MOF material required for the storage system.
        
        The base capacity is adjusted using a formula that accounts for deviations in pressure and temperature from the reference conditions.
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
        The adjusted H₂ storage capacity is calculated using the following formula:
        
        $$
        \text{Capacity (wt\%)} = \text{Reference Capacity} \times \frac{\text{Pressure}}{50} \times \frac{77}{\text{Temperature}}
        $$
        
        **Where:**
        - **Reference Capacity:** The base H₂ storage capacity of the MOF at standard conditions (77 K and 50 bar).
        - **Pressure Adjustment ($\frac{\text{Pressure}}{50}$):** Scales the capacity based on the actual operating pressure relative to the reference pressure.
        - **Temperature Adjustment ($\frac{77}{\text{Temperature}}$):** Scales the capacity based on the actual operating temperature relative to the reference temperature (77 K).
        
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
        
        # Display Reference Capacity
        st.markdown(f"""
        **Reference Capacity for {mof_type}:**  
        The reference capacity of the selected MOF (**{mof_type}**) is **{props['h2_capacity']} wt%** at **77 K** and **50 bar**.
        """)
        
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
            **Material Costs (\€/kg):**
            
            - **HKUST-1:** \€200 per kg (copper-based, moderate cost)
            - **MOF-5:**   \€300 per kg (zinc-based, high purity)
            - **UiO-66:**  \€150 per kg (zirconium-based, economical)
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
            mof_required = system_scale / (capacity / 100)
            mof_costs = {"HKUST-1": 200, "MOF-5": 300, "UiO-66": 150}
            material_cost = mof_required * mof_costs[mof_type]
            
            st.write(f"To store **{system_scale} kg** of H₂, the amount of MOF required is computed as:")
            st.latex(r"\text{MOF Required (kg)} = \frac{\text{System Scale (kg H₂)}}{\text{Capacity (wt\%)} / 100}")
            st.latex(r"\text{MOF Required} = \frac{" + f"{system_scale}" + r"}{" + f"{capacity/100:.2f}" + r"} = " + f"{mof_required:.1f}\\,kg")
            st.write(f"This means you need **{mof_required:.1f} kg** of {mof_type}.")
            
            st.write("Next, we calculate the material cost using the cost per kilogram for the selected MOF:")
            st.latex(r"\text{Material Cost} = \text{MOF Required} \times \text{Cost per kg}")
            st.latex(r"\text{Material Cost} = " + f"{mof_required:.1f} \\times {mof_costs[mof_type]} = €{material_cost:,.2f}")
            st.write(f"The total material cost for {mof_type} is **€{material_cost:,.2f}**.")
            
            # Step 3: Summarize the Results
            st.markdown("#### Step 3: Summary of Results")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Gravimetric Capacity", f"{capacity:.2f} wt%")
                st.metric("Volumetric Capacity", f"{volumetric_capacity:.2f} kg/m³")
            with col2:
                st.metric("Required MOF", f"{mof_required:.1f} kg")
                st.metric("Material Cost", f"€{material_cost:,.2f}")
            
            st.markdown("**Conclusion:**")
            st.write(f"""
            - **Storage Capacity:**  
            The selected MOF (**{mof_type}**) has an adjusted hydrogen storage capacity of **{capacity:.2f} wt%** at {temperature} K and {pressure} bar.
            
            - **MOF Material Requirement:**  
            To store **{system_scale} kg** of H₂, you need **{mof_required:.1f} kg** of the MOF.
            
            - **Cost Analysis:**  
            The material cost for the required amount of {mof_type} is **€{material_cost:,.2f}**.
            
            - **Volumetric Efficiency:**  
            The volumetric capacity is **{volumetric_capacity:.2f} kg/m³**, which helps evaluate the space utilization of the storage system.
            """)

    # -------------------------------------------------------------------------
    elif case_study == "Water Treatment":
    # Title and Introduction
        st.markdown("## Advanced Water Treatment System")
        st.write("""
        This case study evaluates contaminant removal efficiency and system economics for a water treatment process using adsorption technology. The problem is divided into three main objectives:
        
        1. **Calculate Removal Efficiency:**  
        Determine the percentage removal of contaminants using the Freundlich adsorption model.
        
        2. **Compute Material Requirements:**  
        Calculate daily adsorbent consumption and associated costs.
        
        3. **Estimate Operating Costs:**  
        Analyze the total daily operating costs of the treatment system.
        """)
        
        # Problem Statement Section
        st.markdown("### 🎯 Problem Statement")
        st.markdown("""
        **Objective:**  
        Design a water treatment system using adsorption technology and compute:
        
        - Contaminant removal efficiency under specified conditions
        - Daily adsorbent material requirements
        - Total operating costs
        
        **Key Questions:**
        1. *Removal Efficiency:* What percentage of contaminants is removed at the given adsorbent dose?
        2. *Material Requirements:* How much adsorbent (in kg) is needed daily?
        3. *Cost Analysis:* What are the daily material and operating costs?
        """)
        
        # Formula Explanation
        st.markdown("### 📝 Formula Explanation")
        st.markdown(r"""
        The contaminant removal efficiency is calculated using the **Freundlich Isotherm** model:
        
        $$
        C = \frac{C_0}{1 + K_F \times D^{1/n}}
        $$
        
        $$
        \text{Removal (\%)} = \left(1 - \frac{C}{C_0}\right) \times 100
        $$
        
        **Where:**
        - **$C_0$:** Initial contaminant concentration (mg/L)
        - **$C$:** Final contaminant concentration (mg/L)
        - **$K_F$:** Freundlich capacity constant (L/g)
        - **$D$:** Adsorbent dose (g/L)
        - **$n$:** Freundlich intensity parameter (unitless)
        """)
        
        # Input Parameters
        st.markdown("### 📝 Input Parameters")
        
        # Adsorbent Selection and Properties
        adsorbent_type = st.selectbox("Select Adsorbent Type", 
                                    ["Activated Carbon", "Ion Exchange Resin", "Zeolites"])
        
        adsorbent_properties = {
            "Activated Carbon": {"kf": 20, "n": 2.5, "cost": 3.5},
            "Ion Exchange Resin": {"kf": 35, "n": 1.8, "cost": 12.0},
            "Zeolites": {"kf": 15, "n": 2.2, "cost": 7.5}
        }
        props = adsorbent_properties[adsorbent_type]
        
        # Display Freundlich Parameters
        st.markdown(f"""
        **Freundlich Parameters for {adsorbent_type}:**  
        - Capacity constant ($K_F$): **{props['kf']} L/g**  
        - Intensity parameter ($n$): **{props['n']}**
        """)
        
        # System Parameters
        col1, col2, col3 = st.columns(3)
        with col1:
            initial_conc = st.number_input("Initial Concentration (mg/L)", 1, 1000, 100,
                                        help="Contaminant concentration in raw water")
        with col2:
            adsorbent_dose = st.number_input("Adsorbent Dose (g/L)", 0.1, 10.0, 2.0,
                                        help="Mass of adsorbent per liter of water")
        with col3:
            treatment_volume = st.number_input("Treatment Volume (m³/day)", 10, 10000, 1000,
                                            help="Daily water processing capacity")
        
        # Theoretical Background
        with st.expander("📚 Theoretical Background"):
            st.markdown("""
            **Process Fundamentals:**
            - Adsorption follows Freundlich isotherm behavior
            - Mass transfer limited by film diffusion
            - Optimal contact time: 15-30 minutes
            - Effective pH range: 4-8
            
            **Key Assumptions:**
            - Complete mixing in contact basin
            - Equilibrium conditions achieved
            - Negligible competitive adsorption
            """)
        
        # Economic Considerations
        with st.expander("💰 Economic Considerations"):
            st.markdown(f"""
            **Cost Parameters for {adsorbent_type}:**
            - Material Cost: **€{props['cost']}/kg**  
            - Regeneration Cost: **€0.75-1.25/m³**  
            - Disposal Cost: **€80-120/ton**
            
            **Typical Operating Costs:**
            - Energy Consumption: 0.1-0.3 kWh/m³
            - Labor: €0.15-0.30/m³
            - Maintenance: €0.05-0.10/m³
            """)
        
        # Detailed Solution
        if st.checkbox("Show Detailed Solution"):
            st.markdown("### 🔍 Detailed Step-by-Step Solution")
            
            # Step 1: Calculate Final Concentration
            st.markdown("#### Step 1: Calculate Final Concentration")
            final_conc = initial_conc / (1 + props["kf"] * (adsorbent_dose ** (1/props["n"])))
            
            st.write("Using the Freundlich isotherm equation with the selected adsorbent parameters:")
            st.latex(r"C = \frac{" + f"{initial_conc}" + r"}{1 + " + 
                    f"{props['kf']} \\times ({adsorbent_dose}^{{1/{props['n']}}})}} = {final_conc:.2f} \, \text{{mg/L}}")
            
            # Step 2: Calculate Removal Efficiency
            st.markdown("#### Step 2: Determine Removal Efficiency")
            removal = (1 - final_conc/initial_conc) * 100
            
            st.write("Calculating removal efficiency from initial and final concentrations:")
            st.latex(r"\text{Removal} = \left(1 - \frac{" + f"{final_conc:.2f}" + r"}{" + 
                    f"{initial_conc}" + r"}\right) \times 100 = " + f"{removal:.1f}\%")
            
            # Step 3: Calculate Material Requirements
            st.markdown("#### Step 3: Compute Daily Material Needs")
            daily_adsorbent = adsorbent_dose * treatment_volume  # Convert g/L to kg/m³ (1 g/L = 1 kg/m³)
            material_cost = daily_adsorbent * props["cost"]
            
            st.write(f"Daily adsorbent requirement for {treatment_volume} m³ treatment volume:")
            st.latex(r"\text{Daily Adsorbent} = " + f"{adsorbent_dose} \, \text{{g/L}} \\times {treatment_volume} \, \text{{m³/day}} = {daily_adsorbent:,.1f} \, \text{{kg/day}}")
            st.write(f"Material cost at €{props['cost']}/kg:")
            st.latex(r"\text{Material Cost} = " + f"{daily_adsorbent:,.1f} \\times {props['cost']} = €{material_cost:,.2f}")
            
            # Step 4: Calculate Operating Costs
            st.markdown("#### Step 4: Estimate Operating Costs")
            operating_cost = treatment_volume * 0.25  # Average of typical energy+maintenance costs
            
            st.write("Calculating total operating costs (energy, labor, maintenance):")
            st.latex(r"\text{Operating Cost} = " + f"{treatment_volume} \, \text{{m³/day}} \\times 0.25 \, \text{{€/m³}} = €{operating_cost:,.2f}")
            
            # Results Summary
            st.markdown("#### Step 5: Summary of Results")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Final Concentration", f"{final_conc:.2f} mg/L")
                st.metric("Removal Efficiency", f"{removal:.1f}%")
            with col2:
                st.metric("Daily Adsorbent Needed", f"{daily_adsorbent:,.1f} kg")
                st.metric("Total Daily Cost", f"€{material_cost + operating_cost:,.2f}")
            
            st.markdown("**Conclusion:**")
            st.write(f"""
            - **Treatment Performance:**  
            The system achieves **{removal:.1f}% contaminant removal**, reducing concentration from **{initial_conc} mg/L** to **{final_conc:.2f} mg/L**.
            
            - **Material Requirements:**  
            Requires **{daily_adsorbent:,.1f} kg/day** of {adsorbent_type} at a cost of **€{material_cost:,.2f}/day**.
            
            - **Operating Costs:**  
            Total daily operating costs are **€{operating_cost:,.2f}**, including energy, labor, and maintenance.
            
            - **System Effectiveness:**  
            The Freundlich intensity parameter (n = {props['n']}) indicates {"favorable" if props['n'] > 2 else "moderate"} adsorption conditions.
            """)

    # -------------------------------------------------------------------------
    elif case_study == "Air Purification":
    # Title and Introduction
        st.markdown("## VOC Removal System for Industrial Air Purification")
        st.write("""
        This case study evaluates the performance and economics of a volatile organic compound (VOC) removal system. The analysis focuses on three key objectives:
        
        1. **Calculate Removal Efficiency:**  
        Determine VOC removal percentage using adsorption kinetics.
        
        2. **Estimate Energy Consumption:**  
        Compute system power requirements based on airflow characteristics.
        
        3. **Analyze Operational Costs:**  
        Evaluate hourly and annual operating costs for the purification system.
        """)
        
        # Problem Statement Section
        st.markdown("### 🎯 Problem Statement")
        st.markdown("""
        **Objective:**  
        Design an air purification system for VOC removal and compute:
        
        - VOC removal efficiency at specified operating conditions
        - System pressure drop and energy requirements
        - Operational costs per hour
        
        **Key Questions:**
        1. *Removal Efficiency:* What percentage of VOCs is removed at the given contact time?
        2. *Energy Requirements:* How much power does the system consume?
        3. *Cost Analysis:* What are the operational costs per hour?
        """)
        
        # Formula Explanation
        st.markdown("### 📝 Formula Explanation")
        st.markdown(r"""
        The VOC removal efficiency is calculated using **adsorption kinetics**:
        
        $$
        \text{Removal (\%)} = 100 \times \left(1 - e^{-k \tau}\right)
        $$
        
        **Where:**
        - **$k$:** Adsorption rate constant (s⁻¹)
        - **$\tau$:** Contact time (s)
        - **$e$:** Base of natural logarithm
        
        Pressure drop is calculated through empirical correlation:
        $$
        \Delta P = \alpha \times \tau \times Q^{0.5}
        $$
        """)
        
        # Input Parameters
        st.markdown("### 📝 Input Parameters")
        
        # Adsorbent Selection and Properties
        adsorbent_type = st.selectbox("Select Adsorbent Material", 
                                    ["Activated Carbon", "Molecular Sieves", "Polymeric Adsorbents"])
        
        adsorbent_properties = {
            "Activated Carbon": {"k": 0.65, "alpha": 0.12, "cost": 5.5},
            "Molecular Sieves": {"k": 0.85, "alpha": 0.18, "cost": 15.0},
            "Polymeric Adsorbents": {"k": 0.45, "alpha": 0.09, "cost": 20.0}
        }
        props = adsorbent_properties[adsorbent_type]
        
        # Display Adsorption Parameters
        st.markdown(f"""
        **Adsorption Parameters for {adsorbent_type}:**  
        - Rate constant ($k$): **{props['k']} s⁻¹**  
        - Pressure coefficient ($α$): **{props['alpha']}**
        """)
        
        # System Parameters
        col1, col2, col3 = st.columns(3)
        with col1:
            flow_rate = st.number_input("Air Flow Rate (m³/h)", 100, 10000, 1000,
                                    help="Volumetric airflow through the system")
        with col2:
            voc_conc = st.number_input("VOC Concentration (ppm)", 1, 1000, 100,
                                    help="Initial VOC concentration in contaminated air")
        with col3:
            contact_time = st.slider("Contact Time (s)", 1, 10, 3,
                                help="Residence time in adsorption bed")
        
        # Theoretical Background
        with st.expander("📚 Theoretical Background"):
            st.markdown("""
            **Process Fundamentals:**
            - Follows Tóth isotherm adsorption behavior
            - Mass transfer limited by pore diffusion
            - Breakthrough occurs at 5% of inlet concentration
            
            **Key Assumptions:**
            - Ideal plug flow conditions
            - Isothermal operation (25°C)
            - Negligible humidity effects
            - Fresh adsorbent properties
            """)
        
        # Economic Considerations
        with st.expander("💰 Economic Considerations"):
            st.markdown(f"""
            **Cost Parameters for {adsorbent_type}:**
            - Material Cost: **€{props['cost']}/kg**  
            - Replacement Frequency: **Every 9-12 months**  
            - Regeneration Cost: **€0.50-1.00/kg**
            
            **Typical Operating Costs:**
            - Electricity Rate: €0.12/kWh
            - Maintenance: 7% of capital cost/year
            - Labor: €25-50/hour
            """)
        
        # Detailed Solution
        if st.checkbox("Show Detailed Solution"):
            st.markdown("### 🔍 Detailed Step-by-Step Solution")
            
            # Step 1: Calculate Removal Efficiency
            st.markdown("#### Step 1: Calculate VOC Removal Efficiency")
            removal = 100 * (1 - math.exp(-props["k"] * contact_time))
            
            st.write("Using the adsorption kinetic equation with system parameters:")
            st.latex(r"\text{Removal} = 100 \times \left(1 - e^{-" + 
                    f"{props['k']} \\times {contact_time}" + r"}\right) = " + 
                    f"{removal:.1f}\%")
            
            # Step 2: Calculate Pressure Drop
            st.markdown("#### Step 2: Determine System Pressure Drop")
            pressure_drop = props["alpha"] * contact_time * (flow_rate**0.5)
            
            st.write("Calculating pressure drop through adsorption bed:")
            st.latex(r"\Delta P = " + f"{props['alpha']} \\times {contact_time} \\times ({flow_rate}^{{0.5}}) = {pressure_drop:.2f} \, \text{{Pa}}")
            
            # Step 3: Calculate Power Consumption
            st.markdown("#### Step 3: Compute Energy Requirements")
            power_consumption = (flow_rate * pressure_drop) / (3600 * 0.65)  # 0.65 = fan efficiency
            
            st.write("Converting pressure drop to fan power consumption:")
            st.latex(r"P = \frac{Q \times \Delta P}{3600 \times \eta} = " + 
                    f"\\frac{{{flow_rate} \\times {pressure_drop:.2f}}}{{3600 \\times 0.65}} = {power_consumption:.2f} \, \text{{kW}}")
            
            # Step 4: Calculate Operating Costs
            st.markdown("#### Step 4: Estimate Operational Costs")
            energy_cost = power_consumption * 0.12  # €0.12/kWh
            maintenance_cost = power_consumption * 0.07  # 7% of energy cost
            
            st.write("Calculating hourly operational costs:")
            st.latex(r"\text{Energy Cost} = " + f"{power_consumption:.2f} \\times 0.12 = €{energy_cost:.2f}")
            st.latex(r"\text{Maintenance Cost} = " + f"{power_consumption:.2f} \\times 0.07 = €{maintenance_cost:.2f}")
            
            # Results Summary
            st.markdown("#### Step 5: Summary of Results")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("VOC Removal Efficiency", f"{removal:.1f}%")
                st.metric("System Pressure Drop", f"{pressure_drop:.2f} Pa")
            with col2:
                st.metric("Power Consumption", f"{power_consumption:.2f} kW")
                st.metric("Total Hourly Cost", f"€{energy_cost + maintenance_cost:.2f}")
            
            st.markdown("**Conclusion:**")
            st.write(f"""
            - **Removal Performance:**  
            Achieves **{removal:.1f}% VOC removal** at {contact_time}s contact time using {adsorbent_type}.
            
            - **Energy Requirements:**  
            Requires **{power_consumption:.2f} kW** continuous power input to maintain {flow_rate} m³/h airflow.
            
            - **Economic Analysis:**  
            Hourly operating costs total **€{energy_cost + maintenance_cost:.2f}** (energy + maintenance).
            
            - **System Design:**  
            The pressure drop of **{pressure_drop:.2f} Pa** indicates {"efficient" if pressure_drop < 500 else "high-resistance"} flow conditions.
            """)

    # -------------------------------------------------------------------------
    elif case_study == "Carbon Capture":
        # Title and Introduction
        st.markdown("## Industrial CO₂ Capture System")
        st.write("""
        This case study evaluates the technical and economic feasibility of a post-combustion carbon capture system. The analysis focuses on three key objectives:
        
        1. **Calculate Capture Capacity:**  
        Determine hourly CO₂ capture rates based on flue gas characteristics.
        
        2. **Estimate Energy Requirements:**  
        Compute regeneration energy needs for adsorbent material.
        
        3. **Analyze Operational Costs:**  
        Evaluate hourly operating costs in euro currency.
        """)
        
        # Problem Statement Section
        st.markdown("### 🎯 Problem Statement")
        st.markdown("""
        **Objective:**  
        Design a carbon capture system using adsorption technology and compute:
        
        - CO₂ capture rate under specified conditions
        - Energy requirements for adsorbent regeneration
        - Operational costs per hour
        
        **Key Questions:**
        1. *Capture Capacity:* How much CO₂ can be captured hourly?
        2. *Energy Demand:* What regeneration energy is required?
        3. *Cost Analysis:* What are the hourly operational costs?
        """)
        
        # Formula Explanation
        st.markdown("### 📝 Formula Explanation")
        st.markdown(r"""
        The CO₂ capture rate is calculated using:
        
        $$
        \text{CO}_2\ \text{Captured (kg/h)} = Q_{\text{flue}} \times C_{\text{CO}_2} \times \eta \times \rho_{\text{CO}_2}
        $$
        
        **Where:**
        - **$Q_{\text{flue}}$:** Flue gas flow rate (m³/h)
        - **$C_{\text{CO}_2}$:** CO₂ concentration (vol%)
        - **$\eta$:** Capture efficiency (%)
        - **$\rho_{\text{CO}_2}$:** CO₂ density (1.98 kg/m³ at STP)
        """)
        
        # Input Parameters
        st.markdown("### 📝 Input Parameters")
        
        # Adsorbent Selection and Properties
        adsorbent = st.selectbox("Select Adsorbent Material", 
                            ["Zeolite 13X", "Activated Carbon", "Amine-modified Silica"])
        
        adsorbent_props = {
            "Zeolite 13X": {"regeneration_energy": 3.2, "cost": 2.0},
            "Activated Carbon": {"regeneration_energy": 2.4, "cost": 1.5},
            "Amine-modified Silica": {"regeneration_energy": 2.8, "cost": 3.0}
        }
        props = adsorbent_props[adsorbent]
        
        # Display Adsorbent Properties
        st.markdown(f"""
        **Adsorption Parameters for {adsorbent}:**  
        - Regeneration Energy: **{props['regeneration_energy']} GJ/ton CO₂**  
        - Material Cost: **€{props['cost']}/kg**
        """)
        
        # System Parameters
        col1, col2, col3 = st.columns(3)
        with col1:
            flue_gas = st.number_input("Flue Gas Flow (m³/h)", 1000, 100000, 10000,
                                    help="Total flue gas volume flow rate")
        with col2:
            co2_conc = st.slider("CO₂ Concentration (vol%)", 5, 20, 12,
                            help="CO₂ content in flue gas")
        with col3:
            capture_eff = st.slider("Target Capture Efficiency (%)", 50, 95, 90,
                                help="System capture performance")
        
        # Theoretical Background
        with st.expander("📚 Theoretical Background"):
            st.markdown("""
            **Process Fundamentals:**
            - Temperature Swing Adsorption (TSA) technology
            - Selective CO₂ adsorption isotherms
            - Cyclic adsorption/desorption operation
            
            **Key Assumptions:**
            - Standard temperature and pressure (STP) conditions
            - Ideal gas behavior
            - Steady-state operation
            - 90% adsorbent utilization efficiency
            """)
        
        # Economic Considerations
        with st.expander("💰 Economic Considerations"):
            st.markdown(f"""
            **Cost Parameters for {adsorbent}:**
            - Material Replacement: **€{props['cost']*1.2:.1f}-{props['cost']*1.5:.1f}/kg**  
            - Steam Generation: **€18-22/ton**  
            - Maintenance: **3.5% of capital cost/year**
            
            **Energy Costs:**
            - Thermal Energy: **€7-9/GJ**
            - Electricity: **€0.15/kWh**
            - Carbon Credit Value: **€50-80/ton CO₂**
            """)
        
        # Detailed Solution
        if st.checkbox("Show Detailed Solution"):
            st.markdown("### 🔍 Detailed Step-by-Step Solution")
            
            # Step 1: Calculate CO₂ Capture Rate
            st.markdown("#### Step 1: Calculate CO₂ Capture Rate")
            co2_flow = flue_gas * (co2_conc/100)
            co2_captured = co2_flow * (capture_eff/100) * 1.98
            
            st.write("Using flue gas characteristics and capture efficiency:")
            st.latex(rf"\text{{CO}}_2\ \text{{Captured}} = {flue_gas} \times \frac{{{co2_conc}}}{{100}} \times \frac{{{capture_eff}}}{{100}} \times 1.98 = {co2_captured:.1f}\ \text{{kg/h}}")
            
            # Step 2: Calculate Regeneration Energy
            st.markdown("#### Step 2: Determine Regeneration Energy")
            regen_energy = (co2_captured / 1000) * props["regeneration_energy"]
            
            st.write("Calculating thermal energy required for adsorbent regeneration:")
            st.latex(rf"\text{{Energy}} = \frac{{{co2_captured:.1f}}}{{1000}} \times {props['regeneration_energy']} = {regen_energy:.2f}\ \text{{GJ/h}}")
            
            # Step 3: Calculate Operational Costs
            st.markdown("#### Step 3: Compute Operational Costs")
            energy_cost = regen_energy * 8  # €8/GJ
            material_use = (co2_captured / 1000) * 0.05  # 5% adsorbent replacement rate
            material_cost = material_use * props["cost"]
            
            st.write("Breaking down hourly operational costs:")
            st.latex(rf"\text{{Energy Cost}} = {regen_energy:.2f} \times 8 = €{energy_cost:.2f}")
            st.latex(rf"\text{{Material Cost}} = ({co2_captured:.1f}/1000) \times 0.05 \times {props['cost']} = €{material_cost:.2f}")
            
            # Results Summary
            st.markdown("#### Step 4: Summary of Results")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("CO₂ Capture Rate", f"{co2_captured:.1f} kg/h")
                st.metric("Regeneration Energy", f"{regen_energy:.2f} GJ/h")
            with col2:
                st.metric("Energy Costs", f"€{energy_cost:.2f}/h")
                st.metric("Material Costs", f"€{material_cost:.2f}/h")
            
            st.markdown("**Conclusion:**")
            st.write(f"""
            - **Capture Performance:**  
            The system captures **{co2_captured:.1f} kg CO₂/h** from {flue_gas} m³/h flue gas at {co2_conc}% concentration.
            
            - **Energy Requirements:**  
            Requires **{regen_energy:.2f} GJ/h** thermal energy for {adsorbent} regeneration.
            
            - **Cost Analysis:**  
            Total hourly operating costs reach **€{energy_cost + material_cost:.2f}** (energy + materials).
            
            - **Environmental Impact:**  
            Equivalent to removing emissions from {"{:,}".format(int(flue_gas//200))} EU average cars hourly.
            """)
if __name__ == "__main__":
    app()
