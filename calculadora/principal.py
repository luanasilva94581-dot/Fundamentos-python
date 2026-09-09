from calculeition import somar, subtrair, multiplicar, dividir

def executar_calculeition():

    operacoes = {
        "1": somar,
        "2": subtrair,
        "3": multiplicar,
        "4": dividir
    }

    while True:
        print("=============CALCULEITION============")
        print("*************ESCOLHA UMA OPÇÃO***********")
        print("1- Somar")
        print("2- Subtrair")
        print("3- Multiplicar")
        print("4- Dividir")
        print("0- Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("-----CALCULEIRO ENCERRADA!-----")
            break

        if opcao not in operacoes:
            print("OPÇÃO INVÁLIDA!")
            continue

        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))

        funcao = operacoes[opcao]

        resultado = funcao(numero1, numero2)

        print(f'O resultado da operação é {resultado}')

executar_calculeition()
