# l = []

# for i in range(10):
#     l.append(2*i)

# print(l)
# print(l[5])

# ------------------------------------ exemplo ----------------------------------- #
# l = []

# for i in range(5):
#     x = int(input())
#     l.append(x)

# print(l)
# print(f'O primeiro eemento é: {l[0]}')
# print(f'O último elemento é: {l[-1]}')
# print(f'tamanho: {len(l)}')

# print(f'10 está na lista? {10 in l}')

# ------------------------------------ EX2 ----------------------------------- #
# t = [11, 7, 2, 4]

# print(min(t))

# menor = t[0]

# for i in t:
#     if menor > i:
#         menor = i

# print(menor)

# ------------------------------------ EX4 ----------------------------------- #
# l = []

# maior = 0
# ind_maior = 0

# for i in range(10):
#     x = int(input(f'Digite o {i+1}º número: '))

#     l.append(x)

#     if x > maior:
#         maior = x
#         ind_maior = i

# print(f'Números: {l}')        
# print(f'Maior número: {maior}')
# print(f'índice do maior número: {ind_maior}')

# ------------------------------------- x ------------------------------------ #
# l = [15, 23, 4, 5, 6, 11]
# l2 = l[:]

# ------------------------------------ EX5 ----------------------------------- #
# x = int(input('Qtd de números: '))
# L = []
# maior = float('-inf')

# for i in range(5, 0, -1):
#     print(L[:])


#     num = int(input(f'digite o {i+1}º número: '))
#     L.append(num)

#     # # if (L[i] > maior):
#     # #     L[i] = L[i-1]
    
# print(f'números: {L}')

# print('inverso: {}')

# ---------------------------------- PROJETO --------------------------------- #
dados_login = ('123', 'recife') # tupla (lista imutável)

entrada_usuario = input('Digite o CPF: ')
entrada_senha = input('Digite a senha: ')

def logar():
    if entrada_usuario != dados_login[0]:
        print('CPF não encontrado')
        return

    if entrada_senha != dados_login[1]:
        print('senha incorreta')
        return

    print('logado com sucesso')
    print('1- consultar saldo')
    print('2- depositar')
    print('3- sair')

logar()