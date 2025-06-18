import streamlit as st
from components.time_tracking_page import TimeTrackingPage

class LoginPage():
    def __init__(self):
        pass

    @staticmethod
    def render():
        st.title("Marcar ponto")

        st.header("Digite sua Matrícula")

        with st.form("login_form"):
            registration = st.text_input("", key="registration")

            submitted = st.form_submit_button("Confirmar", use_container_width=True)

        if submitted: 
             # Aqui você pode adicionar verificação real da matrícula
            if registration.strip() != "":
                st.session_state.page = "time_tracking_page"
                st.session_state.card_id = registration
            else:
                st.error("Matrícula não registrada")