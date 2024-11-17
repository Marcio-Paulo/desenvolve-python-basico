#entrada de dados (Entrada)
comprimento = int(input("Digite o comprimento: "))
largura     = int(input("Digite a Largura: "))
preco_m2    = float(input("Digite o valor do m2: "))

#Processamento
area_m2     = comprimento * largura
preco_total = preco_m2 * area_m2

#Impressão de dados (Saída)
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")