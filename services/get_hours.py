import streamlit as st

def get_hours(card_id, date):
    try:
        check_in, check_out = st.contract.functions.getHours(card_id, date).call()
        print(f"pegarhoras {check_in} eo {check_out}")
        return check_in, check_out
    
    except Exception as e:
        st.error(f"Erro ao achar : {str(e)}")
        print(f"Erro ao processar consulta: {str(e)}")
        return False, False