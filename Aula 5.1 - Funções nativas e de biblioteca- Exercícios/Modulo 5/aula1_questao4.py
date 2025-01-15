from datetime import datetime

def exibir_data_hora_atual():
    # Obtém a data e hora atuais
    agora = datetime.now()

    # Formata a data e hora
    data_formatada = agora.strftime("%d/%m/%Y")
    hora_formatada = agora.strftime("%H:%M")

    # Exibe os resultados
    print(f"Data: {data_formatada}")
    print(f"Hora: {hora_formatada}")

# Executa a função
exibir_data_hora_atual()
