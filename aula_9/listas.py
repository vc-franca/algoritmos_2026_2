# ------------------------------------ EX1 ----------------------------------- #
# l = []

# intervalo1 = 0
# intervalo2 = 0
# intervalo3 = 0
# intervalo4 = 0

# while True:
#     x = int(input('número: '))
#     l.append(x)

#     if x < 0:
#         break

#     if x in range(25):
#         intervalo1 += 1

#     if x in range(26, 51):
#         intervalo2 += 1

#     if x in range(51, 76):
#         intervalo3 += 1

#     if x in range(76, 101):
#         intervalo4 += 1

# print(intervalo1)
# print(intervalo2)
# print(intervalo3)
# print(intervalo4)

# ------------------------------------ EX2 ----------------------------------- #
# votos = [0 for i in range(1, 10)]
# sistemas = ['Windows Server', 'Unix', 'Linux', 'Netware', 'MacOS', 'TempleOS', 'Outro']

# while True:
#     voto = int(input('Voto: '))

#     if voto == 0:
#         break

#     if 0 < voto <= 6:
#         votos[voto] += 1

# print('Sistemas operacional | Votos | %')
# print(('-'*20))

# for i in range(7):
#     print(f'{sistemas[i]} | {votos[i]} | {(votos[i] / sum(votos)) * 100}')

# print(votos)

# ------------------------------------ EX3 ----------------------------------- #
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
