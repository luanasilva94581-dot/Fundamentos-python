def cadastrar_produto(produtos):
    nome = input("Digite o  produto: ")
    preco = float(input("Digite o preço: "))
    estoque = int(input("Digite o estoque: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(produto)

    print("Produto cadastrado com sucesso!")


def listar_produtos(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        print("\n===== PRODUTOS =====")

        for produto in produtos:
            print(f"Nome:", produto["nome"])
            print(f"Preço: R$", format(produto["preco"], ".2f"))
            print(f"Estoque:", produto["estoque"])
            print()


def buscar_produto(produtos):
    nome = input("Digite o nome do produto: ")

    encontrado = False

    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            print(f"Produto encontrado!")
            print(f"Nome:", produto["nome"])
            print(f"Preço: R$", format(produto["preco"], ".2f"))
            print(f"Estoque:", produto["estoque"])
            encontrado = True

    if not encontrado:
        print("Produto não encontrado.")


def atualizar_estoque(produtos):
    nome = input("Digite o nome do produto: ")

    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            quantidade = int(input("Digite a quantidade para alterar: "))

            produto["estoque"] += quantidade

            if produto["estoque"] < 0:
                produto["estoque"] = 0

            print(f"Estoque atualizado!")
            print(f"Novo estoque:", produto["estoque"])
            return

    print(f"Produto não encontrado.")


def remover_produto(produtos):
    nome = input("Digite o nome do produto que deseja remover: ")

    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            produtos.remove(produto)
            print(f"Produto removido com sucesso!")
            return

    print(f"Produto não encontrado.")


def sistema():
    produtos = []

    while True:
        print(f"===== SISTEMA DE PRODUTOS =====")
        print(f"1 - Cadastrar produto")
        print(f"2 - Listar produtos")
        print(f"3 - Buscar produto")
        print(f"4 - Atualizar estoque")
        print(f"5 - Remover produto")
        print(f"6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto(produtos)

        elif opcao == "2":
            listar_produtos(produtos)

        elif opcao == "3":
            buscar_produto(produtos)

        elif opcao == "4":
            atualizar_estoque(produtos)

        elif opcao == "5":
            remover_produto(produtos)

        elif opcao == "6":
            print(f"Sistema encerrado!")
            break

        else:
            print(f"Opção inválida. Tente novamente.")


sistema()