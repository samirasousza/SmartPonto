from datetime import datetime, timedelta


def get_month_days(ano, mes):
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

        dias =[dia.timestamp() for dia in dias]

        return dias