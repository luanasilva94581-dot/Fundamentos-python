def IMC ()
peso = float(input('Qual o seu peso?'))
altura = float(input('Qual a sua altura?'))

imc = peso / (altura ** 2)
print(f'seu imc é {imc:.2f}')

imc()