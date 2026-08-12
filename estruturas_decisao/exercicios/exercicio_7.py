def temperatura ():

    temperatura = float(input("Informe a temperatura em graus Celsius: "))

     if temperatura < 15:
         print("Frio")

    elif temperatura <= 25:
        print("Agradável")

    else:
        print("Quente")

temperatura()