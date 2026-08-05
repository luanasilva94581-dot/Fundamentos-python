def comissao():

    salario = float(input('salario: '))
    vendas = float(input('quantidade de vendas: '))
    percentual = float(input('percentual de vendas: '))
    salario_final = salario * (percentual/100)
    print(f'salario final: {salario_final}')

comissao()