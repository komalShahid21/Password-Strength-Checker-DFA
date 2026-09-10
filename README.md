# 🔐 Password Strength Checker (DFA)

## 📌 Description
A web application built with Streamlit that validates password strength based on formal language theory (Theory of Automata). It uses a Deterministic Finite Automaton (DFA) to validate rules in real-time.

## 🛠️ Technologies Used
*   Python
*   Streamlit (Web Framework)
*   Theory of Automata (DFA Logic)

## ✨ Key Features
*   **DFA Implementation:** Passwords are validated using state transitions rather than simple regex, demonstrating strong theoretical CS knowledge.
*   **Real-time Feedback:** Interactive checklist showing which rules are passed/failed as the user types.
*   **Strict Rules:** Requires lowercase, uppercase, digit, minimum length of 6, and cannot start with a digit.
*   **Clean UI:** Simple and intuitive Streamlit interface.

## 🚀 How to Run
1. Clone this repository.
2. Install Streamlit: `pip install streamlit`
3. Run the app: `streamlit run "TOA (IsYourPasswordStrongEnough).py"`
