#Entrada de dados
genero = input("Gênero: ")
idade  = int(input("Idade: "))
tempo  = int(input("Tempo de Serviço: "))

#A: Para mulheres, ter mais de 60 anos. Para homens, 65.
a = (genero == 'feminino' and idade >=60) or \
    (genero == 'masculino' and idade >=65)
#B: Ou ter trabalhado pelo menos 30 anos
b = tempo >=30
#C: Ou ter 60 anos  e trabalhado pelo menos 25.
c = idade >=60 and tempo >=25

pode_aposentar = a or b or c


#saida
print(pode_aposentar)