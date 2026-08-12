def verificacao_numero ():

    numero = int(input("Digite um numero inteiro"))

    if numero > 0:
        print("Positivo")
    if numero < 0:
        print("Negativo")
    else:
        print("zero")

verificacao_numero()