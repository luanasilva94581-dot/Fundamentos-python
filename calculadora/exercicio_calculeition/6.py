def cadastrar_notas():
    aluno = {}

    aluno["nome"] = input("Digite o nome do aluno: ")

    aluno["nota1"] = float(input("Digite a primeira nota: "))
    aluno["nota2"] = float(input("Digite a segunda nota: "))
    aluno["nota3"] = float(input("Digite a terceira nota: "))

    media = (aluno["nota1"] + aluno["nota2"] + aluno["nota3"]) / 3

    aluno["media"] = media

    print(f"DADOS DO ALUNO:")
    print(f"Nome:", aluno["nome"])
    print(f"Nota 1:", aluno["nota1"])
    print(f"Nota 2:", aluno["nota2"])
    print(f"Nota 3:", aluno["nota3"])
    print(f"Média:", aluno["media"])


cadastrar_notas()