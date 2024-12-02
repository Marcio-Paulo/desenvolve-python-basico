# Leia o valor de n
n = int(input("Digite a quantidade de números a serem lidos: "))

# Inicialize a variável 'maior'
maior = 0

# Loop enquanto n for maior que 0
while n > 0:
    # Leia o próximo número
    x = int(input("Digite um número: "))
    
    # Verifique se x é maior que 'maior'
    if x > maior:
        maior = x
    
    # Decremente o valor de n
    n -= 1

# Imprima o maior número encontrado
print("O maior número é:", maior)
