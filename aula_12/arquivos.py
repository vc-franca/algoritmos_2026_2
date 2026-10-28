# arquivo = open('teste.txt', 'r')

# for linha in arquivo.readlines():
#     print(linha, end='')

# arquivo.close()

# isso
# arquivo = open('teste.txt', 'w')
# arquivo.write('vou para Pernambuco ano que vem')
# arquivo.close()

# é isso: 
# with open('teste.txt', 'w') as file:
#     file.write()

# pares = open('aula_12/pares.txt', 'w')
# impares = open('aula_12/impares.txt', 'w')

# for i in range(1000):
#     if i % 2 == 0:
#         pares.write(str(i) + '\n')
#     else:
#         impares.write(str(i) + '\n')

# ------------------------------------ EX1 ----------------------------------- #
import os

contatos = []

nome_arquivo = 'contatos.txt'

def carregar_contatos():
    if not os.path.exists(nome_arquivo):
        return

    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            nome, sobrenome, telefone, email = linha.strip().split(';')

            contatos.append({
                'nome': nome,
                'sobrenome': sobrenome,
                'telefone': telefone,
                'email': email
            })

def salvar_contatos():
    with open(nome_arquivo, 'w') as arquivo:
        for contato in contatos:
            arquivo.write(f'{contato['nome']}; {contato['sobrenome']}; {contato['telefone']}; {contato['email']}')

def novo_contato():
    nome = input('Digite o nome: ')
    sobrenome = input('DIgite o sobrenome: ')
    telefone = input('DIgite o telefone: ')
    email = input('Digite o email: ')

    novo = {
        'nome': nome,
        'sobrenome': sobrenome,
        'telefone': telefone,
        'email': email
    }

    contatos.append(novo)

def exibe_contato():
    print(f'Nome: {contatos['nome']} \n Sobrenome: {contatos['sobrenome']} \n Telefone: {contatos['telefone']} \n Email: {contatos['email']}')

def buscar_contato():
    nome = input('Digite o nome a aser buscado: ')

    for i in range(len(contatos)):
        if contatos[i]['nome'] == nome:
            exibe_contato()

def menu():
    print('''
1- novo contato
2- buscar contato (nome)
3- atualizar contato
4- apagar contato
0- sair
''')

def processa_menu(menu):
    if menu == 1:
        novo_contato()
        return True
    elif menu == 2:
        buscar_contato()
        return True
    elif menu == 3:
        atualizar_contaato()
        return True
    elif menu == 4:
        apagar_contato()
        return True
    elif menu == 0:
        return False

    return False

carregar_contatos()
while True:
    carregar_contatos()
    menu()

    menu = int(input())

    if not menu(menu):
        break

    salvar_contatos()