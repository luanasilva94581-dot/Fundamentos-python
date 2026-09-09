def cadastrar_filme():
    filme = {
        "titulo": "I.T A COISA",
        "ano": 2017,
        "genero": "terror",
        "notas": []
    }

    for i in range(5):
        nota = float(input("Digite a nota do filme: "))
        filme["notas"].append(nota)

    media = sum(filme["notas"]) / len(filme["notas"])

    print(f"FILME:")
    print(f"Título:", filme["titulo"])
    print(f"Ano:", filme["ano"])
    print(f"Gênero:", filme["genero"])
    print(f"Notas:", filme["notas"])
    print(f"Média:", media)


cadastrar_filme()