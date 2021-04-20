# DESAFIO 51 COM WHILE.
# script lerá o primeiro termo e a razão de uma PA e mostrará os 10 primeiros termos de uma progressão.
print('*'*15)
print('Generator PA 10x 2.0')
print('*'*15)

p = int(input('Enter first PA term: '))
r = int(input('Enter reason PA: '))

termo = p
contador = 1

while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    contador += 1
