from datetime import datetime
import streamlit as st

def check_in(cardid, timestamp, date):
    try:
        nonce = st.w3.eth.get_transaction_count(st.sender_address)
        # Acessa a função store do contrato inteligente e prepara uma chamada com o parâmetro num (o número que o usuário digitou).
        # Constrói a transação em formato de dicionário Python, com os dados necessários para enviá-la à rede Ethereum.
        tx = st.contract.functions.checkIn(cardid, timestamp, date).build_transaction({
            'chainId': 11155111,  # Sepolia
            'gas': 200000, #Quantidade máxima de gás que a transação pode consumir. Fixado em 200000 unidades, o que é mais do que suficiente para essa função simples.
            'gasPrice': st.w3.to_wei('10', 'gwei'), #Define o preço do gás a ser pago por unidade. Convertido de 10 gwei para wei (menor unidade do ETH) usando w3.to_wei(...).
            'nonce': nonce #Define o nonce, ou seja, o número de transações já enviadas pela conta. Garante que cada transação tenha um número único, necessário para ser aceita pela rede.
        })

        signed_tx = st.w3.eth.account.sign_transaction(tx, st.private_key)
        tx_hash = st.w3.eth.send_raw_transaction(signed_tx.raw_transaction)

        st.success(f"Entrada registrada em {datetime.fromtimestamp(float(timestamp)).strftime('%H:%M:%S %d-%m-%Y')}")
        # Espera a transação ser minerada
        receipt = st.w3.eth.wait_for_transaction_receipt(tx_hash)
        print(receipt.logs)
        
        
    except Exception as e:
        st.error(f"Erro ao enviar transação: {str(e)}")
        return False, f"Erro ao processar: {str(e)}"