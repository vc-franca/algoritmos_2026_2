# ----------------------------------- EX 1 ----------------------------------- #

# altura = float(input('Diga sua altura: '))

# peso_ideal = (72.7 * altura) - 58

# print('Peso ideal: ', peso_ideal)

# ----------------------------------- EX 2 ----------------------------------- #
# km_percorridos = float(input('digite a quantidade de quilômetros percorridos: '))
# dias_alugados = int(input('Digite a quantidade de dias alugados: '))


# preco_km = 0.15 * km_percorridos
# preco_dia = 60 * dias_alugados

# print('Total a pagar: ', (preco_km + preco_dia))

# ----------------------------------- EX 3 ----------------------------------- #
dias = int(input('quantidade de dias: '))
horas = int(input('quantidade de horas: '))
minutos = int(input('quantidade de minutos: '))
segundos = int(input('quantidade de segundos: '))

dias = 24 * 60 * 60 * dias
horas = 60 * 60 * horas
minutos = 60 * minutos

tempo_total = dias + horas + minutos + segundos

print('Tempo total em segundos foi de: ', tempo_total)
