def cadastrar_alunos():
    alunos = []

    for i in range(5):
        print(f"Cadastro do aluno", i + 1)

        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        nota = float(input("Digite a nota: "))

        aluno = {
            "nome": nome,
            "idade": idade,
            "nota": nota
        }

        alunos.append(aluno)

    print("===== ALUNOS CADASTRADOS =====")

    for aluno in alunos:
        print(f"Nome:", aluno["nome"])
        print(f"Idade:", aluno["idade"])
        print(f"Nota:", aluno["nota"])
        print()


cadastrar_alunos()