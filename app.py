import streamlit as st
from components.login_page import LoginPage
from components.time_tracking_page import TimeTrackingPage

class App:

    @staticmethod
    def run():
        st.set_page_config(
            page_title="Marcador de ponto",
            page_icon="🔒",
            layout="wide"
        )

        # Inicializa o estado da página, se necessário
        if "page" not in st.session_state:
            st.session_state.page = "login_page"

        # Lógica de navegação entre páginas
        if st.session_state.page == "login_page":
            LoginPage().render()  # Chama a função show() do login.py
        elif st.session_state.page == "time_tracking_page":
            TimeTrackingPage().render()

        # login_page = LoginPage().render()

App.run()