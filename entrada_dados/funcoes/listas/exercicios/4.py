def remover_produto(produtos, produto):
    produtos.remove(produto)
    print("Lista de produtos:", produtos)


produtos = ["Arroz", "Feijão", "Macarrão", "molho"]

produto = input("Digite o produto que deseja remover: ")

remover_produto(produtos, produto)