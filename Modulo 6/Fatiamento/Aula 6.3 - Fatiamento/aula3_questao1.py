# Solicitar do usuário uma quantidade indefinida de números (pelo menos 4)
print("Digite ao menos 4 números inteiros (digite 'fim' para encerrar):")
numeros = []

while True:
    entrada = input("Digite um número (ou 'fim' para terminar): ")
    if entrada.lower() == 'fim':
        if len(numeros) >= 4:
            break
        else:
            print("Você deve digitar pelo menos 4 números.")
    else:
        try:
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro ou 'fim'.")

# Imprimir conforme solicitado, usando fatiamento
print("\nLista original:", numeros)
print("3 primeiros elementos:", numeros[:3])
print("2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])
