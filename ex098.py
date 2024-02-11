def contador(i, f, p):
    print(f'contagem de {i} até {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end='')
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end='')
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
