# Faça um programa que imprima os números ímpares entre 0 e umnúmero digitado pelo usuário

# x = 0
# n = int(input('Digite um número: '))

# while x <= n:
#     if x % 2 != 0:
#         print(x)
#         x += 1
#     x += 1


# Faça um programa que imprima os números de 1 a 50 de 1 em 1 e de 52 a 100 de 2 em 2
# i = 0

# while i <= 50:
#     print(i)
#     i += 1

# i = 52

# while i <= 100:
#     print(i)
#     i += 2

# Escreva um programa que imprima a tabuada de um número digitado pelo usuário

# n = int(input('Digite o número o qual desejas ver a tabuada: '))

# i = 1

# for i in range(1, 11):
#     print(f'{i} x {n} = {i * n}')
#     i += 1


# Faça um programa que leia 6 números inteiro positivos do usuário exiba o maior o número lido
# maior = 0

# for i in range(6):
#     x = int(input('número: '))
#     if x > maior:
#         maior = x

# print(f'o maior é: {maior}')


#  Faça um programa que solicita um número entre 0 e 10
# ▶ Mostre uma mensagem de erro caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.
# ▶ Quando o valor for válido dê a mensagem “número aceito”.
# ▶ Dica: você pode utilizar operadores lógicos (and ou or) na
# condição do while também!

# x = 11

# while x < 1 or x > 10:
#     x = int(input('Número inválido. Digite um valor ente 0 e 10'))
# print('número aceito')

# while True:
#     x = int(input('Valor ente 0 e 10: '))
#     if 0 < x < 10:
#         print('número aceito')
#         break


#  Escreva um programa que leia números digitados pelo usuário
# ▶ O programa deve ler os números até que o 0 (zero) seja digitado.
# ▶ Quando o 0 for digitado, o programa deve exibir:
# ⋆ a quantidade de números que foram digitados;
# ⋆ a somatória destes números;
# ⋆ e a média aritmética.

# x = 0

# while True:
#     x = int(input('Digite um número: '))
#     if x != 0:
#         print()

#         break

# 9) Faça um programa que leia um valor n, inteiro e positivo calcule e mostre a seguinte soma: S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
# n = int(input('Digite um número: '))

# soma = 0
# cont = 1

# while cont <= n:
#     soma += 1/cont
#     print(f'soma - 1 /cont = {soma}')
#     cont += 1

# 11) Foi feita uma pesquisa entre os habitantes de uma região.
# Foram coletados os dados de idade, sexo (M/F) e salário. Faça
# um programa que informe:
# a) a média de idade do grupo;
# b) a média de salários dos homens;
# c) quantidade de mulheres com salário abaixo de R$600,00.
# Encerre a entrada de dados quando for digitada uma idade
# negativa (os dados da idade negativa não podem entrar nos
# cálculos dos itens solicitados acima)

# # 3 acumuladores
# soma_idade = 0
# soma_sal_m = 0
# media_m = 0

# # 3 contadores
# cont_total = 0
# cont_m = 0
# cont_f_600 = 0

# while True:
#     idade = int(input('Digite e idade: '))
#     sexo = input('Digite o sexo: ')
#     salario = float(input('Digite o salário: '))

#     if idade < 0:
#         break

#     cont_total += 1
#     soma_idade += idade

#     if sexo == 'M':
#         cont_m +=1
#         soma_sal_m += salario
#     elif salario < 600:
#         cont_f_600 += 1

# print(f'Média de idade do grupo: {soma_idade / cont_total}')

# if cont_m > 0:
#     media_m = soma_sal_m / cont_m

# print(f'Média de salário dos homens: {media_m}')
# print(f'Média de salário das mulheres: {cont_f_600}')

