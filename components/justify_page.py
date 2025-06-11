import streamlit as st
from datetime import datetime

class JustifyPage():
    def __init__(self):
        pass

    @staticmethod
    def render():
        st.title("📝 Justificar Falta")

        st.markdown("Preencha o motivo da ausência:")

        if "justificativas" not in st.session_state:
            st.session_state.justificativas = []

        with st.form("justificativa_form"):
            data = st.date_input("Data da falta")
            motivo = st.text_area("Motivo da ausência")
            enviar = st.form_submit_button("✅ Enviar Justificativa")
            cancelar = st.form_submit_button("❌ Cancelar")

            if enviar:
                justificativa = {
                    "data": data.strftime("%d/%m/%Y"),
                    "motivo": motivo
                }
                st.session_state.justificativas.append(justificativa)
                st.success("Justificativa registrada com sucesso!")
                st.session_state.page = "time_tracking_page"

            elif cancelar:
                st.session_state.page = "time_tracking_page"
