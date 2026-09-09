def cadastrar_pessoa():
    pessoa = {
    "nome": "Luana",
    "idade": 17
}

    pessoa["email"] = input("Digite o email: ")
    pessoa["endereco"] = input("Digite o endereço: ")
    pessoa["telefone"] = input("Digite o telefone: ")

    print(f"DADOS DO CADASTRO:")
    print(f"Nome:", pessoa["nome"])
    print(f"Idade:", pessoa["idade"])
    print(f"Email:", pessoa["email"])
    print(f"Endereço:", pessoa["endereco"])
    print(f"Telefone:", pessoa["telefone"])


cadastrar_pessoa()