# Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos. Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade
# correspondente a num_elementos, e armazene em uma lista chamada elementos.
# Em seguida imprima:
# A lista elementos
# A soma dos valores da lista
# A média dos valores da lista
import random

# Gerar aleatoriamente um valor entre 5 e 20
num_elementos = random.randint(5, 20)

# Gerar uma lista com valores aleatórios entre 1 e 10, na quantidade definida por num_elementos
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Calcular a soma e a média dos elementos da lista
soma = sum(elementos)
media = soma / num_elementos

# Imprimir os resultados
print(f"Quantidade de elementos gerados: {num_elementos}")
print(f"Lista de elementos: {elementos}")
print(f"Soma dos valores: {soma}")
print(f"Média dos valores: {media:.2f}")
