def calcular_diferenca_absoluta():
    try:
        # Solicita ao usuário para inserir dois números decimais
        num1 = float(input("Insira o primeiro número decimal: "))
        num2 = float(input("Insira o segundo número decimal: "))

        # Calcula a diferença absoluta
        diferenca = abs(num1 - num2)

        # Arredonda o resultado para duas casas decimais
        diferenca_arredondada = round(diferenca, 2)

        print(f"A diferença absoluta entre os números é: {diferenca_arredondada}")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

# Chama a função
calcular_diferenca_absoluta()
