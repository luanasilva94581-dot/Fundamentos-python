def mostrar_nomes(nomes):
    for nome in nomes:
        print(f"O nome da lista é: {nome}")

lista_nomes = ["Oscar", "Kishan", "Bucky", "Lian"]
mostrar_nomes(lista_nomes)

#Adiocionando nomenovo na lista
def adcionar_nome(nomes, nome):
    nomes.append(nome)
    print(nomes)

adcionar_nome(lista_nomes, "Steve")

#   Adicionando novo nome em uma posição especifica
def adicionar_nome_posicao(nomes, nome, posicao):
    nomes.insert(posicao, nome)
    print(f"O nome {nome} foi inserido na posição {posicao} da lista: {nomes}")
adicionar_nome_posicao(lista_nomes, "ligth", posicao=2)

# Juntando duas listas
def juntar_nomes(nomes, novos_nomes):
    (nomes.extend(novos_nomes))
    print(f"Os novos nomes {novos_nomes} foram inseridos na lista {nomes}")

novos_nomes = ["Carlos","Max", "Yuki"]
juntar_nomes(lista_nomes, novos_nomes)

#removendo itens da lista
def removendo_nome (nomes, nome):
    if nome not in nomes:
        print(f"Este nome não existe na lista")
    else:
        nomes.remove(nome)
        print(f"O nome {nome} foi removido na lista: {nomes}")
removendo_nome(lista_nomes, "Yuki")


#removendo nome pelo indice
def remover_nome_pelo_indice(nomes, posicao):
    nomes.pop(posicao)
    print(f"O nome da posição {posicao} da lista: {nomes[posicao]}, foi removido!")
remover_nome_pelo_indice(lista_nomes, 6)

#descobrindo a posição(index) pleo nome
def encontrar_posicao_pelos_valores(nomes, nome):
    if nome not in nomes:
        print('nome não encontrado')
    else:
        posicao = nomes.index(nome)
        print(f"O nome {nome} foi encontrado na lista: {posicao}")

encontrar_posicao_pelos_valores(lista_nomes, "Kishan")

#caontando elementos da lista
def quantidade_de_nomes(nomes):
    quantidade = len(nomes)
    print(f"Quantidade de nomes: {quantidade}")
#quantidade_de_nomes(lista_nomes)

#ordenando os elemententos da lista
def odernar_nomes(nomes):
    lista_nomes_ordenados = sorted(lista_nomes)
    print(f"A lista ordenada é {lista_nomes_ordenados}")
#ordenar_nomes(lista_de_nomes)


#operações matematicas
#calcular media
def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade
    print(f'A meida das notas é {media}')

def gerenciar_notas(notas, nova_nota):
    notas.append(nova_nota)
    notas_ordenadas = sorted(notas)

    media = sum(notas) / len (notas)

    return notas_ordenadas, media

#notas_ordenadas, batata =  gerenciar_notas()
#print(f'A nota ordenada = {notas_ordenadas}')
#print(f'A media das notas é {batata}')
#agerenciar_notas()


notas_semestre = [7.8, 9.0, 4.5, 3.0,]
#calcular_media(notas_semestre)

#lista das listas
def adicionar_produtos(produtos, produto):
    produtos.append(produto)
    print(f"minha lista de produtos: {produtos[0][2]}")

lista_produtos = [
    ["Morango", 4, 50.00],
    ["bala fini", 3, 29.00]
]
novo_produto = ["coca-cola",3 , 9.00, "Monster", 4, 30.00]
adicionar_produtos(lista_produtos, novo_produto)

def quantidade_total_produtos(produtos):
    quantidade = []
    for produto in produtos:
        quantidade.append(produto[1])
    return sum(quantidade)

quantidade_total_produtos(lista_produtos)

def valor_total_produtos(produtos):
    valores = []

    for produto in produtos:
        valor = produto[1] * produto[2]
        valores.append(valor)

        return sum(valores)

preco_total_produtos = valor_total_produtos(lista_produtos)
print(f'O valor total dos produtos é {preco_total_produtos}')
