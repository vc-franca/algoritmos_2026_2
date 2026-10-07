# ------------------------------------ EX1 ----------------------------------- #
# preco = int(input('Insira o preço: '))
# codigo = int(input('INsira o código de origem do produto: '))

# if codigo == 1:
#     print(f'Preço: {preco}; Procedência: Sul')
# elif codigo == 2:
#     print(f'Preço: {preco}; Procedência: Norte')
# elif codigo == 3:
#     print(f'Preço: {preco}; Procedência: Leste')
# elif codigo == 4:
#     print(f'Preço: {preco}; Procedência: Oeste')
# elif codigo > 4 and codigo < 7 or codigo > 24 and codigo < 31:
#     print(f'Preço: {preco}; Procedência: Nordeste')
# elif codigo == 7 or codigo == 8 or codigo == 9:
#     print(f'Preço: {preco}; Procedência: Sudeste')
# elif codigo > 9 and codigo < 21:
#     print(f'Preço: {preco}; Procedência: Centro-Oeste')
# else:
#     print('Produto importado')

# ------------------------------------ EX2 ----------------------------------- #
# a = int(input('Digite o primeiro valor: '))
# b = int(input('Digite o segundo valor: '))
# c = int(input('Digite o terceiro valor: '))

# if a == b or a == c or b == c:
#     resultado = 'Por favor, digite três valores diferentes'
# elif a > b > c:
#     resultado = f'{a}, {b}, {c}'
# elif a > c > b:
#     resultado = f'{a}, {c}, {b}'
# elif b > a > c:
#     resultado = f'{b}, {a}, {c}'
# elif b > c > a:
#     resultado = f'{b}, {c}, {a}'
# elif c > a > b:
#     resultado = f'{c}, {a}, {b}'
# elif c > b > a:
#     resultado = f'{c}, {b}, {a}'

# print(f'Em ordem decrescente: {resultado}')

# ------------------------------------ EX3 ----------------------------------- #
# altura = float(input('Digite sua altura (m): '))
# sexo = input('Insira seu sexo (m ou f): ')

# formula_m = (72.7 * altura) - 58
# formula_f = (62.1 * altura) - 44.7

# if sexo == 'm':
#     print(f'Seu peso ideal é: {formula_m:.2f}')
# else:
#     print(f'Seu peso ideal é: {formula_f:.2f}')
