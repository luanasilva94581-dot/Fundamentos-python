def caixa_eletronico():
    saldo = float(input("Digite o saldo disponivel: "))
    saque = float(input("Digite o valor que deseja sacar: R$ "))

    if saque <= 0
        print("valor do saque inválido")
    elif saque > saldo:
        print("saldo insuficiente")
    else:
        saldo = saldo - saque
        print("saque realizado")
        print(f"Novo saldo: {saldo:.2f}")

caixa_eletronico()
