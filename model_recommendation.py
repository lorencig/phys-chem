import streamlit as st

def recommend_model(adsorbent_nature, adsorption_type, interactions):
    # Simplified recommendation logic considering only Langmuir, BET, Temkin, and Freundlich isotherms.
    if adsorbent_nature == "Homogeneous":
        if adsorption_type == "Monolayer":
            return "Langmuir Isotherm", "Recommended because the surface is uniform and the adsorption forms a single layer."
        elif adsorption_type == "Multilayer":
            return "BET Isotherm", "Recommended because the uniform surface supports multilayer adsorption."
    elif adsorbent_nature == "Heterogeneous":
        if adsorption_type == "Monolayer":
            if interactions == "Yes":
                return "Temkin Isotherm", "Recommended because it accounts for interactions on heterogeneous surfaces."
            else:
                return "Freundlich Isotherm", "Recommended due to the variability in adsorption sites on heterogeneous surfaces."
        elif adsorption_type == "Multilayer":
            return "BET Isotherm", "Recommended for multilayer adsorption on heterogeneous surfaces."
    
    # Fallback: If system conditions are broad, suggest Langmuir as a default.
    return "Langmuir Isotherm", "Recommended as a default model for various adsorption systems."

def app():
    st.title("Model Recommendation")
    st.markdown("""
    **Instructions:**  
    Choose the nature of your adsorbent, the type of adsorption, and specify if adsorbate–adsorbate interactions are present.  
    The system will recommend the most appropriate adsorption model along with a brief summary and justification.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        # Nature of Adsorbent
        adsorbent_nature = st.selectbox(
            "Nature of Adsorbent ", 
            ["Homogeneous", "Heterogeneous"],
            help="Homogeneous: Uniform surface with identical adsorption sites. Heterogeneous: Non-uniform surface with varying adsorption sites."
        )
        
        # Type of Adsorption
        adsorption_type = st.selectbox(
            "Type of Adsorption ", 
            ["Monolayer", "Multilayer"],
            help="Monolayer: Adsorption occurs in a single layer. Multilayer: Adsorption occurs in multiple layers."
        )
    
    with col2:
        # Adsorbate–Adsorbate Interactions (No/Yes selection)
        interactions = st.selectbox(
            "Adsorbate–Adsorbate Interactions Present?",
            ["No", "Yes"],
            help="Select 'Yes' if there are interactions between adsorbed molecules on the surface."
        )
    
    if st.button("Recommend Model"):
        model, explanation = recommend_model(adsorbent_nature, adsorption_type, interactions)
        st.success(f"**Recommended Model:** {model}")
        st.info(f"**Justification:** {explanation}")
        
        # Provide a summary and a link to the original publication.
        if model == "Langmuir Isotherm":
            summary = "The Langmuir model assumes monolayer adsorption on a surface with a finite number of identical sites and no interactions between adsorbed molecules."
        elif model == "BET Isotherm":
            summary = "The BET model extends the Langmuir theory to multilayer adsorption and is well suited for porous materials."
        elif model == "Freundlich Isotherm":
            summary = "The Freundlich model is an empirical model that describes adsorption on heterogeneous surfaces."
        elif model == "Temkin Isotherm":
            summary = "The Temkin model considers adsorbate–adsorbate interactions on heterogeneous surfaces and assumes a linear decrease in adsorption heat."
        
        st.markdown(f"**Model Summary:** {summary}\n\n")

if __name__ == "__main__":
    app()