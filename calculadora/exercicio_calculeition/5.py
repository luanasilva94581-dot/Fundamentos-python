def cadastrar_dados():
    dados = {}

    quantidade = int(input("Quantas informações deseja cadastrar? "))

    for i in range(quantidade):
        chave = input("Digite o nome da chave: ")
        valor = input("Digite o valor: ")

        dados[chave] = valor

    print(f"DADOS CADASTRADOS:")

    for chave, valor in dados.items():
        print(chave, ":", valor)


cadastrar_dados()