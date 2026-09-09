def remover_telefone():
    funcionario = {
        "nome": "junior",
        "idade": 40,
        "cargo": "encanador",
        "salario": 4000,
        "telefone": "(19) 6767-8482"
    }

    print(f"Antes da remoção:")
    print(funcionario)

    telefone_removido = funcionario.pop("telefone")

    print(f"telefone removido:", telefone_removido)

    print(f"Depois da remoção:")
    print(funcionario)


remover_telefone()