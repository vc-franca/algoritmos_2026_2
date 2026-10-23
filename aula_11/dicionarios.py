# dicionario = {
#     1: 'exemplo',
#     2: 'de',
#     3: 'dicionario'
# }

# dicionario['six'] = 'seven'


# del dicionario['six']

# print(dicionario)

# print(list(dicionario.items())) # pode ser útil pro projeto
# print(list(dicionario.values()))

# for k in dicionario.keys():
#     print(f'chave: {k}, valor: {dicionario[k]}')

# ------------------------------------ EX1 ----------------------------------- #
# d = {
#     'um': 'one',
#     'dois': 'two',
#     'tres': 'three'
# }

# def procuraChave(dicio, valor):
#     L = []

#     for chave in dicio:
#         if dicio[chave] == valor:
#             L.append(chave)

#     return L



# print(procuraChave(d, 'one'))

# ------------------------------------ EX2 ----------------------------------- #
# import random

# numeros = {}

# for i in range(21):
#     numeros[i] = 0

# for i in range(100):
#     x = random.randint(0, 20)

#     numeros[x] += 1

# print(numeros)

# ------------------------------------ EX3 ----------------------------------- #
