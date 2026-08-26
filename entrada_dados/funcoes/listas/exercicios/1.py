def adicionar_nome(nomes, nome):
    nomes.append(nome)
    print("Nome adicionado:", nome)
    print("Lista de nomes:", nomes)


lista_nomes = []

nome = input("Digite um nome: ")

adicionar_nome(lista_nomes, nome)