def analisar_temperaturas(temperaturas):
    quantidade = len(temperaturas)
    soma = sum(temperaturas)
    media = soma / quantidade
    ordenadas = sorted(temperaturas)

    return quantidade, soma, media, ordenadas


temperaturas = [25, 30, 22, 28, 26]

quantidade, soma, media, ordenadas = analisar_temperaturas(temperaturas)

print("Quantidade de temperaturas:", quantidade)
print("Soma das temperaturas:", soma)
print("Média das temperaturas:", media)
print("Temperaturas ordenadas:", ordenadas)