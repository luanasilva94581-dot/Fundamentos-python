def reajustar_preco():
    produto = {
        "nome": "Mouse",
        "preco": 100
    }

    aumento = float(input("Digite o percentual de aumento: "))

    produto["preco"] += produto["preco"] * aumento / 100

    print(f"Preço atual: R$ ", produto["preco"])

reajustar_preco()