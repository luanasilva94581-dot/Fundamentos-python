def verificar_aprovacao():
    aluno = {
        "nome": "Luana",
        "media": 7.5,
        "frequencia": 80
    }

    if aluno["media"] >= 6 and aluno["frequencia"] >= 75:
        print(f"Aluno aprovado!")
    else:
        print(f"Aluno reprovado.")

verificar_aprovacao()