def limpar_texto(texto):
    return texto.strip()

texto = input("Digite uma frase: ")

resultado = limpar_texto(texto)

print("texto sem espaços", resultado)
