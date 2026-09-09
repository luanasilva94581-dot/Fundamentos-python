def lista_compras():
    compra = {
        "cliente": "Maria",
        "produtos": []
    }

    for i in range(5):
        produto = input("Digite o nome do produto: ")
        compra["produtos"].append(produto)

    print(f"Cliente:", compra["cliente"])
    print(f"Produtos comprados:")

    for produto in compra["produtos"]:
        print(f"-", produto)


lista_compras()