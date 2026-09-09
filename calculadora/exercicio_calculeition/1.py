def cadastrar_pessoa():
    pessoa = {
        "nome": "Luana",
        "idade": 17,
        "telefone": "(19) 99999-9999",
        "endereco": "Rua das Flores, 100",
        "cidade": "Piracicaba"
    }

    print(f"Nome:", pessoa["nome"])
    print(f"Idade:", pessoa["idade"])
    print(f"Telefone:", pessoa["telefone"])
    print(f"Endereço:", pessoa["endereco"])
    print(f"Cidade:", pessoa["cidade"])


cadastrar_pessoa()