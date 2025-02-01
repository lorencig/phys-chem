import streamlit as st

def app():
    st.title("Theory")
    st.markdown("Select a model from the dropdown to view its theoretical background, key assumptions, and a link to the original publication.")
    model_choice = st.selectbox("Select Model", ["Langmuir adsorption model", "BET theory", "Freundlich Equation", "Temkin Isotherm"])
#"Dubinin-Radushkevich (D-R) Isotherm", "Sips Isotherm", "Redlich-Peterson Isotherm"
    if model_choice == "Langmuir adsorption model":
        st.markdown("""
        <div style="text-align: justify;">
                    
        # Langmuir adsorption model

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

        For **multilayer adsorption**, the modified Langmuir equation is:  
        $$
        Y = \\sum_{i=1}^{3} \\left( \\sum_{j=1}^{3} a_{j,i} T_j \\right) \\cdot \\frac{\\alpha_i \\cdot p}{1 + \\alpha_i \\cdot p}
        $$  
        Where:  
        - $Y$: Total amount adsorbed.  
        - $a_{j,i}$: Coefficients related to neighboring sites.  
        - $\\alpha_i$: Adsorption constant for layer $i$.  

        ## 5. Principles/Assumptions
        1. **Homogeneous Surface**: All adsorption sites are energetically equivalent.  
        2. **Monolayer Adsorption**: Each site can hold only one molecule.  
        3. **No Interactions**: Adsorbed molecules do not interact with each other.  
        4. **Reversible Process**: Adsorption and desorption occur simultaneously.  
        5. **Ideal Behavior**: The adsorbate behaves as an ideal gas or solution.  

        ## 6. Limitations
        - **Homogeneity Assumption**: Real surfaces are often heterogeneous, with sites of varying energies.  
        - **No Multilayer Adsorption**: The basic Langmuir model does not account for adsorption beyond a monolayer.  
        - **No Interactions**: The model ignores interactions between adsorbed molecules.  
        - **High-Pressure Failure**: At high pressures, the model fails to predict saturation accurately.  

        ## 7. Explanation
        The Langmuir equation describes adsorption as a dynamic equilibrium between the rate of adsorption and desorption. At low pressures, the fraction of occupied sites ($\\theta$) increases linearly with pressure. As pressure increases, $\\theta$ approaches 1, indicating monolayer coverage. The model is widely used due to its simplicity and ability to fit experimental data for many systems.  

        ### Key Notes
        - The Langmuir model is most suitable for **monolayer adsorption** on **homogeneous surfaces**.  
        - It is often compared to the **Freundlich model**, which is empirical and better suited for heterogeneous surfaces.  
        - The linearized form of the Langmuir equation is used to determine the parameters $K_a$ and $\\theta_{max}$:  
        $$
        \\frac{p}{q} = \\frac{1}{K_a \\cdot q_{max}} + \\frac{p}{q_{max}}
        $$  
        Where $q$ is the amount adsorbed, and $q_{max}$ is the maximum adsorption capacity.  

        ### Limitations in Real-World Applications
        - **Surface Heterogeneity**: Real surfaces often have sites with varying adsorption energies.  
        - **Adsorbate Interactions**: Interactions between adsorbed molecules can significantly affect adsorption behavior.  
        - **High-Pressure Behavior**: The model fails to predict adsorption at high pressures or concentrations.  

        ### Extensions and Modifications
        - **BET Model**: Extends the Langmuir model to account for multilayer adsorption.  
        - **Temkin Isotherm**: Incorporates adsorbate-adsorbate interactions.  
        - **Freundlich Isotherm**: Empirical model for heterogeneous surfaces.  
        
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
        - $P$: Equilibrium pressure of the adsorbate gas.  
        - $P_0$: Saturation pressure of the adsorbate gas.  
        - $V$: Volume of gas adsorbed at pressure $P$.  
        - $V_m$: Volume of gas required to form a **monolayer** on the surface.  
        - $C$: BET constant related to the heat of adsorption.  

        The linearized form of the BET equation is:  
        $$
        \\frac{P}{V(P_0 - P)} = \\frac{1}{V_m \\cdot C} + \\frac{C - 1}{V_m \\cdot C} \\cdot \\frac{P}{P_0}
        $$  

        ## 5. Principles/Assumptions
        1. **Multilayer Adsorption**: Gas molecules adsorb in multiple layers on the surface.  
        2. **No Interactions**: Adsorbed molecules in one layer do not interact with those in other layers.  
        3. **First Layer Energy**: The heat of adsorption for the first layer ($E_1$) is higher than for subsequent layers ($E_L$), which are assumed to have the same energy as the heat of liquefaction.  
        4. **Infinite Layers**: Adsorption can theoretically occur in an infinite number of layers.  
        5. **Equilibrium**: Adsorption and desorption rates are in equilibrium for each layer.  

        ## 6. Limitations
        - **Applicability**: The BET equation is valid only in the relative pressure range of $0.05 < P/P_0 < 0.35$.  
        - **Surface Heterogeneity**: The theory assumes a homogeneous surface, which may not be true for real materials.  
        - **Micropores**: The BET method may overestimate surface area for materials with **micropores** due to enhanced adsorption in small pores.  
        - **Negative C Values**: In some cases, the BET constant $C$ can be negative, indicating invalid assumptions.  

        ## 7. Explanation
        The BET theory is based on the concept of **multilayer adsorption**, where gas molecules form layers on a solid surface. The first layer has a higher adsorption energy due to direct interaction with the surface, while subsequent layers have energies similar to the heat of liquefaction. By measuring the volume of gas adsorbed at different pressures, the **monolayer volume** ($V_m$) can be determined, which is then used to calculate the **specific surface area** of the material.  

        ### Key Steps in BET Analysis:
        1. **Gas Adsorption**: Measure the volume of gas (usually nitrogen at 77 K) adsorbed at various pressures.  
        2. **BET Plot**: Plot $\\frac{P}{V(P_0 - P)}$ vs. $\\frac{P}{P_0}$ to obtain a linear relationship.  
        3. **Monolayer Volume**: Determine $V_m$ from the slope and intercept of the BET plot.  
        4. **Surface Area Calculation**: Use $V_m$ to calculate the specific surface area:  
        $$
        S = \\frac{V_m \\cdot N_A \\cdot \\sigma}{M}
        $$  
        Where:  
        - $N_A$: Avogadro's number.  
        - $\\sigma$: Cross-sectional area of the adsorbate molecule.  
        - $M$: Molar volume of the adsorbate gas.  

        ### Applications of BET Theory:
        - **Catalysis**: Determining the surface area of catalysts to optimize reaction efficiency.  
        - **Pharmaceuticals**: Analyzing the surface area of powders to ensure proper dissolution and bioavailability.  
        - **Batteries**: Characterizing electrode materials to improve performance.  
        - **Activated Carbon**: Measuring the surface area of porous materials for adsorption applications.  

        ### Modified Versions:
        - **t-Plot and αs-Plot**: Used to analyze microporous materials and distinguish between monolayer and multilayer adsorption.  
        - **NLDFT (Non-Local Density Functional Theory)**: Provides more accurate pore size distribution for micro- and mesoporous materials.  

        ### Key Notes:
        - The BET method is most suitable for **nonporous** and **mesoporous** materials.  
        - For **microporous materials**, additional methods like **CO₂ adsorption** or **NLDFT** are recommended.  
        - The BET equation is widely used due to its simplicity, but care must be taken to ensure the validity of the assumptions.  

        ### Limitations in Real-World Applications:
        - **Micropore Overestimation**: The BET method may overestimate surface area for materials with micropores.  
        - **Pressure Range**: The theory is valid only in a limited pressure range ($0.05 < P/P_0 < 0.35$).  
        - **Surface Heterogeneity**: Real surfaces often have sites with varying adsorption energies, which the BET model does not account for.  

        ### Extensions and Modifications:
        - **BJH Method**: Used for pore size distribution analysis in mesoporous materials.  
        - **DFT Methods**: Provide more accurate surface area and pore size distributions for complex materials.  
                    
        **Reference:** [Stephen Brunauer, P. H. Emmett, and Edward Teller, 1938](https://pubs.acs.org/doi/10.1021/ja01269a023)     
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
        - The Freundlich equation or Freundlich adsorption isotherm is widely used to describe **adsorption equilibrium data** in environmental chemistry, particularly for **gas-phase adsorption**.  
        - It is applied to model **heterogeneous adsorption surfaces** with varying adsorption energies.  

        ## 3. Short Summary
        The Freundlich equation is an **empirical model** that describes the relationship between the amount of adsorbate bound to an adsorbent and the equilibrium concentration (or pressure) of the adsorbate. It assumes a **heterogeneous surface** with multiple adsorption sites of different energies and is commonly used for low to moderate adsorbate concentrations.  

        ## 4. Formula
        The Freundlich equation is expressed as:  
        $$
        q = K_d \\cdot C^{1/n}
        $$  
        Where:  
        - $q$: Amount of adsorbate bound per unit weight of adsorbent (mg/kg)  
        - $C$: Equilibrium concentration of adsorbate in the fluid phase (mg/L)  
        - $K_d$: Distribution coefficient (L/kg)  
        - $n$: Correction factor (dimensionless, typically < 1)  

        The linearized form is:  
        $$
        \\log q = \\frac{1}{n} \\log C + \\log K_d
        $$  

        ## 5. Principles/Assumptions
        - The adsorbent surface is **heterogeneous**, with multiple adsorption sites of varying energies.  
        - Adsorption occurs in **multilayers** rather than a monolayer.  
        - The model assumes **no saturation** of adsorption capacity, meaning adsorption increases continuously with adsorbate concentration or pressure.  

        ## 6. Limitations
        - **No adsorption maximum**: The equation does not predict saturation at high adsorbate concentrations or pressures.  
        - **Empirical nature**: The model lacks a theoretical basis, making it less reliable for mechanistic interpretations.  
        - **Not applicable at high pressures**: The assumption of continuous adsorption fails at high pressures or concentrations.  
        - **Single retention process**: The model assumes only one type of adsorption mechanism is occurring.  

        ## 7. Explanation
        The Freundlich equation is used to describe adsorption behavior on surfaces with varying adsorption energies. At low adsorbate concentrations, adsorption increases significantly with concentration. However, the model fails to account for saturation at high concentrations or pressures, limiting its applicability. Despite its empirical nature, it remains widely used due to its simplicity and ability to fit experimental data for heterogeneous surfaces.  

        ### Key Notes
        - The Freundlich equation is most suitable for **low to moderate concentrations** and **heterogeneous surfaces**.  
        - It is often compared to the **Langmuir model**, which assumes a homogeneous surface and monolayer adsorption.    
        - The linearized form of the equation ($\\log q$ vs. $\\log C$) is used to determine the parameters $K_d$ and $n$.
        
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
        The Temkin isotherm model considers the effect of **indirect adsorbate-adsorbent interactions** on the adsorption process. It assumes that the heat of adsorption decreases linearly with surface coverage and is characterized by a **uniform distribution of binding energies** up to a maximum binding energy. The model is widely used but has limitations, including dimensional inconsistency and the inability to fit Type I isotherms accurately.  

        ## 4. Formula
        The Temkin isotherm is expressed as:  
        $$
        q_e = \\frac{RT}{b_T} \\ln(K_T \\cdot C_e)
        $$  
        Where:  
        - $q_e$: Amount of adsorbate adsorbed at equilibrium (mg/g).  
        - $C_e$: Equilibrium concentration of the adsorbate in solution (mg/L).  
        - $K_T$: Equilibrium binding constant (L/mol) corresponding to the maximum binding energy.  
        - $b_T$: Heat of adsorption parameter (J/mol).  
        - $R$: Universal gas constant (8.314 J/K/mol).  
        - $T$: Temperature (K).  

        The linearized form of the Temkin isotherm is:  
        $$
        q_e = \\frac{RT}{b_T} \\ln(K_T) + \\frac{RT}{b_T} \\ln(C_e)
        $$  
        A plot of $q_e$ vs. $\\ln(C_e)$ yields a straight line with:  
        - **Slope**: $\\frac{RT}{b_T}$.  
        - **Intercept**: $\\frac{RT}{b_T} \\ln(K_T)$.  

        ## 5. Principles/Assumptions
        1. **Linear Heat of Adsorption**: The heat of adsorption decreases linearly with increasing surface coverage.  
        2. **Uniform Binding Energies**: Adsorption is characterized by a uniform distribution of binding energies up to a maximum value.  
        3. **Indirect Interactions**: The model accounts for indirect adsorbate-adsorbent interactions.  
        4. **No Saturation Limit**: The Temkin isotherm does not predict a finite saturation limit at high concentrations.  

        ## 6. Limitations
        - **Dimensional Inconsistency**: The commonly used form of the Temkin isotherm suffers from dimensional inconsistency.  
        - **No Henry’s Law Limit**: The model does not approach a linear isotherm at low concentrations.  
        - **No Saturation Limit**: It cannot describe adsorption data with a saturation plateau.  

        ## 7. Explanation
        The Temkin isotherm is based on the assumption that the heat of adsorption decreases linearly with surface coverage due to adsorbate-adsorbent interactions. Unlike the Freundlich isotherm, which assumes a logarithmic decrease in adsorption heat, the Temkin model assumes a linear decrease. This makes it suitable for systems where adsorbate-adsorbent interactions significantly affect adsorption behavior.  

        ### Key Features:
        - **Heat of Adsorption**: The parameter $b_T$ represents the heat of adsorption and is expressed in J/mol.  
        - **Binding Energy Distribution**: The model assumes a uniform distribution of binding energies up to a maximum value.  
        - **Linearized Form**: The linearized form of the Temkin isotherm is used to determine $K_T$ and $b_T$ from experimental data.  

        ### Applications:
        - **Environmental Research**: Used to model adsorption of water contaminants.  
        - **Catalysis**: Applied to study adsorption behavior in catalytic processes.  
        - **Adsorption Studies**: Used to analyze adsorption isotherms for various adsorbate-adsorbent systems.  

        ### Limitations in Real-World Applications:
        - **Type I Isotherms**: The Temkin isotherm cannot accurately fit Type I isotherms, which exhibit a saturation limit.  
        - **Low Concentrations**: The model does not approach a linear isotherm at low concentrations, limiting its applicability.  

        ### Extensions and Modifications:
        - **Modified Temkin Isotherm**: A revised form that approaches a linear isotherm at low concentrations and starts at the origin (0,0). This form outperforms the traditional Temkin isotherm in fitting adsorption data.  

        ### Key Notes:
        - The Temkin isotherm is most suitable for systems where **adsorbate-adsorbent interactions** significantly affect adsorption behavior.  
        - Care must be taken to use the **correct form** of the Temkin isotherm to avoid dimensional inconsistency and parameter confusion.  
        - The model is widely used but has limitations, particularly in fitting Type I isotherms and describing adsorption at low concentrations.  
        </div>
        """, unsafe_allow_html=True)

    elif model_choice == "Dubinin-Radushkevich (D-R) Isotherm":
        st.markdown("""
        ### Dubinin-Radushkevich (D-R) Isotherm
        **Theory:** Describes adsorption in microporous solids.  
        **Equation:** \\( Q = Q_{max}\\exp\\left[-K\\left(RT\\ln\\left(1+\\frac{1}{P}\\right)\\right)^2\\right] \\)  
        **Key Assumptions:**  
        - Adsorption in micropores  
        - No assumption of a homogeneous surface  
        **Reference:** [Dubinin & Radushkevich, 1947](https://doi.org/10.1021/ie50414a005)
        """)
    elif model_choice == "Sips Isotherm":
        st.markdown("""
        ### Sips Isotherm
        **Theory:** Combines Langmuir and Freundlich isotherms for heterogeneous systems.  
        **Equation:** \\( Q = Q_{max}\\frac{(KP)^{1/n}}{1+(KP)^{1/n}} \\)  
        **Key Assumptions:**  
        - Heterogeneous adsorption  
        **Reference:** [Sips, 1948](https://doi.org/10.1021/ie50414a005)
        """)
    elif model_choice == "Redlich-Peterson Isotherm":
        st.markdown("""
        ### Redlich-Peterson Isotherm
        **Theory:** A versatile three-parameter model that can describe both homogeneous and heterogeneous adsorption.  
        **Equation:** \\( Q = \\frac{K_RP}{1+a_RP^{\\beta}} \\)  
        **Key Assumptions:**  
        - Empirical model  
        **Reference:** [Redlich & Peterson, 1959](https://doi.org/10.1021/ie50414a005)
        """)

