velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MLTADO! Você excedeu o limite permitido que é de 80KM/h')
    multa = (velocidade -80) *7
    print(f'Você deve pagar uma multa de {multa:.2f}!')
print('Tenho um bom dia! Dirija com segunrança')