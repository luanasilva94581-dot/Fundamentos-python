def desconto_compra ():

    valor = float(input("digite o valor da compra: "))

    if valor <= 100:
        desconto = 0;
    elif valor <= 500:
        desconto = 10;
    else:
        desconto = 15;

    valor_desconto = valor * desconto /100
    valor_final = valor - valor_desconto

    print("Desconto", desconto, "%")
    print("Valor final: R$", valor_final)

desconto_compra()
