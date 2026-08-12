def maior_numero ():

    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero: "))

    if numero1 > numero2:
        print("O maior numero é:", numero1)
    elif numero2 > numero1:
        print("O maior numero é:", numero2)
    else:
        print("Os números são iguais")

maior_numero()