import math
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adiacente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')