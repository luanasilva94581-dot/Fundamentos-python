def inserir_aluno(alunos, nome, posicao):
    alunos.insert(posicao, nome)
    print("Lista de alunos:", alunos)


lista_alunos = []

nome = input("Digite o nome do aluno: ")
posicao = int(input("Digite a posição do aluno: "))

inserir_aluno(lista_alunos, nome, posicao)