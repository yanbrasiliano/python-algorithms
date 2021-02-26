"""
4. A probabilidade de dar um valor em um dado é 1/6 (uma em 6). Faça um
script em Python que simule 1 milhão de lançamentos de dados e mostre a
frequência que deu para cada número.
"""

from random import randint


def generator():

    return randint(1, 6)


def repeat(n):
	n1 = n2 = n3 = n4 = n5 = n6 = 0
	for values in range(n):
		amount = generator()

		if (amount == 1):
			n1 += 1
		elif(amount == 2):
			n2 += 1
		elif(amount == 3):
			n3 += 1
		elif(amount == 4):
			n4 += 1
		elif(amount == 5):
			n5 += 1
		else:
			n6 += 1

	print(f'Number 1: {(n1/n)*100:.1f}%')
	print(f'Number 2: {(n2/n)*100:.1f}%')
	print(f'Number 3: {(n3/n)*100:.1f}%')
	print(f'Number 4: {(n4/n)*100:.1f}%')
	print(f'Number 5: {(n5/n)*100:.1f}%')
	print(f'Number 6: {(n6/n)*100:.1f}%')
	print()
	print(f'Number 1: {n1}')
	print(f'Number 2: {n2}')
	print(f'Number 3: {n3}')
	print(f'Number 4: {n4}')
	print(f'Number 5: {n5}')
	print(f'Number 6: {n6}')


def menu():
	print()
	number = int(input('Number of plays: '))
	repeat(number)


while True:
    menu()
