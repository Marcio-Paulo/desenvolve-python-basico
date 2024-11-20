#O programa deve imprimir False se os pontos de atributo não são consistentes com a classe escolhida.
# Segue um exemplo de interação com seu código no terminal, com entradas de dados destacadas em laranja e as impressões de seu código em branco.
#Escolha a classe (guerreiro, mago ou arqueiro): mago
#Digite os pontos de força (de 1 a 20): 8
#Digite os pontos de magia (de 1 a 20): 17
#Pontos de atributo consistentes com a classe escolhida: True


classe = input("Escolha a classe do Personagem: ")

forca  = int(input("Digite os pontos de força de 1 a 20: "))

magia  = int(input("Digite os pontos de magia de 1 a 20: "))

#Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.

guerreiro = forca >=15 and magia <=10

#Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.

mago = forca <=10 and magia>=15

#Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum deles pode ser superior a 15.

arqueiro = forca >5 and magia <15

print(guerreiro or mago or arqueiro)