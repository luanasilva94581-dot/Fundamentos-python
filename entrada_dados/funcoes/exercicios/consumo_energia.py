def consumo_energia ()
    consumo = float(input('Digite o valor do consumo: '))
    preco = float(input('digite o preco'))

    valor = consumo * preco

    print(f'O valor da conta é {valor:.2f}')

    consumo_energia()