def controlar_estoque():
    produto = {
        "nome": "Mouse",
        "preco": 80,
        "estoque": 10
    }

    quantidade = int(input("Digite a quantidade vendida: "))

    if quantidade <= produto["estoque"]:
        produto["estoque"] -= quantidade
        print(f"Venda realizada!")
        print(f"Estoque restante:", produto["estoque"])
    else:
        print(f"Quantidade maior que o estoque disponível.")


controlar_estoque()