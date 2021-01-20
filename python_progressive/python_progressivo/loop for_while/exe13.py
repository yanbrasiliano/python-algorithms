#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

#Resultado com função pow.
'''from math import pow
base = int(input('Enter base to potentiation: '))
exp = int(input('Enter exponentiation to potentiation: '))
r = pow(base,exp)
print(f'Result: {r}')'''

#Resultado com While
while True:
	base = int(input('Enter base to potentiation: '))
	exp = int(input('Enter exponentiation to potentiation: '))
	r = base**exp
	if exp < 0:
		r = (1/base)**exp
	print(f'{r}')
	option = ' '
	while option not in 'YN':
		option=str(input('CONTINUE? [Y/N]')).strip().upper()
	if option == 'N':
		break
print('thanks!')








