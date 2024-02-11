núm = 0
cont = 0
soma = 0
while núm != 999:
    núm = int(input('Digite um número [999 para parar]: '))
    soma += núm
    cont += 1
print(f'Você digitou {cont - 1} número e a soma entre eles foi {soma - 999}')
