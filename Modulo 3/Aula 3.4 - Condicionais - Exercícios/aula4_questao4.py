#Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete
# Com base na distância e no peso do pacote. Escreva um código que solicita
# A distância da entrega em quilômetros e o peso do pacote em quilogramas.
# O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

# Entrada de dados Solicita os dados ao usuário
distancia = float(input("Digite a distância da entrega em quilômetros: "))
peso = float(input("Digite o peso do pacote em quilogramas: "))

# Determina o custo por quilograma com base na distância
if distancia <= 100:
    custo_por_kg = 1.0
elif 101 <= distancia <= 300:
    custo_por_kg = 1.50
else:
    custo_por_kg = 2.0

# Calcula o custo base
custo_frete = custo_por_kg * peso

# Aplica a taxa adicional se o peso for superior a 10 kg
if peso > 10:
    custo_frete += 10

# Calcula e exibe o valor do frete
print(f"O valor do frete é: R${custo_frete:.2f}")