#4. A probabilidade de dar um valor em um dado é 1/6 (uma em 6). Faça um script em Python que simule 1 milhão de lançamentos de dados e mostre a frequência que deu para cada número.

from random import randint

def genarator():
	return randint(1,6)

def repeat(n):
	a = b = c = d = e = f = 0
	for v in range(n):
		x = genarator()
		if x == 1:
			a+=1
		elif x == 2:
			b+=1
		elif x == 3:
			c+=1
		elif x == 4:
			d+=1
		elif x == 5:
			e+=1
		else:
			f+=1


	print(f'NUMBER 1 {(a/n)*100}%')
	print(f'NUMBER 2 {(b/n)*100}%')
	print(f'NUMBER 3 {(c/n)*100}%')
	print(f'NUMBER 4 {(d/n)*100}%')
	print(f'NUMBER 5 {(e/n)*100}%')	
	print(f'NUMBER 6 {(f/n)*100}%')

def menu():
	n = int(input('Number of moves: '))
	repeat(n)
	


while True: 
	menu()
	