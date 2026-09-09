def remover_informacao():
    funcionario = {
        "nome": "Yuri",
        "idade": 24,
        "cargo": "Apresentador",
        "salario": 7000,
        "telefone": "(19) 4002 8922"
    }

    del funcionario["telefone"]

    print(f"Dicionário atualizado:")
    print(funcionario)


remover_informacao()