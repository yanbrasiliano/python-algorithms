'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

totalv = totalp = barato = contador = 0
x = ' '

while True:
	print('~REGISTER PRODUCT~')
	produto = str(input('Name: ')).strip()
	contador+=1
	valor = float(input('R$ '))
	totalv += valor
	if valor > 1000:
		totalp += 1
	if contador == 1:
		barato = valor
		x = produto
	else:
		if valor < barato:
			barato = valor  
			x = produto
	opção = ' '
	while opção not in 'YN':
		opção = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
	if opção == 'N':
			break

print(f'Total value: R${totalv}')
print(f'{totalp} products cost more than R$1000.')
print(f'The cheapest product is {x} and you value is: R${barato}')