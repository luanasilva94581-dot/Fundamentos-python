def classificar_velocidade():
    velocidade = float(input("Digite a velocidade (km/h): "))

    if velocidade <= 60:
        print("Velocidade permitida")
    elif velocidade <= 80:
        print("Atenção: velocidade acima do permitido")
    else velocidade <80
        print("Multa por excesso de velocidade")


classificar_velocidade()