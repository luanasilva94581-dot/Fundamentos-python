def adicionar_convidados(convidados, novos_convidados):
    convidados.extend(novos_convidados)
    print("Lista de convidados:", convidados)


convidados = ["Lua", "Maria"]

novos_convidados = ["João", "Ana", "Lucas"]

adicionar_convidados(convidados, novos_convidados)