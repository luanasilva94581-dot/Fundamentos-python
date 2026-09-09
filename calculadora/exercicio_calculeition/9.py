def consultar_cliente():
    cliente = {
        "nome": "Amanda",
        "idade": 14,
        "email": "amanda@email.com",
        "cidade": "itatuapeva"
    }

    informacao = input("Digite o nome da informação que deseja consultar: ")

    resultado = cliente.get(informacao)

    if resultado is not None:
        print(f"Informação:", resultado)
    else:
        print(f"Informação não encontrada.")


consultar_cliente()