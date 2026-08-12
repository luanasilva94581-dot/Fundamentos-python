def aluno_aprovado():
        nota_1 = float(input("Digite sua primeira nota: "))
        nota_2 = float(input("Digite sua segunda nota: "))

        media = (nota_1 + nota_2) / 2

        if media >= 6:
            print("Aluno aprovado!")
        elif media >= 5 and media < 6:
            print("Aluno de recuperação!")

    aluno_aprovado()







def login():
    e_mail_input = input("Digite seu e-mail: ")
    senha_input = input("Digite sua senha: ")

    if e_mail_input == e_mail_input and senha_input == senha_input:
        print("Logado!")
        acessar_admin = input("Deseja acessar area administrativa? (Digite S ou N): ")
        if acessar_admin == "S":
            codigo_secreto_input = input("Digite seu codigo secreto: ")
            if codigo_secreto_input == codigo_secreto_input:
                print("Acesso adm liberado")
            else:
                print("codigo secreto errado")
        elif acessar_admin == "N":
            print("Voce acessou como usuario comum")
        else:
            print("opção invalida")
    else:
        print("Email ou senha incorreto!")

login()