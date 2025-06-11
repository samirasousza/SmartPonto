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

        # Inicializa os estados
        if "ponto_registrado" not in st.session_state:
            st.session_state.ponto_registrado = []

        if "entrada_registrada" not in st.session_state:
            st.session_state.entrada_registrada = False

        if "saida_registrada" not in st.session_state:
            st.session_state.saida_registrada = False

        col1, col2 = st.columns(2)

        with col1:
            # Desativa o botão se entrada já foi registrada e saída ainda não
            entrada_btn_disabled = st.session_state.entrada_registrada and not st.session_state.saida_registrada

            if st.button("🟢 Registrar Entrada", use_container_width=True, disabled=entrada_btn_disabled):
                timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                st.session_state.ponto_registrado.append({"tipo": "entrada", "hora": timestamp})
                st.session_state.entrada_registrada = True
                st.session_state.saida_registrada = False
                # st.success(f"Entrada registrada em {timestamp}")

            # Mostrar hora da última entrada
            if st.session_state.entrada_registrada:
                ultima_entrada = [p for p in st.session_state.ponto_registrado if p["tipo"] == "entrada"][-1]
                st.markdown(f"🕒 Última entrada: `{ultima_entrada['hora']}`")

        with col2:
            if st.button("🔴 Registrar Saída", use_container_width=True):
                timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                st.session_state.ponto_registrado.append({"tipo": "saida", "hora": timestamp})
                st.session_state.saida_registrada = True
                st.session_state.entrada_registrada = False  # Libera o botão de entrada novamente
                # st.success(f"Saída registrada em {timestamp}")

                # Mostrar hora da última saída
            if st.session_state.saida_registrada:
                ultima_saida = [p for p in st.session_state.ponto_registrado if p["tipo"] == "saida"][-1]
                st.markdown(f"🕒 Última saída: `{ultima_saida['hora']}`")

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