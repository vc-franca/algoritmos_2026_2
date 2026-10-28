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
palavra = input('Digite uma palavra: ')

i = 0
j = len(palavra) - 1
palindromo = True

while i <= j:
    if palavra[i] != palavra[j]:
        palindromo = False
        break

    i += 1
    j -= 1

if palindromo:
    print('é palíndromo')
else:
    print('não é palíndromo')