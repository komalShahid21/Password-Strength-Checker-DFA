import streamlit as st

class PasswordDFA:
    def __init__(self):
        self.start_state = (False, False, False, 0)  # (has_lower, has_upper, has_digit, length)
        self.dead_state = "DEAD"

    def transition(self, state, char):
        if state == self.dead_state:
            return self.dead_state

        has_lower, has_upper, has_digit, length = state

        # cannot start with digit
        if length == 0 and char.isdigit():
            return self.dead_state

        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True

        length += 1
        return (has_lower, has_upper, has_digit, length)

    def is_accepting(self, state):
        if state == self.dead_state:
            return False
        has_lower, has_upper, has_digit, length = state
        return has_lower and has_upper and has_digit and length >= 6

    def validate_password(self, password):
        state = self.start_state
        for char in password:
            state = self.transition(state, char)
        return self.is_accepting(state)


# -------------------------
# Streamlit UI
# -------------------------
st.set_page_config(page_title="isyourpasswordstrongenough", page_icon="🔐")

st.title("🔐 Password Strength Checker")

st.write("""
**Rules:**  
• Must not start with a digit  
• At least 1 lowercase letter  
• At least 1 uppercase letter  
• At least 1 digit  
• Minimum length 6
""")

# Real-time input using session_state
if "pw" not in st.session_state:
    st.session_state.pw = ""

def on_change():
    st.session_state.pw = st.session_state.input_pw

st.text_input("Enter password:", type="password", key="input_pw", on_change=on_change)
pw = st.session_state.pw

# show checklist
st.write("### Rule checklist")
st.write(f"- Starts with non-digit: {'✔' if (not pw or (pw and not pw[0].isdigit())) else '❌'}")
st.write(f"- Has lowercase: {'✔' if any(c.islower() for c in pw) else '❌'}")
st.write(f"- Has uppercase: {'✔' if any(c.isupper() for c in pw) else '❌'}")
st.write(f"- Has digit: {'✔' if any(c.isdigit() for c in pw) else '❌'}")
st.write(f"- Length >= 6: {'✔' if len(pw) >= 6 else '❌'}")

dfa = PasswordDFA()
ok = dfa.validate_password(pw)

st.write("---")
if pw:
    if ok:
        st.success("✔ Password is VALID")
    else:
        st.error("❌ Password is INVALID")

