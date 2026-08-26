def adicionar_nota(notas, nota):
    notas.append(nota)


def remover_nota(notas, nota):
    if nota in notas:
        notas.remove(nota)
        print("Nota removida:", nota)
    else:
        print("Nota não encontrada.")


def media_notas(notas):
    if len(notas) > 0:
        media = sum(notas) / len(notas)
        return media
    else:
        return 0


notas = [8, 7, 9]

adicionar_nota(notas, 10)

print("Notas:", notas)

remover_nota(notas, 7)

print("Notas após remoção:", notas)

media = media_notas(notas)

print("Média das notas:", media)