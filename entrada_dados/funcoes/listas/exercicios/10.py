def inverter_lista(lista):
    nova_lista = list(reversed(lista))
    return nova_lista


lista = ["Lua", "Dede", "Lucas", "Maria", "Fran"]

resultado = inverter_lista(lista)

print("Lista invertida:", resultado)