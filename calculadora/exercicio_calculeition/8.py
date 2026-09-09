def fazer_login():
    usuario = {
        "login": "admin",
        "senha": "1234"
    }

    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    if login == usuario["login"] and senha == usuario["senha"]:
        print("Login realizado com sucesso!")
    else:
        print(f"Login ou senha incorretos.")


fazer_login()