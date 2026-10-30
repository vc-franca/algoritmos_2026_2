# print(ord('a'))
# print(ord('A'))
# print(ord('b'))
# print(ord('B'))

# print(chr(97))

# for i in range(255):
#     if i > 65 and i <= 91:
#         print('%c' % i, end=' ')

# print(u'\u00ae')
# print(u'\u0061')
# print(u'\u00c7')

# ------------------------------------ EX1 ----------------------------------- #
# palavra = input('Digite uma palavra: ')

# nova_palavra = ''

# for char in palavra:
#     if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
#         nova_palavra += chr(ord(char) - 32)
#     else:
#         nova_palavra += char

# print(nova_palavra)

# vogais = ['a', 'e', 'i', 'o', 'u']

# for i in range(len(palavra)):
#     if palavra[i] in vogais:
#         palavra = palavra.replace(palavra[i], palavra[i].upper(), 1)

# print(palavra)

# ------------------------------------ EX2 ----------------------------------- #
# palavra = input('Digite uma palavra: ')

# i = 0
# j = len(palavra) - 1
# palindromo = True

# while i <= j:
#     if palavra[i] != palavra[j]:
#         palindromo = False
#         break

#     i += 1
#     j -= 1

# if palindromo:
#     print('é palíndromo')
# else:
#     print('não é palíndromo')

# ------------------------------------ EX3 ----------------------------------- #
# with open('aula_13/arquivo.txt', 'r') as arq:
#     a = arq.read().split()

# maior = 0

# for i in range(len(a)):
#     if len(a[i]) > maior:
#         maior = len(a[i]) + 1 

# print(maior)

# ------------------------------------ EX4 ----------------------------------- #
with open('aula_13/arquivo2.txt', 'r') as arq:
    a = arq.read().split()

palavras = [p.lower() for p in a]

for p in palavras:
    p = [i.isaplha() for i in p]

