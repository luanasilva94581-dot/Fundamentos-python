def  classificar_nota ():

    nota = float(input("Digite a nota de 0 a 10: "))

    if nota >= 0 or nota <= 4:
        print("Insuficiente")

    elif nota >= 6:
        print("Regular")

    elif nota >= 8:
        print("Bom")

    elif nota <= 10:
        print("Exelente")

classificar_nota()