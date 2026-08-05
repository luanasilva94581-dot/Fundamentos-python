def desconto():
    preco = float(input('preco: R$'))
    percentual =float(input('desconto: (%) '))
    valor_final = preco - (preco * percentual/100)
    print(f'valor final: {valor_final}')

desconto()