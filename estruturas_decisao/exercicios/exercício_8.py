def Faixa_etária ():

    idade = int(input("Qual a sua idade: "))

    if idade >= 0 and idade <= 12:
        print("Criança")
    elif idade <= 17:
        print("Adolescente")
    elif idade <= 59:
        print("Adulto")
    else:
        print("Idoso")


Faixa_etária()