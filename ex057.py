sexo = str(input('Informe seu sexo [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. por favor, informe seu sexo: '))
print(f'Sexo {sexo} registrado com sucesso')
