#Você está desenvolvendo um programa para verificar se um ano é bissexto.
# Escreva um código em Python que solicita ao usuário para inserir um ano e imprime "Bissexto"
# se o ano for (1) divisível por 4 e não for divisível por 100, ou (2) se for divisível por 400.
# Caso contrário, imprima "Não Bissexto".
# Teste seu código com os valores: 1900 (não bissexto), 2000 (bissexto), 2016 (bissexto) e 2017 (não bissexto).

ano1= int(input("Digite o ano: "))
ano2 = int(input("Digite o ano: "))
ano3 = int(input("Digite o ano: "))
ano4 = int(input("Digite o ano: "))
anos = ano1, ano2, ano3, ano4
if (ano1 % 4 == 0 and ano1 % 100 != 0) or (ano1 % 400 == 0):
    print(f"{ano1} Bissexto")
else:
    print (f"{ano1} Não Bissexto")

if (ano2 % 4 == 0 and ano2 % 100 != 0) or (ano2 % 400 == 0):
    print(f"{ano2} Bissexto")
else:
    print (f"{ano2} Não Bissexto")

if (ano3 % 4 == 0 and ano3 % 100 != 0) or (ano3 % 400 == 0):
    print(f"{ano3} Bissexto")
else:
    print (f"{ano3} Não Bissexto")

if (ano4 % 4 == 0 and ano4 % 100 != 0) or (ano4 % 400 == 0):
    print(f"{ano4} Bissexto")
else:
    print (f"{ano4} Não Bissexto")
