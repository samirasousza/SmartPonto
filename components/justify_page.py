from services.excuse_check_in import excuse_check_in
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
                excuse_check_in(st.session_state.card_id, str(datetime.now().timestamp()), str(datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()), motivo)
                
                # Criando uma falta com justificativa
                #excuse_check_in("1111", str(datetime.today().replace(day= 8,hour=9, minute=20, second=32, microsecond=0).timestamp()), str(datetime.today().replace(day=8, hour=0, minute=0, second=0, microsecond=0).timestamp()), motivo)

                st.session_state.justificativas.append(justificativa)
                st.success("Justificativa registrada com sucesso!")
                st.session_state.page = "time_tracking_page"

            elif cancelar:
                st.session_state.page = "time_tracking_page"
