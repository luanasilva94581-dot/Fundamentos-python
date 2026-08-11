def troca_valores ()
    #antes
a = int(input('Digite o valor do A: '))
b = int(input('Digite o valor do B: '))

print(f'\nantes')
print(f'o valor do A: {a}')
print(f'o valor do B: {b}')

a, b = b, a

print(f'\ndepois')
print(f'o valor do A: {a}')
print(f'o valor do B: {b}')

troca_valores()