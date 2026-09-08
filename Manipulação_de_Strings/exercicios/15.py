def validar_especie(animal):
    if animal.isalpha():
        print("Espécie de animal válida.")
    else:
        print("Espécie inválida.")


animal = input("Digite a espécie do animal: ")

validar_especie(animal)