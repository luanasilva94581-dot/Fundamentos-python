def criar_email(nome, sobrenome, dominio):
    email = nome.lower() + "." + sobrenome.lower() + "@" + dominio.lower()
    return email


nome = input("Digite o nome: ")
sobrenome = input("Digite o sobrenome: ")
dominio = input("Digite o domínio: ")

resultado = criar_email(nome, sobrenome, dominio)

print("E-mail:", resultado)
