# Operador or

def posso_comprar():
    TEM_CARTAO = false
    tem_dinheiro = bool(input("Voce tem dinheiro para comprar? "))
    autorizado = tem_dinheiro or TEM_CARTAO
    print(f"Vou comer um Mc-Donalds hoje? {autorizado}")


posso_comprar()
