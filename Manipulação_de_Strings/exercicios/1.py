def nome_maiusculo (nome):
    return nome.title()

nome = input("Digite um nome: ")

resultado = nome_maiusculo(nome)

print("Nome Maiusculo", resultado)