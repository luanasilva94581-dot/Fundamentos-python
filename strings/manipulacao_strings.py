# Converter texto para maiúsculas e minúsculas
def formatar_nome(nome):
    #nome maiúsculo:
    nome_maiusculo = nome.upper()

    # nome minúsculo:
    nome_minusculo = nome.lower()

    #nome com primeira letra maiúsculo:
    nome_camel_case = nome_maiusculo.capitalize()

    return (nome_maiusculo, nome_minusculo, nome_camel_case)

nome = input("digite seu nome: ")

# print(formatar_nome(nome)[1])

banana, batata, cebola = formatar_nome(nome)
print(f"Nome maiusculo: {banana}")
print(f"Nome minusculo: {batata}")
print(f"Nome camel_case: {cebola}")

# remover espaços desnecessarios
def limpar_texto(texto):
    #remove espaços no inicio e final do texto
    texto_Limpo = texto.strip()
    # Remove espaços da esquerda .lstrip()
    # Remove espaços da direita .rstrip()
    return texto_Limpo

texto_1 = ("       Aprender Python é legal!!!!!!!      "
           "")
print(f"Texto ates: {texto_1}")
print(f"Texto depois: {limpar_texto(texto_1)}")

# Substituir palavras
def trocar_cidade(texto):
    # Troca uma palavra por outra
    texto_trocado = texto.replace("São Paulo", "Piracicaba")
    return texto_trocado

cidade = input("digite seu cidade: ")
print(f"Eu moro em: {trocar_cidade(cidade)}")

# Contar caracteres ou ocorrencias
def analisar_texto(texto, Letras ):
    # contar a quantidade de caracteres
    qtde_caracteres = len(texto)

    # Contar a quantidade de ocorridos
    qtde_letra= texto.strip().lower().count("a")

    return qtde_caracteres, qtde_letra

texto_2 = input("digite seu texto: ")
Letra = input("digite uma letra: ")
caracteres, Letra = analisar_texto(texto_2, Letra)

print(f"Total de caracteres: {caracteres}")
print(f"Total de letras pesquisadas: {Letra}")

# Verificar se uma palavra está presente
def verificar_palavra(frase, palavra):
    palavra_presente = frase.lower() in frase.lower()
    # Retorna um booleano (true ou false)
    return palavra_presente

frase = input("digite uma frase: ")
palavra = input("digite uma palavra: ")

print(f"A palavra está presente na frase?: {verificar_palavra(frase, palavra)}")

# Encontrar a posição de uma palavra
def encontra_letra(texto, letra):
    encontrar_posicao_palavra = texto.lower().find(palavra.lower())
    return encontrar_posicao_palavra

frase_2 = input("digite uma nova frase: ")
palavra_2 = input("digite uma palavra para saber sua posicao: ")

print(f"A posição da palavra é: {encontra_letra(frase_2, palavra_2)}")