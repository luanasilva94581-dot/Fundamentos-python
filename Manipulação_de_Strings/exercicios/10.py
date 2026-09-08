def separar_nome(nome_completo):
    partes = nome_completo.split()

    for parte in partes:
        print(parte)


nome_completo = input("Digite seu nome completo: ")

separar_nome(nome_completo)