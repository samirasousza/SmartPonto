import streamlit as st
from components.login_page import LoginPage
from components.time_tracking_page import TimeTrackingPage
from dotenv import load_dotenv
from web3 import Web3
import os
import json

load_dotenv()

class App:

    @staticmethod
    def run():
        st.set_page_config(
            page_title="Marcador de ponto",
            page_icon="🔒",
            layout="wide"
        )

        # Inicializa o contrato, se necessário
        if 'contract' not in st.session_state:
            # Carrega variáveis do .env
            
            st.private_key = os.getenv("PRIVATE_KEY")

            # Conexão Sepolia (Infura, Alchemy, etc.)
            st.provider_url = os.getenv("PROVIDER_URL")
            st.w3 = Web3(Web3.HTTPProvider(st.provider_url))
            st.account = st.w3.eth.account.from_key(st.private_key)
            st.sender_address = st.account.address

            # Endereço do contrato ProductsOriginChain
            st.contract_address = os.getenv("CONTRACT_ADDRESS")
            st.abi = '''
[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "string",
				"name": "Mensagem",
				"type": "string"
			}
		],
		"name": "Aviso",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "string",
				"name": "cardId",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "timestamp",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "checkIn",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "checkOut",
				"type": "string"
			}
		],
		"name": "CheckEvent",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "string",
				"name": "entrada",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "sainda",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "bool",
				"name": "justificado",
				"type": "bool"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "justificativa",
				"type": "string"
			}
		],
		"name": "PontoEvent",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "bool",
				"name": "tam",
				"type": "bool"
			}
		],
		"name": "Tam",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "cardId",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "datetime",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "date",
				"type": "string"
			}
		],
		"name": "checkIn",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "cardId",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "datetime",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "date",
				"type": "string"
			}
		],
		"name": "checkOut",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "cardId",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "date",
				"type": "string"
			}
		],
		"name": "consultarPonto",
		"outputs": [
			{
				"internalType": "string",
				"name": "entrada",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "saida",
				"type": "string"
			},
			{
				"internalType": "bool",
				"name": "justificado",
				"type": "bool"
			},
			{
				"internalType": "string",
				"name": "justificativa",
				"type": "string"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "cardId",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "datetime",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "date",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "excuse",
				"type": "string"
			}
		],
		"name": "excuseCheckIn",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"name": "registros",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "exists",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "checkIn",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "checkOut",
				"type": "string"
			},
			{
				"internalType": "bool",
				"name": "excused",
				"type": "bool"
			},
			{
				"internalType": "string",
				"name": "excuse",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
                        '''


            st.session_state.contract = st.contract = st.w3.eth.contract(address=st.contract_address, abi=json.loads(st.abi))


        # Inicializa o estado da página, se necessário
        if "page" not in st.session_state:
            st.session_state.page = "login_page"

        # Lógica de navegação entre páginas
        if st.session_state.page == "login_page":
            LoginPage().render()  # Chama a função show() do login.py
        elif st.session_state.page == "time_tracking_page":
            TimeTrackingPage().render()

        # login_page = LoginPage().render()

App.run()