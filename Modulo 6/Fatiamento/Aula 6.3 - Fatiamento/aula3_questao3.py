import random

# Gerar lista com 20 elementos entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]

print("Lista original:")
print(lista)

# Definir o tamanho do intervalo (ex: 3 elementos consecutivos)
tamanho_intervalo = 3
maior_qtd_negativos = -1
inicio_maior_intervalo = 0

# Percorrer a lista para encontrar o intervalo com mais números negativos
for i in range(len(lista) - tamanho_intervalo + 1):
    intervalo = lista[i:i + tamanho_intervalo]
    qtd_negativos = sum(1 for num in intervalo if num < 0)
    if qtd_negativos > maior_qtd_negativos:
        maior_qtd_negativos = qtd_negativos
        inicio_maior_intervalo = i

# Deletar o intervalo com mais negativos
del lista[inicio_maior_intervalo:inicio_maior_intervalo + tamanho_intervalo]

print("\nLista após deletar o intervalo com mais números negativos:")
print(lista)
