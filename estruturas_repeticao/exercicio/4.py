def pares():
    while True:
        numero = int(input("digite o primeiro numero: "))

        for numero in range(1, numero + 1):
            if numero % 2 != 0:
                print(f'Seus numeros impares: {numero}')
        break

pares()