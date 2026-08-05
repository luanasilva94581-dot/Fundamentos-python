def combustivel()
    distancia = float(input("Distancia percorrida em km "))
    combustivel = float(input("Combustivel gasto em litros "))
    media = distancia / combustivel
    print(f'Valor da combustivel: {media}')

combustivel()