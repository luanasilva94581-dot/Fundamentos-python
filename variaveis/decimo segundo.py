from statistics import median

produto_condicionado = 21.90
produto_biscoito = 10.98
produto_miojo = 3.50

total = produto_condicionado + produto_biscoito + produto_miojo
print(f'O total da compra é de R${total:.2f}')

media = total / 3
print(f"a media da sua compra é de R${media:.2f}")

print(f"o produto mais caro da sua compra é o condicionador custando {produto_condicionado:.2f}")