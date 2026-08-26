def adicionar_produtos(compras, produtos):
    compras.extend(produtos)


def cancelar_compra(compras, produto):
    if produto in compras:
        compras.remove(produto)
        print("Produto removido:", produto)
    else:
        print("Produto não encontrado.")


compras = ["Arroz", "Feijão", "Leite"]

novos_produtos = ["Pão", "Macarrão", "Café"]

adicionar_produtos(compras, novos_produtos)

print("Lista de compras:", compras)

cancelar_compra(compras, "Leite")

print("Lista de compras atualizada:", compras)