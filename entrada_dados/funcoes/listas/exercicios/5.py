def remover_item(itens, posicao):
    removido = itens.pop(posicao)
    return removido


itens = ["Caderno", "Caneta", "Lápis", "Borracha"]

posicao = int(input("Digite a posição do item que deseja remover: "))

item_removido = remover_item(itens, posicao)

print("Item removido:", item_removido)
print("Lista atualizada:", itens)