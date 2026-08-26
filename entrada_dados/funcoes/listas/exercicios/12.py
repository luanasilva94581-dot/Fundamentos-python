def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade

    return media


lista_notas = [8, 7, 9, 10]

resultado = calcular_media(lista_notas)

print("A média das notas é:", resultado)