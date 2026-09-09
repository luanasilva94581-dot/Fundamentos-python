def verificar_chave():
    usuario = {
        "nome": "Luana",
        "idade": 17,
        "email": "luana@email.com",
        "cidade": "Piracicaba"
    }

    chave = input("Digite o nome da chave que deseja verificar: ")

    if chave in usuario:
        print("A chave existe no dicionário.")
    else:
        print("Sinto muito mas a chave não existe no dicionário.")


verificar_chave()