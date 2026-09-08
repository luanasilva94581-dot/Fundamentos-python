def contar_letra(frase, letra):
    return frase.count(letra)

frase = input("Digite uma frase: ")
letra = input("Digite uma letra: ")

resultado = contar_letra(frase, letra)

print("A letra aparece", resultado, "vezes")