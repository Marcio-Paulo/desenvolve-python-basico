#entrada de dados (Entrada)
Fahrenheit = int(input("Digite a Temperatura em °F: "))

#Processamento
Celcius = (Fahrenheit - 32) * (5/9)

#Impressão de dados (Saída)
print(f"{Fahrenheit} graus Fahrenheit são {int(Celcius)} graus Celsius")