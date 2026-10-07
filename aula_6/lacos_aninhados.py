# problema da tabela 4 x 4:
# fazer só um <for i in range(16)> transformaria numa lista, achataria
# fazer 4 <for i in range(4)> com números adequados é imprático
# certo é:
# for i in range(4):
#     for k in range(4): 
        # código
# dá também pra identificar doordenadas estilo batalha naval

# for i in range(10):
#     # print(f'linha {i}: ')
#     # print(f'coluna: ', end=' ')

#     for k in range(10):
#         if i == k:
#             print(1, end=' ')
#         else:
#             print(f'{0}', end=' ')
#     print()

n = int(input('Digite a quantidade de números a serem testados: '))

total_primos = 0
primos = 0

for i in range(n):
    x = int(input(f'Digite o número {i}: '))
    if x > 1:
        primos = 1

    for k in range(2, x):
        if x % k == 0:
            primos = 0
            break

    total_primos += primos

print(f'Total de números primos: {total_primos}')