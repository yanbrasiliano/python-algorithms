# DESAFIO 51 COM WHILE e IMPLEMENTAÇÕES NOVAS.
# script lerá o primeiro termo e a razão de uma PA e mostrará os 10 primeiros termos de uma progressão. No final, ele perguntará quantos termos a mais a pessoa quer, se necessário.
from time import sleep
print('*'*15)
print('Generator PA 10x 3.0')
print('*'*15)

p = int(input('Enter first PA term: '))
r = int(input('Enter reason PA: '))

termo = p
contador = 1
total = 0
x = 10

while x != 0:
	total+=x
	while contador <= 10:
			print('{} -> '.format(termo), end='')
			termo += r
			contador += 1
	print('PAUSE')
	x = int(input('How many more terms do you want?'))


print("Finishing...")
sleep(2)
print('Bye!')