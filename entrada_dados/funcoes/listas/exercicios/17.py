def vender_produto(estoque, produto):
    if produto in estoque:
        estoque.remove(produto)
        print("Produto vendido:", produto)
    else:
        print("Produto não está disponível.")

    return estoque


estoque = ["Mouse", "Teclado", "Monitor", "Webcam"]

produto = input("Digite o produto que deseja vender: ")

estoque_atualizado = vender_produto(estoque, produto)

print("Estoque atualizado:", estoque_atualizado)