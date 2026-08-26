def adicionar_nota(notas, nota):
    notas.append(nota)


def inserir_nota(notas, posicao, nota):
    notas.insert(posicao, nota)


def adicionar_varias_notas(notas, novas_notas):
    notas.extend(novas_notas)


def remover_nota(notas, nota):
    if nota in notas:
        notas.remove(nota)


def remover_ultima_nota(notas):
    if len(notas) > 0:
        return notas.pop()


def encontrar_posicao(notas, nota):
    if nota in notas:
        return notas.index(nota)
    else:
        return -1


def quantidade_notas(notas):
    return len(notas)


def ordenar_notas(notas):
    return sorted(notas)


def notas_inversas(notas):
    return list(reversed(notas))


def somar_notas(notas):
    return sum(notas)


def calcular_media(notas):
    return sum(notas) / len(notas)


notas = [7.5, 6.0, 8.5, 9.0, 5.5]

# 1. Adicionar uma nova nota
adicionar_nota(notas, 10.0)

# 2. Inserir uma nota em uma posição específica
inserir_nota(notas, 2, 7.0)

# 3. Adicionar várias notas
adicionar_varias_notas(notas, [8.0, 9.5])

# 4. Remover uma nota
remover_nota(notas, 6.0)

# 5. Remover a última nota
removida = remover_ultima_nota(notas)

# 6. Encontrar a posição de uma nota
posicao = encontrar_posicao(notas, 8.5)

# 7. Quantidade de notas
quantidade = quantidade_notas(notas)

# 8. Ordenar as notas
ordenadas = ordenar_notas(notas)

# 9. Mostrar notas em ordem inversa
inversas = notas_inversas(notas)

# 10. Soma das notas
soma = somar_notas(notas)

# 11. Média da turma
media = calcular_media(notas)


print("Notas atuais:", notas)
print("Última nota removida:", removida)
print("Posição da nota 8.5:", posicao)
print("Quantidade de notas:", quantidade)
print("Notas ordenadas:", ordenadas)
print("Notas em ordem inversa:", inversas)
print("Soma das notas:", soma)
print("Média da turma:", media)