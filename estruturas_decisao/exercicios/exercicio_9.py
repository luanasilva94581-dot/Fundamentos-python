def calculadora_simples ():

    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    operacao = input("Escolha a operação desejada (+, -, * ou /)")

     if operacao == "+":
         print(numero1 + numero2)
    elif operacao == "-":
        print("resultado", numero1 - numero2)
 elif operacao == "*":
        print("Resultado:", numero1 * numero2)
    elif operacao == "/":
        if numero2 != 0:
            print("Resultado:", numero1 / numero2)
        else:
            print("Não é possível dividir por zero")
    else:
        print("Operação inválida")

calculadora_simples()