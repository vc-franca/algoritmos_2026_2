# ------------------------------------- 1 ------------------------------------ #
# x = 15 / 3 + 2
# print(x)

# x = 12 % 5 * 2
# print(x)

# x = 3 ** 2 + (4 * 2) - 5
# print(x)

# x = (8 + 2) * (5 - 3) + (12 / 4) ** 2
# print(x)

# ------------------------------------- 2 ------------------------------------ #
# A * B >= 100 and C / A <= B 
# 2 * 50 >= 100 and 100 / 2 <= 50
# 100 >= 100 and 50 <= 50
# true and true
# true

# B + A > C or D < A and C - B == B
# 50 + 2 > 100 or -1 < 2 and 100 - 50 == 50
# 52 > 100 or true and 50 == 50
# false or true and true
# false or true
# true

# ------------------------------------- 3 ------------------------------------ #
# n1 = float(input('Digite a nota N1: '))
# n2 = float(input('Digite a nota N2: '))

# media = (3.5*n1 + 7.5*n2) / 11

# print(f'Média = {media:.2f}')

# ------------------------------------- 4 ------------------------------------ #
# distancia = float(input('digite a distância percorrida: '))

# if distancia <= 200:
#     preco = 0.5
#     passagem = preco * distancia
# else:
#     preco = 0.45
#     passagem = preco * distancia

# print(f'{passagem:.2f}')

# ------------------------------------- 5 ------------------------------------ #
# n = int(input('Digite um numero: '))

# if n % 2 == 0:
#     print('O número digitado é PAR')

#     if n % 4 == 0:
#         print('O número é multiplo de 4')
#     else:
#         print('O número não é multiplo de 4')
# else:
#     print('O número digitado é IMPAR')

#     if n % 7 == 0:
#         print('O número é multiplo de 7')
#     else:
#         print('O número não é multiplo de 7')

# ------------------------------------- 6 ------------------------------------ #
# n = int(input('Digite o número desejado: '))

# e = 1

# for i in range(1, n + 1):
#     e += 1/i

# print(f'{e:.3f}')

# ------------------------------------- 7 ------------------------------------ #
# ac = 0

# while True:
#     n = int(input())

#     ac += n

#     if n == 0:
#         break

# print(f'Resultado: {ac}')