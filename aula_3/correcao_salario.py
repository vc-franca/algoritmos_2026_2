valor_hora = int(input('Valor por hora de trabalho: '))
horas_mensais = int(input('Horas mensais trabalhadas: '))

salario_bruto = (valor_hora * horas_mensais)

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.5

salario_liquido = salario_bruto - ir - inss - sindicato

print(f'Salário bruto: R$ {salario_bruto:.2f}')
print(f'IR (11%): R$ {ir:.2f}')
print(f'INSS (8%): R$ {inss:.2f}')
print(f'Sindicato: R$ {sindicato:.2f}')
print(f'Salário líquido: R$ {salario_liquido}')
