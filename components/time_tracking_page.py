import streamlit as st
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
import time

class TimeTrackingPage():
    def __init__(self):
        pass

    @staticmethod
    def render():
        # Atualiza a página a cada 1 segundo
        st_autorefresh(interval=1000, key="refresh_timer")

        st.title("Registro de Ponto")

        # Hora atual
        st.markdown("### Data e Hora Atual:")
        hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        st.info(hora_atual)

        # Espaço entre botões de entrada e saída
        col1, col2 = st.columns(2)

        # Inicializa lista de registros se não existir
        if "ponto_registrado" not in st.session_state:
            st.session_state.ponto_registrado = []

        with col1:
            if st.button("🟢 Registrar Entrada", use_container_width=True):
                timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                st.session_state.ponto_registrado.append({"tipo": "entrada", "hora": timestamp})
                st.success(f"Entrada registrada em {timestamp}")

        with col2:
            if st.button("🔴 Registrar Saída", use_container_width=True):
                timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                st.session_state.ponto_registrado.append({"tipo": "saida", "hora": timestamp})
                st.success(f"Saída registrada em {timestamp}")

        st.markdown("---")
        st.subheader("Outras opções:")

        # Coluna vertical de botões
        if st.button("📝 Justificar Falta", use_container_width=True):
            st.session_state.page = "justify_page"

        if st.button("📋 Ver Pontos Marcados", use_container_width=True):
            st.session_state.page = "history_page"

        if st.button("🔙 Sair", use_container_width=True):
            st.session_state.page = "login_page"

        # with st.form("clock_form"):
        #     entrada = st.time_input("Horário de entrada")
        #     saida = st.time_input("Horário de saída")
        #     confirmar = st.form_submit_button("Registrar", use_container_width=True)

        # if confirmar:
        #     st.success(f"Ponto registrado: {entrada} - {saida}")