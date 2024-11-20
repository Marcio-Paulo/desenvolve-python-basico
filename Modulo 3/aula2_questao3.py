#Terminal

#Digite sua idade: 17

idade = int(input("Digite sua idade: "))

#Já jogou pelo menos 3 jogos de tabuleiro? True

jogos = input("Já jogou mais de 3 jogos de tabuleiro?"
              "(Responda True ou False)")

#Quantos jogos já venceu? 1

venceu = int(input("Já venceu quantos jogos? "))

#Apto para ingressar no clube de jogos de tabuleiro: True

admissao = 16 <= idade <= 18 and jogos and venceu >= 1

#Saída
print(f"Apto para ingressar no clube de jogos de tabuleiro: {admissao}")