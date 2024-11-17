#Entrada de dados
produto_1        = input("Digite o nome do produto 1: ")
valor_unit_1     = float (input("Digite o preço unitário do produto 1: "))
qntd_produto_1   = int (input ("Digite a quantidade do produto 1: "))
produto_2        = input("Digite o nome do produto 2: ")
valor_unit_2     = float (input("Digite o preço unitário do produto 2: "))
qntd_produto_2   = int (input("Digite a quantidade do produto 2: "))
produto_3        = input("Digite o nome do produto 3: ")
valor_unit_3     = float (input("Digite o preço unitário do produto 3: "))
qntd_produto_3   = int (input("Digite a quantidade do produto 3: "))

#Processamento
produto_1=valor_unit_1*qntd_produto_1
produto_2=valor_unit_2*qntd_produto_2
produto_3=valor_unit_3*qntd_produto_3
total  = produto_1+produto_2+produto_3
#Saida de dados
print(f"Total: R${total:,.2f}")