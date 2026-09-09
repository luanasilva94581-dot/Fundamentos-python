def calcular_notas():
    aluno = {
        "nome": "livia",
        "notas": [8,6.8, 9.0]
    }

    notas = aluno["notas"]

    media = sum(notas) / len(notas)

    print(f"Nome:", aluno["nome"])
    print(f"Notas:", notas)
    print(f"Maior nota:", max(notas))
    print(f"Menor nota:", min(notas))
    print(f"Média:", media)


calcular_notas()