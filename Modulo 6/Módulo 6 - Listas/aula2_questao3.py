# Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50.
# Crie uma terceira lista interseccao contendo apenas os valores que se repetem nas duas listas.
# Ao final imprima:
# Ambas as listas
# A lista intersecção ordenada
# A quantidade de vezes que cada elemento aparece em cada lista
# Atenção, a lista de intersecções não pode ter duplicatas. 

import random
from collections import Counter

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = sorted(list(set(lista1) & set(lista2)))

contagem1 = Counter(lista1)
contagem2 = Counter(lista2)

print("Lista 1:")
print(lista1)

print("\nLista 2:")
print(lista2)

print("\nInterseção (sem duplicatas, ordenada):")
print(interseccao)

print("\nQuantidade de vezes que cada elemento da interseção aparece em cada lista:")
for valor in interseccao:
    print(f"Valor {valor}: aparece {contagem1[valor]}x na lista1 e {contagem2[valor]}x na lista2")
