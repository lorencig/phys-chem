import streamlit as st
import importlib

# Define available pages and corresponding module names
PAGES = {
    "Learning Objectives": "learning_objectives",
    "Theory": "theory",
    "Simulation": "simulation",
    "Model Recommendation": "model_recommendation", 
    #"Data Analysis": "data_analysis",
    #"Case Studies": "case_studies",
    "Quiz": "quiz"
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Dynamically import the module and run its app() function
module_name = PAGES[selection]
module = importlib.import_module(module_name)
module.app()