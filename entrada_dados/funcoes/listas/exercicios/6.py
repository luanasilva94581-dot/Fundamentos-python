def encontrar_produto(produtos, produto):
    posicao = produtos.index(produto)
    return posicao


produtos = ["Arroz", "Batata", "banana", "lentilha"]

produto = input("Digite o produto que deseja encontrar: ")

posicao = encontrar_produto(produtos, produto)

print("O produto está na posição:", posicao)