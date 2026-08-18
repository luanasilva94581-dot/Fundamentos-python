def preco_incresso ():
    idade = int(input("Digite sua idade: "))

    if idade < 5:
        print("ingresso gratuito!")
    elif idade < 12:
        print("Ingresso: R$ 10,00")
    elif idade < 59:
        print("Ingresso: R$ 20,00")
    elif idade < 60:
        print("Ingresso: R$ 10,00")

preco_incresso()
