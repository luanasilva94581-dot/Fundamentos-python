def sistema_votacao ():
    idade = int(input("Digite sua idade: "))

    if idade < 16:
        print("Não pode votar")
    elif idade < 17:
        print("votar é opcional")
    elif idade < 69:
        print("votar é obrigatorio")
    elif idade < 70:
        print("voto opcional")

sistema_votacao()