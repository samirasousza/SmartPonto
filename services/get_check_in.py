import streamlit as st

def get_check_in(card_id, date):
    try:
        check_in, check_out, excused, excuse = st.contract.functions.consultarPonto(card_id, date).call()
        return check_in, check_out, excused, excuse
    
    except Exception as e:
        st.error(f"Erro ao achar : {str(e)}")
        print(f"Erro ao processar consulta: {str(e)}")
        return False, False, False, False