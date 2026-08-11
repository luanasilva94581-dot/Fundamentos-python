def prestacao():
    valor = float(input('digite o valor do produto: '))
    parcelas = int(input('digite guantas parcelas: '))

    prestacao = valor / parcelas
    print(f'O valor de cada parcela é {prestacao:.2f}')

    prestacao()