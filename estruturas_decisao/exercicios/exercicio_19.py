def classificar_numero():
    numero = int(input("Digite um número inteiro: "))

    if numero > 0:
        tipo = "positivo"
    elif numero < 0:
        tipo = "negativo"
    else:
        tipo = "zero"

    if numero == 0:
        paridade = "par"
    elif numero % 2 == 0:
        paridade = "par"
    else:
        paridade = "ímpar"

    print(f"Número: {numero}")
    print(f"Classificação: {tipo} e {paridade}")


classificar_numero()