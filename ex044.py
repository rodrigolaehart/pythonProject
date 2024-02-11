preço = float(input('Preço das compras: R$'))
print(''' Formas de pagamento
[ 1 ]à vista dinheiro/cheque
[ 2 ]à vista cartão 
[ 3 ]2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de {parcela:.2f}')
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
else:
    total = 0
    print('Opção inválida de pagamento. tente novamente')
print(f'Sua compra de R$ {preço:.2f} vai custar R${total:.2f} no final.')