from random import random

lista1 = [round((random() * 100)) for i in range(10)]
print(lista1)

lista2 = [random() for i in range(5)]
print(lista2)

lista3 = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete']
print(lista3)

completa = []
completa.append(lista1)
completa.append(lista2)
completa.append(lista3)

lista1 = []
lista2 = []
lista3 = []

print(completa)

for i in range(len(completa)):
    print(f'lista [{i+1}]')

    for j in range(len(completa[i])):
        print(completa[i][j])