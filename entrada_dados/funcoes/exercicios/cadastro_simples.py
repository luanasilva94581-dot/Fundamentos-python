from entrada_dados.input import idade


def cadastro_simples():
    nome = input('Digite seu nome  : ')
    idede = input('Digite sua idede  : ')
    profissao = input('Digite sua profissao  : ')
    cidade = input('Digite sua cidade  : ')

print(cadastro_simples())
print(f'nome: {nome}')
print(f'idade: {idade}')
print(f'profissao: {profissao}')
print(f'cidade: {cidade}')

cadastro_simples()