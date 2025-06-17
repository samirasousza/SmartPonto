from services.get_check_in import get_check_in
import streamlit as st
from datetime import datetime, timedelta
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

    #def_get_hours():
    def total_income(income_value, work_hours, total_hours):
        income_per_hour = income_value/ (30 * work_hours)
        return total_hours * income_per_hour
        
    
    def dias_do_mes(ano, mes):
        # Encontrar o primeiro dia do mês
        primeiro_dia = datetime(ano, mes, 1, 0, 0, 0)
        
        # Encontrar o último dia do mês
        if mes == 12:
            proximo_mes = datetime(ano + 1, 1, 1, 0, 0, 0)
        else:
            proximo_mes = datetime(ano, mes + 1, 1, 0, 0, 0)
        
        ultimo_dia = proximo_mes - timedelta(days=1)

        # Criar a lista de dias
        dias = [primeiro_dia + timedelta(days=i) for i in range((ultimo_dia - primeiro_dia).days + 1)]
        print(dias)

        dias =[dia.timestamp() for dia in dias]

        print("aqui estao")
        print(dias)
        
        return dias
    
    @staticmethod
    def render():
        st.title("📋 Histórico de Pontos")
        checks=0
        with st.expander('Ano e Mês', expanded=True):
            this_year = datetime.now().year
            this_month = datetime.now().month
            report_year = st.selectbox("", range(this_year, this_year - 2, -1))
            month_abbr = list(months)
            print(month_abbr)
            report_month_str = st.radio("", month_abbr, index=this_month - 1, horizontal=True)
            report_month = month_abbr.index(report_month_str) + 1
            checks=1

        # Exemplo: Todos os dias de junho de 2025
        if st.button("Buscar pontos", use_container_width=True):
            print(report_year)
            print(report_month)
            dias_mes = HistoryPage.dias_do_mes(int(report_year), int(months[report_month_str]))
            checks=0
            st.markdown(f"Pontos para o mês de {report_month_str}")
            for dia in dias_mes:
                check_in, check_out, excused, excuse = get_check_in(st.session_state.card_id, str(dia))
                print("O que foi retornado")
                print(check_in)
                print(check_out)
                print(excused)
                print(excuse)

                if check_in != "":
                    checks = 1
                    st.markdown(f"""
                    **Checkin:** `{datetime.fromtimestamp(float(check_in)).strftime('%Y-%m-%d %H:%M:%S')}`  
                    **Checkout:** `{datetime.fromtimestamp(float(check_out)).strftime('%Y-%m-%d %H:%M:%S')}`  
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
                dias_mes = HistoryPage.dias_do_mes(int(report_year), int(months[report_month_str]))
                print(f"Tamanho mes {len(dias_mes)}")
                if len(dias_mes)!=0:
                    checks=0
                    st.markdown(f"Salário para o mês de {report_month_str}")
                    for dia in dias_mes:
                        check_in, check_out, excused, excuse = get_check_in(st.session_state.card_id, str(dia))
                        
                        print("O que foi retornado")
                        print(check_in)
                        print(check_out)
                        print(excused)
                        print(excuse)
                        if check_in != "":
                            if excused == True:
                                total_hours += work_hours
                            else:
                                hours_dif=datetime.fromtimestamp(float(check_out)) - datetime.fromtimestamp(float(check_in))
                                total_hours += hours_dif.total_seconds()/ (60 * 60)
                            
                    
                    final_income = HistoryPage.total_income(income_value, work_hours, total_hours)
                
                    st.markdown(f"Total previsto para receber: {final_income:.2f}")
                    st.markdown(f"Total de horas trabalhadas: {total_hours:.2f}")

                else:
                    st.markdown(f"Houve um problema ao calcular o salário no mês de {report_month_str}")

            else:
                st.error("Preencha os campos")
 
           

        st.markdown("---")
        if st.button("🔙 Voltar", use_container_width=True):
            st.session_state.page = "time_tracking_page"

    

