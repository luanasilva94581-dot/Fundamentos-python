def calculadora_frete ():
    compra = float(input("Digite o valor do compra: R$ "))

    if compra <= 100:
        frete = 20
    elif compra <= 300:
        frete = 10
    elif:
        frete = 0

        total = compra + frete
    print(f"valor da compra: {compra:2.f}"
    print(f"valor da frete: {frete:2.f}")
    print(f"total: {total:2.f}")

calculadora_frete()
