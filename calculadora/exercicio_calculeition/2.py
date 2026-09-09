def alterar_informacoes():
    aluno = {
        "nome": "Luana",
        "idade": 17,
        "telefone": "(19) 99999-9999",
        "endereco": "Rua das Flores, 100",
        "cidade": "Piracicaba",
        "nota": 8.5,
        "turma": "3º Ano",
        "curso": "Desenvolvimento de Sistemas"
    }

    print(f"ANTES DAS ALTERAÇÕES:")
    print(aluno)

    aluno["idade"] = 18
    aluno["cidade"] = "Campinas"

    print(f"DEPOIS DAS ALTERAÇÕES:")
    print(aluno)


alterar_informacoes()