// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract SmartPonto {
    // Evento para log de ponto
    event CheckEvent(
        string indexed cardId,
        string timestamp,
        string checkIn,
        string checkOut
    );

    event Aviso(string Mensagem);
    event PontoEvent(string entrada, string sainda, bool justificado, string justificativa);

    // Estrutura de ponto com entrada e saída
    struct Check {
        uint exists;
        string checkIn;
        string checkOut;
        bool excused;
        string excuse;
    }

    // Mapeamento: funcionario => data => ponto
    mapping(string => mapping(string => Check)) public registros;

    // Bater ponto entrada
    function checkIn(string memory cardId, string memory datetime, string memory date) public {
        Check storage check = registros[cardId][date];
        
        
        if (check.excused == false){
            
            if (bytes(check.checkIn).length == 0) {
                check.checkIn = datetime;
                check.excuse = "Nao ha justificativas";
                emit CheckEvent(cardId, datetime, check.checkIn, check.checkOut);
            } else {
                emit Aviso("Ponto ja registrado (entrada e saida) para essa data");
            }

        }else{
            emit Aviso("Ponto ja justificado para essa data");
        }
    }

    // Bater ponto da saída
    function checkOut(string memory cardId, string memory datetime, string memory date) public {
        Check storage check = registros[cardId][date];
        
        
        if (check.excused == false){
        
        if (bytes(check.checkIn).length != 0 && bytes(check.checkOut).length == 0) {
            check.checkOut = datetime;
        } if(bytes(check.checkIn).length == 0 ) {
            emit Aviso(" falta fazer checkin");
        } if (bytes(check.checkOut).length != 0){
            emit Aviso("Ponto ja registrado de saida para essa data");

        } else{
            emit Aviso("Deu tudo errado");

        }

        emit CheckEvent(cardId, datetime, check.checkIn, check.checkOut);
        }else{
            emit Aviso("Ponto ja justificado para essa data");
        }
    }

    function excuseCheckIn(string memory cardId, string memory datetime, string memory date, string memory excuse) public{
        Check storage check = registros[cardId][date];

        if ((bytes(check.checkIn).length == 0 && bytes(check.checkOut).length == 0 )) {
        check.excused = true;
        check.excuse = excuse;
        check.checkIn = datetime;
        check.checkOut = datetime;
        } else {
            emit Aviso("Ponto ja registrado para essa data");
        }
    }

    // Função para consultar um ponto específico
    function consultarPonto(string memory cardId, string memory date)
        public
        returns (string memory entrada, string memory saida, bool justificado, string memory justificativa)
    {
        Check memory check = registros[cardId][date];
     
        emit Aviso(date);
        if (bytes(check.checkIn).length > 0 && bytes(check.checkOut).length > 0 ){
            emit Aviso("Exixte ponto, funcionario veio");
            emit PontoEvent (check.checkIn, check.checkOut, check.excused, check.excuse);
            return (check.checkIn, check.checkOut, check.excused, check.excuse);
        }else {
            emit Aviso("Nao existe ponto para esse dia, funcionario faltou");
            return("", "", false, "");
        }
    }
}