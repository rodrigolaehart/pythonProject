dis = float(input('Qual é a distância da sua viagem? '))
preco = dis * 0.50 if dis <= 200 else dis * 0.45
print(f'E o preço da sua viagem será de R${preco:.2f}')