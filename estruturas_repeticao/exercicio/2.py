def contato():
    while True:
        num_1 = int(input("digite o primeiro numero: "))
        num_2 = int(input("digite o segundo numero: "))
        if num_1 <= 0 and num_2 <= 0:
            print('numero incontaveis')
            break
        else:
            for i in range(num_1, num_2):
                print(f'Contando {i}')
        break


contato()