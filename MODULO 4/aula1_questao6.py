# Entrada de dados
#Quantidade de experimento
n = int(input("Digite o número de experimentos registrados: "))
#Inicializar Variaveis e controle
cont = 0

sapos, coelhos, ratos = 0, 0, 0
# Interações
while cont < n:
    quantia = int(input())
    tipo = input()

    if tipo == 'C':
        coelhos += quantia
    elif tipo == 'R':
        ratos += quantia
    elif tipo == 'S':
        sapos += quantia
    cont += 1
        
# Cálculos
total = coelhos + ratos + sapos
percentual_coelhos = (coelhos / total) * 100
percentual_ratos = (ratos / total) * 100
percentual_sapos = (sapos / total) * 100

# Saída
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")