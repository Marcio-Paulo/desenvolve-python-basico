n = int(input("Digite a quantidade de idades: "))
#inicializar a variavel

# resultado da soma
soma = 0
#variavel de controle do laço
cont = 0

#Laço de repetição 
while cont < n:
    cont += 1
    idade = int(input())
    soma += idade


# Imprima a média
print(f"A soma das idades é {soma}.")
print(f"A média das idades é {soma/n:.0f} anos")