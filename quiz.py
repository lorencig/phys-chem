import streamlit as st
import random

def get_quiz_questions():
    # List of 50 unique questions on Langmuir, BET, Temkin, and Freundlich isotherms
    questions = [
        {
            "question": "What does the Langmuir isotherm assume?",
            "choices": [
                "Monolayer adsorption on a homogeneous surface",
                "Multilayer adsorption on heterogeneous surfaces",
                "Random adsorption with no defined behavior",
                "Adsorption with chemical reaction"
            ],
            "correct": 0
        },
        {
            "question": "Which model is most appropriate for multilayer adsorption?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 1
        },
        {
            "question": "The Freundlich isotherm is used for:",
            "choices": [
                "Homogeneous surfaces",
                "Heterogeneous surfaces",
                "Micropore filling",
                "No adsorption"
            ],
            "correct": 1
        },
        {
            "question": "What does a negative ΔH indicate in adsorption?",
            "choices": [
                "Exothermic process",
                "Endothermic process",
                "No heat change",
                "Irreversible adsorption"
            ],
            "correct": 0
        },
        {
            "question": "A high surface area generally leads to:",
            "choices": [
                "Higher adsorption capacity",
                "Lower adsorption capacity",
                "No effect",
                "Increased desorption"
            ],
            "correct": 0
        },
        {
            "question": "Which isotherm assumes a linear decrease in adsorption heat?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 3
        },
        {
            "question": "The BET isotherm is an extension of which model?",
            "choices": [
                "Langmuir",
                "Freundlich",
                "Temkin",
                "Henry's Law"
            ],
            "correct": 0
        },
        {
            "question": "Which isotherm is empirical and describes adsorption on heterogeneous surfaces?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 2
        },
        {
            "question": "What is the primary assumption of the Langmuir isotherm?",
            "choices": [
                "All adsorption sites are equivalent",
                "Adsorption occurs in multilayers",
                "Adsorption heat decreases linearly",
                "Surface is heterogeneous"
            ],
            "correct": 0
        },
        {
            "question": "Which isotherm is suitable for describing adsorption in micropores?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 1
        },
        {
            "question": "What does the Freundlich isotherm equation describe?",
            "choices": [
                "Linear adsorption",
                "Exponential adsorption",
                "Logarithmic adsorption",
                "Power-law adsorption"
            ],
            "correct": 3
        },
        {
            "question": "Which isotherm accounts for adsorbate–adsorbate interactions?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 3
        },
        {
            "question": "What is the main limitation of the Langmuir isotherm?",
            "choices": [
                "It assumes monolayer adsorption",
                "It cannot describe heterogeneous surfaces",
                "It ignores adsorbate–adsorbate interactions",
                "All of the above"
            ],
            "correct": 3
        },
        {
            "question": "Which isotherm is best for describing adsorption at low pressures?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 0
        },
        {
            "question": "What does the BET isotherm assume about the surface?",
            "choices": [
                "It is homogeneous",
                "It is heterogeneous",
                "It has micropores",
                "It is non-porous"
            ],
            "correct": 0
        },
        {
            "question": "Which isotherm is used for describing adsorption at high pressures?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 1
        },
        {
            "question": "What does the Temkin isotherm assume about adsorption heat?",
            "choices": [
                "It is constant",
                "It decreases linearly with coverage",
                "It increases exponentially",
                "It is negligible"
            ],
            "correct": 1
        },
        {
            "question": "Which isotherm is most suitable for describing chemisorption?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 0
        },
        {
            "question": "What does the Freundlich isotherm constant 'n' represent?",
            "choices": [
                "Adsorption capacity",
                "Adsorption intensity",
                "Surface heterogeneity",
                "Heat of adsorption"
            ],
            "correct": 1
        },
        {
            "question": "Which isotherm is best for describing physical adsorption?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 1
        },
        {
            "question": "What does the Langmuir isotherm equation describe?",
            "choices": [
                "Linear adsorption",
                "Exponential adsorption",
                "Saturation adsorption",
                "Power-law adsorption"
            ],
            "correct": 2
        },
        {
            "question": "Which isotherm is used for describing adsorption on non-ideal surfaces?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 2
        },
        {
            "question": "What does the BET isotherm equation describe?",
            "choices": [
                "Monolayer adsorption",
                "Multilayer adsorption",
                "Micropore filling",
                "Chemisorption"
            ],
            "correct": 1
        },
        {
            "question": "Which isotherm assumes that adsorption sites are energetically equivalent?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 0
        },
        {
            "question": "What does the Freundlich isotherm describe about adsorption sites?",
            "choices": [
                "They are homogeneous",
                "They are heterogeneous",
                "They are non-porous",
                "They are chemically reactive"
            ],
            "correct": 1
        },
        {
            "question": "Which isotherm is best for describing adsorption at intermediate pressures?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 2
        },
        {
            "question": "What does the Temkin isotherm assume about adsorbate–adsorbate interactions?",
            "choices": [
                "They are negligible",
                "They are significant",
                "They are constant",
                "They are random"
            ],
            "correct": 1
        },
        {
            "question": "Which isotherm is best for describing adsorption on porous materials?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 1
        },
        {
            "question": "What does the Langmuir isotherm assume about adsorption sites?",
            "choices": [
                "They are finite and identical",
                "They are infinite and varied",
                "They are non-interacting",
                "They are chemically reactive"
            ],
            "correct": 0
        },
        {
            "question": "Which isotherm is best for describing adsorption at low concentrations?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 0
        },
        {
            "question": "What does the Freundlich isotherm assume about adsorption heat?",
            "choices": [
                "It is constant",
                "It varies with coverage",
                "It is negligible",
                "It is linear"
            ],
            "correct": 1
        },
        {
            "question": "Which isotherm is best for describing adsorption on non-porous materials?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 0
        },
        {
            "question": "What does the BET isotherm assume about adsorption layers?",
            "choices": [
                "They are infinite",
                "They are limited to a monolayer",
                "They are limited to multilayers",
                "They are random"
            ],
            "correct": 2
        },
        {
            "question": "Which isotherm is best for describing adsorption on surfaces with varying site energies?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 2
        },
        {
            "question": "What does the Temkin isotherm assume about adsorption sites?",
            "choices": [
                "They are identical",
                "They are energetically varied",
                "They are non-interacting",
                "They are chemically reactive"
            ],
            "correct": 1
        },
        {
            "question": "Which isotherm is best for describing adsorption at high concentrations?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 1
        },
        {
            "question": "What does the Freundlich isotherm assume about adsorption capacity?",
            "choices": [
                "It is constant",
                "It varies with concentration",
                "It is negligible",
                "It is linear"
            ],
            "correct": 1
        },
        {
            "question": "Which isotherm is best for describing adsorption on surfaces with strong adsorbate–adsorbate interactions?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 3
        },
        {
            "question": "What does the Langmuir isotherm assume about adsorbate–adsorbate interactions?",
            "choices": [
                "They are negligible",
                "They are significant",
                "They are constant",
                "They are random"
            ],
            "correct": 0
        },
        {
            "question": "Which isotherm is best for describing adsorption on surfaces with weak adsorbate–adsorbate interactions?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 0
        },
        {
            "question": "What does the BET isotherm assume about adsorption heat?",
            "choices": [
                "It is constant",
                "It varies with coverage",
                "It is negligible",
                "It is linear"
            ],
            "correct": 0
        },
        {
            "question": "Which isotherm is best for describing adsorption on surfaces with moderate adsorbate–adsorbate interactions?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 3
        },
        {
            "question": "What does the Freundlich isotherm assume about adsorption sites?",
            "choices": [
                "They are identical",
                "They are energetically varied",
                "They are non-interacting",
                "They are chemically reactive"
            ],
            "correct": 1
        },
        {
            "question": "Which isotherm is best for describing adsorption on surfaces with strong adsorbate–surface interactions?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 0
        },
        {
            "question": "What does the Temkin isotherm assume about adsorption capacity?",
            "choices": [
                "It is constant",
                "It varies with concentration",
                "It is negligible",
                "It is linear"
            ],
            "correct": 1
        },
        {
            "question": "Which isotherm is best for describing adsorption on surfaces with weak adsorbate–surface interactions?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 2
        },
        {
            "question": "What does the Langmuir isotherm assume about adsorption capacity?",
            "choices": [
                "It is constant",
                "It varies with concentration",
                "It is negligible",
                "It is linear"
            ],
            "correct": 0
        },
        {
            "question": "Which isotherm is best for describing adsorption on surfaces with moderate adsorbate–surface interactions?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 2
        },
        {
            "question": "What does the BET isotherm assume about adsorption capacity?",
            "choices": [
                "It is constant",
                "It varies with concentration",
                "It is negligible",
                "It is linear"
            ],
            "correct": 1
        },
        {
            "question": "Which isotherm is best for describing adsorption on surfaces with strong adsorbate–surface interactions?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 0
        },
        {
            "question": "What does the Freundlich isotherm assume about adsorption heat?",
            "choices": [
                "It is constant",
                "It varies with coverage",
                "It is negligible",
                "It is linear"
            ],
            "correct": 1
        },
        {
            "question": "Which isotherm is best for describing adsorption on surfaces with weak adsorbate–surface interactions?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 2
        },
        {
            "question": "What does the Temkin isotherm assume about adsorption heat?",
            "choices": [
                "It is constant",
                "It varies with coverage",
                "It is negligible",
                "It is linear"
            ],
            "correct": 1
        },
        {
            "question": "Which isotherm is best for describing adsorption on surfaces with moderate adsorbate–surface interactions?",
            "choices": [
                "Langmuir",
                "BET",
                "Freundlich",
                "Temkin"
            ],
            "correct": 2
        },
    ]
    return questions

def app():
    st.title("Quiz: Test Your Adsorption Knowledge")
    questions = get_quiz_questions()
    selected_questions = random.sample(questions, 8)
    user_answers = {}
    for idx, q in enumerate(selected_questions):
        st.markdown(f"**Question {idx+1}:** {q['question']}")
        choices = q["choices"].copy()
        random.shuffle(choices)
        correct_answer = q["choices"][q["correct"]]

        user_choice = st.radio(
            f"Select your answer for Question {idx+1}:",
            choices,
            key=f"quiz_q{idx}",
            index=0  # No default selection
        )
        user_answers[idx] = {"user_choice": user_choice, "correct_answer": correct_answer}
        st.write("---")

    if st.button("Submit Quiz"):
        score = sum(1 for ans in user_answers.values() if ans["user_choice"] == ans["correct_answer"])
        st.success(f"You scored {score} out of {len(selected_questions)}!")
        st.markdown("### Detailed Feedback")
        for idx, ans in user_answers.items():
            feedback = "Correct" if ans["user_choice"] == ans["correct_answer"] else f"Incorrect. The correct answer is: **{ans['correct_answer']}**."
            st.markdown(f"**Question {idx+1}:** {feedback}")

if __name__ == "__main__":
    app()