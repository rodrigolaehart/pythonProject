pri = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = pri + (10 - 1) * razão
for c in range(pri, décimo, razão):
    print(f'{c}')
print('ACABOU')
