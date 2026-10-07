# ------------------------------ checar se é par ----------------------------- #
# def is_even(value):
#     if value % 2 ==0:
#         return print('par')
    
#     return print('ímpar')

# x = int(input('Digite um valor: '))

# is_even(x)

# ------------------------------------- cronômetro ------------------------------------ #
# from time import sleep

# def cronometro(segundos_total, segundos_intervalo):
#     for i in range(1, segundos_total + 1, segundos_intervalo):
#         sleep(segundos_intervalo)
#         print(i)

# cronometro(10, 2)

# ------------------------------------- variáveis globais ------------------------------------ #
# a = 5

# def alterar_valor():
#     global a
#     a = 7

# print(a)
# a = alterar_valor(a)
# print(a)

# se eu quiser acessar uma variável com valor modificado por uma função,
# eu tenho que atribuir o valor da variável chamando a própria função com essa variável como parêmetro

# ------------------------------ alores padrões ------------------------------ #
# a = 5

# def alterar_valor(x = 0):
#     global a
#     a = x

# print(a)
# alterar_valor(10)
# print(a)
# alterar_valor()
# print(a)

# ---------------------------------- funções lambda (arrow functions do js/ts só que com "lambda" ao invés de "=>") ---------------------------------- #
# def somaF(x=1, y=1):
#     return x + y

# somaL = lambda x=1, y=1: x + y

# print(somaF())
# print(somaL())

# # sintaxe horrível, JS é muito mais legível
# # poderiam deixar pelo menos os parênteses das funções. 

# ---------------------------------- binário --------------------------------- #
for i in range(2):
    for k in range(2):
        print(i, k, end=', ')