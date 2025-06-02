#Crie um programa em Python que receba duas listas de números do usuário, 
# podendo cada lista ter uma quantidade diferente de valores.
# Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. 
# Intercale os elementos até o final da primeira lista, 
# adicionando ao final os elementos remanescentes da maior lista.
# Exemplo de interação via terminal (entradas em laranja): 
# Função para ler uma lista de números do usuário


def ler_lista(nome):
    entrada = input(f"Digite os números da {nome}, separados por espaço: ")
    return [int(x) for x in entrada.strip().split()]

lista1 = ler_lista("primeira lista")
lista2 = ler_lista("segunda lista")

lista_combinada = []

max_len = max(len(lista1), len(lista2))

for i in range(max_len):
    if i < len(lista1):
        lista_combinada.append(lista1[i])
    if i < len(lista2):
        lista_combinada.append(lista2[i])

print("\nPrimeira lista:", lista1)
print("Segunda lista:", lista2)
print("Lista combinada alternada:", lista_combinada)
