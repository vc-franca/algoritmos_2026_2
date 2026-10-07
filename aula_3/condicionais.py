# ----------------------------------- EX 1 ----------------------------------- #
# a = int(input('Digite um número: '))
# b = int(input('Digite outro número: '))

# if a > b:
#     print(f'Maior: {int(a)}')

# if b > a:
#     print(f'Maior: {int(b)}')

# if a == b:
#     print('Os dois números são iguais')

# ----------------------------------- EX 2 ----------------------------------- #
# x = int(input('Escreva um número positivo ou negativo: '))

# if x >= 0:
#     print(f'{x} é positivo')
# else:
#     print(f'{x} é negativo')

# ----------------------------------- EX 3 ----------------------------------- #
# x = int(input('Digite um número que corresponda a um dia da semana: '))

# if x == 1:
#     print('Domingo')
# if x == 2:
#     print('Segunda')
# if x == 3:
#     print('Terça')
# if x == 4:
#     print('Quarta')
# if x == 5:
#     print('Quinta')
# if x == 6:
#     print('Sexta')
# if x == 7:
#     print('Sábado')

# ----------------------------------- EX 4 ----------------------------------- #
# salario = float(input('Digite seu salário: '))

# if salario > 1250.0:
#     aumento = salario * 0.1
#     print(f'Salário reajustado: {aumento + salario}')
# else:
#     aumento = salario * 0.15
#     print(f'Salário reajustado: {aumento + salario}')

# ----------------------------------- EX 5 ----------------------------------- #
# ano_atual = int(input('Digite o ano atual: '))
# ano_nascimento = int(input('Digite seu ano de nascimento: '))

# if ano_atual - ano_nascimento >= 18:
#     print('Você pode tirar CNH')
# if ano_atual - ano_nascimento < 18:
#     print('Você não pode tirar CNH')

# ----------------------------------- EX 6 ----------------------------------- #
# idade_carro = int(input('Digite a idade do seu carro em anos: '))

# if idade_carro < 3:
#     print('E aí novinha')
# else:
#     print('Carroça véia')

# ----------------------------------- EX 7 ----------------------------------- #
# distancia = int(input('Digite a distância a ser percorrida (km): '))

# if distancia <= 200:
#     passagem = 0.5
#     passagem *= distancia
#     print(f'O valor da passagem será de: {passagem}')
# else:
#     passagem = 0.45
#     passagem *= distancia
#     print(f'O valor da passagem será de: {passagem}')

# ----------------------------------- EX 8 ----------------------------------- #
# from math import ceil

# altura = int(input('Digite a altura do cilindro: '))
# raio = int(input('Digite o raio do cilindro: '))

# area_base = 3.14 * raio**2
# perimetro = 2 * 3.14 * raio
# area_lateral = altura * perimetro
# area_cilindro = area_base + area_lateral

# litros = area_cilindro / 3

# qtd_latas = ceil(litros / 5)

# if qtd_latas == 1:
#     custo_total = qtd_latas * 50
#     print(custo_total)
# elif qtd_latas == 2:
#     custo_total = qtd_latas * 48
#     print(custo_total)
# elif qtd_latas == 3:
#     custo_total = qtd_latas * 46
#     print(custo_total)
# elif qtd_latas > 3:
#     custo_total = qtd_latas * 45
#     print(custo_total)
