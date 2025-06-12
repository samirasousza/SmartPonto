from services.get_check_in import get_check_in
import streamlit as st
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
from datetime import date
import time
from services.check_in import check_in
from services.check_out import check_out


class TimeTrackingPage():
    def __init__(self):
        pass

    @staticmethod
    def render():
        # Atualiza a página a cada 1 segundo
        #st_autorefresh(interval=1000, key="refresh_timer")

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
                
                check_in(st.session_state.card_id, str(datetime.now().timestamp()), str(datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()))

                # Criando dados ficticios
                #check_in("1111", str(datetime.today().replace(day= 7,hour=9, minute=7, second=30, microsecond=0).timestamp()), str(datetime.today().replace(day= 7, hour=0, minute=0, second=0, microsecond=0).timestamp()))

                print(f"Id {st.session_state.card_id} data {str(datetime.now().timestamp())} dia {str(datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).timestamp())}")
                st.session_state.entrada_registrada = True
                st.session_state.saida_registrada = False
                # st.success(f"Entrada registrada em {timestamp}")

            # Mostrar hora da ultima entrada
            if st.session_state.entrada_registrada:
                ultima_entrada = [p for p in st.session_state.ponto_registrado if p["tipo"] == "entrada"][-1]
                st.markdown(f"🕒 Última entrada: `{ultima_entrada['hora']}`")

        with col2:
            if st.button("🔴 Registrar Saída", use_container_width=True):
                timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                st.session_state.ponto_registrado.append({"tipo": "saida", "hora": timestamp})
                check_out(st.session_state.card_id, str(datetime.now().timestamp()), str(datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()))
                
                # Criando dados ficticios
                #check_out("1111", str(datetime.today().replace(day= 7,hour=18, minute=40, second=42, microsecond=0).timestamp()), str(datetime.today().replace(day= 7, hour=0, minute=0, second=0, microsecond=0).timestamp()))

                st.success(f"Saída registrada em {timestamp}")

        st.markdown("---")
        st.subheader("Outras opções:")

        # Coluna vertical de botões
        if st.button("📝 Justificar Falta", use_container_width=True):

            st.session_state.page = "justify_page"

        if st.button("📋 Ver Pontos Marcados", use_container_width=True):
            st.session_state.page = "history_page"
            check_in_time, check_out_time, excused, excuse = get_check_in(st.session_state.card_id, str(datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()))
            print(str(date.today()))
            print(str(datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()))
            print("aaaaa")
            print(check_in_time)
            print(check_out_time)
            print(excused)
            print(excuse)

        if st.button("🔙 Sair", use_container_width=True):
            st.session_state.page = "login_page"

        # with st.form("clock_form"):
        #     entrada = st.time_input("Horário de entrada")
        #     saida = st.time_input("Horário de saída")
        #     confirmar = st.form_submit_button("Registrar", use_container_width=True)

        # if confirmar:
        #     st.success(f"Ponto registrado: {entrada} - {saida}")