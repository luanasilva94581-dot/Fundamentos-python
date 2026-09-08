def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)


texto = input("Digite um texto: ")

resultado = contar_palavras(texto)

print("Quantidade de palavras:", resultado)