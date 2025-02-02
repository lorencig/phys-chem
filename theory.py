import streamlit as st

def app():
    st.title("Theory")
    st.markdown("Select a model from the dropdown to view its theoretical background, key assumptions, and a detailed breakdown of the calculations.")
    model_choice = st.selectbox("Select Model", ["Langmuir adsorption model", "BET theory", "Freundlich Equation", "Temkin Isotherm"])

    if model_choice == "Langmuir adsorption model":
        st.markdown("""
        <div style="text-align: justify;">
                    
        # Langmuir Adsorption Model

        ## 1. Author, Year
        - **Author**: Irving Langmuir  
        - **Year**: 1916  

        ## 2. Application/Usage
        - The Langmuir equation is widely used to describe **adsorption phenomena** in gas-solid and liquid-solid systems.  
        - It is applied to model **monolayer adsorption** on homogeneous surfaces, particularly in environmental chemistry, catalysis, and material science.  

        ## 3. Short Summary
        The Langmuir equation is a **theoretical model** that describes the adsorption of molecules onto a surface as a reversible process. It assumes a **homogeneous surface** with a finite number of identical adsorption sites, each capable of holding only one molecule. The model predicts that adsorption reaches a maximum (monolayer coverage) as the adsorbate pressure or concentration increases.  

        ## 4. Formula
        The Langmuir equation is expressed as:  
        $$
        \\theta = \\frac{K_a \\cdot p}{1 + K_a \\cdot p}
        $$  
        Where:  
        - $\\theta$: Fraction of surface sites occupied by the adsorbate (dimensionless).  
        - $K_a$: Adsorption equilibrium constant (related to the affinity of the adsorbate for the surface).  
        - $p$: Partial pressure of the adsorbate in the gas phase (or concentration in the liquid phase).  

        The amount of adsorbed material ($Q$) is calculated as:  
        $$
        Q = Q_{\\text{max}} \\cdot \\theta
        $$  
        Where:  
        - $Q_{\\text{max}}$: Maximum adsorption capacity (mol/kg).  

        ## 5. Detailed Calculation Breakdown

        ### Step 1: Calculate the Adsorption Equilibrium Constant ($K_a$)
        The adsorption equilibrium constant ($K_a$) is calculated using the enthalpy ($\\Delta H$) and entropy ($\\Delta S$) of adsorption:  
        $$
        K_a = \\exp\\left(\\frac{-\\Delta H}{RT} + \\frac{\\Delta S}{R}\\right)
        $$  
        - $\\Delta H$: Enthalpy of adsorption (kJ/mol).  
        - $\\Delta S$: Entropy of adsorption (J/mol·K).  
        - $R$: Universal gas constant (8.314 J/K/mol).  
        - $T$: Temperature (K).  

        ### Step 2: Calculate the Fraction of Surface Coverage ($\\theta$)
        For each pressure ($p$), calculate the fraction of surface coverage ($\\theta$) using the Langmuir equation:  
        $$
        \\theta = \\frac{K_a \\cdot p}{1 + K_a \\cdot p}
        $$  
        - $p$: Partial pressure of the adsorbate (bar).  
        - $K_a$: Adsorption equilibrium constant (dimensionless).  

        ### Step 3: Calculate the Amount of Adsorbed Material ($Q$)
        The amount of adsorbed material ($Q$) is calculated as:  
        $$
        Q = Q_{\\text{max}} \\cdot \\theta
        $$  
        - $Q_{\\text{max}}$: Maximum adsorption capacity (mol/kg).  
        - $\\theta$: Fraction of surface coverage (dimensionless).  

        ### Units and Results
        - $Q$ is expressed in **mol/kg**, representing the amount of adsorbate bound per kilogram of adsorbent.  
        - $Q_{\\text{max}}$ is the theoretical maximum adsorption capacity of the adsorbent.  

        ## 6. Key Notes
        - The Langmuir model is most suitable for **monolayer adsorption** on **homogeneous surfaces**.  
        - The linearized form of the Langmuir equation is used to determine $K_a$ and $Q_{\\text{max}}$:  
        $$
        \\frac{p}{Q} = \\frac{1}{K_a \\cdot Q_{\\text{max}}} + \\frac{p}{Q_{\\text{max}}}
        $$  

        **Reference:** [Langmuir, 1916](https://pubs.acs.org/doi/10.1021/ja02242a004)        
        </div>
        """, unsafe_allow_html=True)

    elif model_choice == "BET theory":
        st.markdown("""
        <div style="text-align: justify;">
                    
        # BET Theory

        ## 1. Author, Year
        - **Authors**: Stephen Brunauer, Paul Hugh Emmett, and Edward Teller  
        - **Year**: 1938  

        ## 2. Application/Usage
        - The BET theory is widely used to determine the **specific surface area** of solid or porous materials by measuring gas adsorption.  
        - It is applied in fields such as **material science**, **catalysis**, **pharmaceuticals**, **battery technology**, and **ceramics**.  

        ## 3. Short Summary
        The BET theory describes **multilayer gas adsorption** on solid surfaces and is used to calculate the **specific surface area** of materials. It assumes that gas molecules adsorb in layers, with the first layer having a higher adsorption energy than subsequent layers. The theory is particularly useful for analyzing **nonporous** and **porous materials**, including those with high surface areas like activated carbon and catalysts.  

        ## 4. Formula
        The BET equation is expressed as:  
        $$
        \\frac{P}{V(P_0 - P)} = \\frac{1}{V_m \\cdot C} + \\frac{C - 1}{V_m \\cdot C} \\cdot \\frac{P}{P_0}
        $$  
        Where:  
        - $P$: Equilibrium pressure of the adsorbate gas (bar).  
        - $P_0$: Saturation pressure of the adsorbate gas (bar).  
        - $V$: Volume of gas adsorbed at pressure $P$ (cm³/g).  
        - $V_m$: Volume of gas required to form a **monolayer** on the surface (cm³/g).  
        - $C$: BET constant related to the heat of adsorption (dimensionless).  

        ## 5. Detailed Calculation Breakdown

        ### Step 1: Measure Gas Adsorption
        - Measure the volume of gas ($V$) adsorbed at various pressures ($P$).  

        ### Step 2: Calculate $V_m$ (Monolayer Volume)
        - Plot $\\frac{P}{V(P_0 - P)}$ vs. $\\frac{P}{P_0}$ to obtain a linear relationship.  
        - Determine $V_m$ from the slope and intercept of the BET plot:  
        $$
        V_m = \\frac{1}{\\text{slope} + \\text{intercept}}
        $$  

        ### Step 3: Calculate Specific Surface Area ($S$)
        - Use $V_m$ to calculate the specific surface area:  
        $$
        S = \\frac{V_m \\cdot N_A \\cdot \\sigma}{M}
        $$  
        - $N_A$: Avogadro's number (6.022 × 10²³ molecules/mol).  
        - $\\sigma$: Cross-sectional area of the adsorbate molecule (m²).  
        - $M$: Molar volume of the adsorbate gas (cm³/mol).  

        ### Units and Results
        - $V_m$ is expressed in **cm³/g**, representing the volume of gas required to form a monolayer.  
        - $S$ is expressed in **m²/g**, representing the specific surface area of the material.  

        ## 6. Key Notes
        - The BET method is most suitable for **nonporous** and **mesoporous** materials.  
        - For **microporous materials**, additional methods like **CO₂ adsorption** or **NLDFT** are recommended.  

        **Reference:** [Brunauer, Emmett, and Teller, 1938](https://pubs.acs.org/doi/10.1021/ja01269a023)     
        </div>
        """, unsafe_allow_html=True)

    elif model_choice == "Freundlich Equation":
        st.markdown("""
        <div style="text-align: justify;">
                    
        # Freundlich Equation

        ## 1. Author, Year
        - **Author**: Herbert Freundlich  
        - **Year**: 1906  

        ## 2. Application/Usage
        - The Freundlich equation is widely used to describe **adsorption equilibrium data** in environmental chemistry, particularly for **gas-phase adsorption**.  
        - It is applied to model **heterogeneous adsorption surfaces** with varying adsorption energies.  

        ## 3. Short Summary
        The Freundlich equation is an **empirical model** that describes the relationship between the amount of adsorbate bound to an adsorbent and the equilibrium concentration (or pressure) of the adsorbate. It assumes a **heterogeneous surface** with multiple adsorption sites of different energies and is commonly used for low to moderate adsorbate concentrations.  

        ## 4. Formula
        The Freundlich equation is expressed as:  
        $$
        q = K_d \\cdot C^{1/n}
        $$  
        Where:  
        - $q$: Amount of adsorbate bound per unit weight of adsorbent (mg/kg).  
        - $C$: Equilibrium concentration of adsorbate in the fluid phase (mg/L).  
        - $K_d$: Distribution coefficient (L/kg).  
        - $n$: Correction factor (dimensionless, typically < 1).  

        ## 5. Detailed Calculation Breakdown

        ### Step 1: Determine $K_d$ and $n$
        - Use experimental data to determine $K_d$ and $n$ by linearizing the Freundlich equation:  
        $$
        \\log q = \\frac{1}{n} \\log C + \\log K_d
        $$  
        - Plot $\\log q$ vs. $\\log C$ to obtain a straight line.  
        - The slope is $\\frac{1}{n}$, and the intercept is $\\log K_d$.  

        ### Step 2: Calculate $q$
        - For each concentration ($C$), calculate the amount of adsorbed material ($q$):  
        $$
        q = K_d \\cdot C^{1/n}
        $$  

        ### Units and Results
        - $q$ is expressed in **mg/kg**, representing the amount of adsorbate bound per kilogram of adsorbent.  
        - $C$ is expressed in **mg/L**, representing the equilibrium concentration of the adsorbate.  

        ## 6. Key Notes
        - The Freundlich equation is most suitable for **low to moderate concentrations** and **heterogeneous surfaces**.  
        - It is often compared to the **Langmuir model**, which assumes a homogeneous surface and monolayer adsorption.  

        **Reference:** [Freundlich, 1906](https://doi.org/10.1515/zpch-1907-5723)
        </div>
        """, unsafe_allow_html=True)    

    elif model_choice == "Temkin Isotherm":
        st.markdown("""
        <div style="text-align: justify;">
                    
        # Temkin Isotherm

        ## 1. Author, Year
        - **Author**: Mikhail I. Temkin  
        - **Year**: 1930s  

        ## 2. Application/Usage
        - The Temkin isotherm is used to describe **adsorption processes** where the heat of adsorption decreases linearly with increasing surface coverage.  
        - It is applied in environmental research, catalysis, and adsorption studies of water contaminants.  

        ## 3. Short Summary
        The Temkin isotherm model considers the effect of **indirect adsorbate-adsorbent interactions** on the adsorption process. It assumes that the heat of adsorption decreases linearly with surface coverage and is characterized by a **uniform distribution of binding energies** up to a maximum binding energy.  

        ## 4. Formula
        The Temkin isotherm is expressed as:  
        $$
        q_e = \\frac{RT}{b_T} \\ln(K_T \\cdot C_e)
        $$  
        Where:  
        - $q_e$: Amount of adsorbate adsorbed at equilibrium (mg/g).  
        - $C_e$: Equilibrium concentration of the adsorbate in solution (mg/L).  
        - $K_T$: Equilibrium binding constant (L/mol).  
        - $b_T$: Heat of adsorption parameter (J/mol).  
        - $R$: Universal gas constant (8.314 J/K/mol).  
        - $T$: Temperature (K).  

        ## 5. Detailed Calculation Breakdown

        ### Step 1: Determine $K_T$ and $b_T$
        - Use experimental data to determine $K_T$ and $b_T$ by linearizing the Temkin isotherm:  
        $$
        q_e = \\frac{RT}{b_T} \\ln(K_T) + \\frac{RT}{b_T} \\ln(C_e)
        $$  
        - Plot $q_e$ vs. $\\ln(C_e)$ to obtain a straight line.  
        - The slope is $\\frac{RT}{b_T}$, and the intercept is $\\frac{RT}{b_T} \\ln(K_T)$.  

        ### Step 2: Calculate $q_e$
        - For each equilibrium concentration ($C_e$), calculate the amount of adsorbed material ($q_e$):  
        $$
        q_e = \\frac{RT}{b_T} \\ln(K_T \\cdot C_e)
        $$  

        ### Units and Results
        - $q_e$ is expressed in **mg/g**, representing the amount of adsorbate bound per gram of adsorbent.  
        - $C_e$ is expressed in **mg/L**, representing the equilibrium concentration of the adsorbate.  

        ## 6. Key Notes
        - The Temkin isotherm is most suitable for systems where **adsorbate-adsorbent interactions** significantly affect adsorption behavior.  
        - Care must be taken to use the **correct form** of the Temkin isotherm to avoid dimensional inconsistency.  

        **Reference:** [Temkin, 1930s](https://doi.org/10.1016/S0926-860X(00)00832-4)
        </div>
        """, unsafe_allow_html=True)
