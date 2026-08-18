def classificar_imc():
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    imc = peso / (altura ** 2)

    if imc < 18.5:
        print(f"Abaixo do peso")
    elif imc <= 25:
        print(f"Peso normal")
    elif imc <= 30:
        print(f"Sobrepeso")
    elif imc <= 40:
        print(f"Obesidade")

        print(f"imc: {imc:.2f}")

classificar_imc()

