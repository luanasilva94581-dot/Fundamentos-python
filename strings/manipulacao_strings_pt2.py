# Dividir uma strings em partes
import urllib

def separar_nome(nome_completo):
    partes = nome_completo.split(" ")
    return partes

nome_completo = input("digite um nome completo: ")
print(f"Nome completo: {separar_nome(nome_completo)[2]}")

# juntar Strings
def criar_nome_completo(partes):
    nome_completo = ",".join(partes)
    return nome_completo

partes_nome = ["Lua", "Vitória", "Ramos"]
print(f"A junção das partes do nome completo: {criar_nome_completo(partes_nome)}")

# Verificar o inicio e o final de uma strings
def analisar_url(url):
    inicia_com_https = url.startswith("https://")
    termina_com_https = url.endswith("tem_br")
    return inicia_com_https, termina_com_https

url = "https://www.google.com"
tem_https, tem_br = analisar_url(url)
print(f"Utiliza https? {analisar_url(url)}")
print(f"Termina com .br? {tem_br}")

# Verificar se a strings comtém somente numeros
def validar_idade(idade):
    idade_valida = idade.isdigit()
    if idade_valida:
        print("O valor digitado é uma idade valida")
    else:
        print("Digete somente números!")

idade = input("digite sua idade: ")
validar_idade(idade)

# Verificar se a strings comtém somente letras
def nome_valido(nome):
    nome_valido = nome.isalpha()
    if nome_valido:
        print("O nome digitado é valido!")
    else:
        print("O nome deve conter somente letras")

nome = input("digite um nome válido: ")
nome_valido(nome)