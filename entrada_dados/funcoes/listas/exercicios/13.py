def adicionar_cliente(fila, cliente):
    fila.append(cliente)


def atender_cliente(fila):
    if len(fila) > 0:
        cliente = fila.pop(0)
        return cliente
    else:
        return "Não há clientes na fila."


fila = []

while True:
    cliente = input("Digite o nome do cliente ou 'sair' para finalizar: ")

    if cliente.lower() == "sair":
        break

    adicionar_cliente(fila, cliente)

print("\nFila de atendimento:", fila)

while len(fila) > 0:
    cliente_atendido = atender_cliente(fila)
    print("Cliente atendido:", cliente_atendido)