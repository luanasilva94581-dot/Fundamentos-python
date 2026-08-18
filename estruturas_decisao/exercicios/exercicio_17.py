def triangulo ():
    lado1 = float(input("Digite o primeiro lado: "))
    lado2 = float(input("Digite o segundo lado: "))
    lado3 = float(input("Digite o terceiro lado: "))

    if lado1 == lado2 and lado2 == lado3:
        print("Equilatero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Isósceles")
    else:
        print("Escaleno")

triangulo()