# Operadores and e or

def posso_entrar_no_swoh_do_veigh():
        POSSUI_INGRESSO = True
        idade = int(input("Qual sua idade? "))
        nome_esta_na_lista = bool(input("Qual o nome da lista? "))

        posso_entrar = (nome_esta_na_lista or POSSUI_INGRESSO) and idade >=18

        print(f"Vou conseguir entrar no show? {posso_entrar}")

posso_entrar_no_swoh_do_veigh()