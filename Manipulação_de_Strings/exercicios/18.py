def validar_senha(senha):
    tem_letra = False
    tem_numero = False
    tem_espaco = False

    for caractere in senha:
        if caractere.isalpha():
            tem_letra = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere.isspace():
            tem_espaco = True

    if len(senha) >= 8 and tem_letra and tem_numero and not tem_espaco:
        print("Senha válida!")
    else:
        print("Senha inválida!")


senha = input("Digite a senha: ")

validar_senha(senha)