import random

def jogo_adivinhacao():
    # Gera um número aleatório entre 1 e 10
    numero_aleatorio = random.randint(1, 10)
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número que estou pensando (entre 1 e 10).")

    while True:
        try:
            # Solicita um palpite do usuário
            palpite = int(input("Digite seu palpite: "))

            if palpite < 1 or palpite > 10:
                print("Por favor, insira um número entre 1 e 10.")
                continue

            # Compara o palpite com o número gerado
            if palpite < numero_aleatorio:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_aleatorio:
                print("Muito alto! Tente novamente.")
            else:
                print("Parabéns! Você acertou!")
                break
        except ValueError:
            print("Por favor, insira um número válido.")

# Executa o jogo
jogo_adivinhacao()
