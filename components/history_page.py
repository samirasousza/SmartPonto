from services.get_check_in import get_check_in
from services.get_month_days import get_month_days
import streamlit as st
from datetime import datetime

months = {
    "Janeiro" : "01",
    "Fervereiro" : "02",
    "Março" : "03",
    "Abril" : "04",
    "Maio" : "05",
    "Junho" : "06",
    "Julho" : "07",
    "Agosto" : "08",
    "Setembro" : "09",
    "Outubro" : "10",
    "Novembro" : "11",
    "Dezembro" : "12"
}

class HistoryPage():
    def __init__(self):
        pass

    def total_income(income_value, work_hours, total_hours):
        income_per_hour = income_value/ (30 * work_hours)
        return total_hours * income_per_hour
        
    
    @staticmethod
    def render():
        st.title("📋 Histórico de Pontos")
        checks=0
        with st.expander('Ano e Mês', expanded=True):
            this_year = datetime.now().year
            this_month = datetime.now().month
            report_year = st.selectbox("", range(this_year, this_year - 2, -1))
            month_abbr = list(months)
            report_month_str = st.radio("", month_abbr, index=this_month - 1, horizontal=True)
            checks=1

        # Exemplo: Todos os dias de junho de 2025
        if st.button("Buscar pontos", use_container_width=True):
            dias_mes = get_month_days(int(report_year), int(months[report_month_str]))
            checks=0
            st.markdown(f"Pontos para o mês de {report_month_str}")
            for dia in dias_mes:
                check_in, check_out, excused, excuse = get_check_in(st.session_state.card_id, str(dia))

                if check_in != "":
                    checks = 1
                    st.markdown(f"""
                    **Checkin:** `{datetime.fromtimestamp(float(check_in)).strftime('%H:%M:%S %d-%m-%Y')}`  
                    **Checkout:** `{datetime.fromtimestamp(float(check_out)).strftime('%H:%M:%S %d-%m-%Y')}`  
                    **Excuse:** `{excuse}`  
                    """)
                    st.markdown("---")

        if checks == 0:
            st.warning("Nenhum ponto registrado ainda.")

        st.header("Consultar salário do mês por horas trabalhadas")
        with st.form("login_form"):
            st.markdown("Digite seu salário")
            income_value = st.number_input("", key="income_value")
            st.markdown("Digite a quantidade de horas que você trabalha por dia")
            work_hours = st.number_input("", key="work_hours")
            submitted = st.form_submit_button("Ver valor", use_container_width=True)

        if submitted: 
             # Aqui você pode adicionar verificação real da matrícula
            if income_value !=0 and  work_hours != 0:
                total_hours=0
                dias_mes = get_month_days(int(report_year), int(months[report_month_str]))

                if len(dias_mes)!=0:
                    checks=0
                    st.markdown(f"Salário para o mês de {report_month_str}")
                    for dia in dias_mes:
                        check_in, check_out, excused, excuse = get_check_in(st.session_state.card_id, str(dia))
                        
                        if check_in != "":
                            if excused == True:
                                total_hours += work_hours
                            else:
                                hours_dif=datetime.fromtimestamp(float(check_out)) - datetime.fromtimestamp(float(check_in))
                                total_hours += hours_dif.total_seconds()/ (60 * 60)
                            
                    
                    final_income = HistoryPage.total_income(income_value, work_hours, total_hours)
                
                    st.markdown(f"Total previsto para receber: R$ {final_income:.2f}")
                    st.markdown(f"Total de horas trabalhadas: R$ {total_hours:.2f}")

                else:
                    st.markdown(f"Houve um problema ao calcular o salário no mês de {report_month_str}")

            else:
                st.error("Preencha os campos")
 
           

        st.markdown("---")
        if st.button("🔙 Voltar", use_container_width=True):
            st.session_state.page = "time_tracking_page"

    

