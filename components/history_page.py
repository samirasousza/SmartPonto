import streamlit as st

class HistoryPage():
    def __init__(self):
        pass

    @staticmethod
    def render():
        st.title("📋 Histórico de Pontos")

        if "ponto_registrado" not in st.session_state or not st.session_state.ponto_registrado:
            st.warning("Nenhum ponto registrado ainda.")
        else:
            for i, registro in enumerate(st.session_state.ponto_registrado[::-1], 1):
                tipo = "Entrada" if registro["tipo"] == "entrada" else "Saída"
                hora = registro["hora"]
                st.markdown(f"**{i}. {tipo}** - {hora}")

        st.markdown("---")
        if st.button("🔙 Voltar", use_container_width=True):
            st.session_state.page = "time_tracking_page"
