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
d = {
    'um': 'one',
    'dois': 'two',
    'tres': 'three'
}

def procuraChave(dicio, valor):

    for valor in dicio.values():
        print(dicio)

procuraChave(d, 'one')