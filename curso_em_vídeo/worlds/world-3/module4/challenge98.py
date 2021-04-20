'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1;
b) de 10 até 0, de 2 em 2;
c) uma contagem personalizada.'''


## SCRIPT com FOR.	
from time import sleep

def count(i,f,c):
	if f < 0:
		f+=1
	if c < 0:
		c*= -1
	elif c < 0:
		c == 1

	if i < f:
		print()
		print('-'*20)
		print(f'Count from {i} to {f} of 1 and 1.')
		sleep(1)
		for c in range (i,f+1,c):
			print(f'{c}',end=' ', flush=True )
			sleep(0.5)
			
	else:
		if f <= 0:
			f-=1
		print()
		print('-'*20)
		print(f'\nCount from {i} to {f+1} of -2 and -2.')
		sleep(1)
		for c in range (i,f-1,-c):
			print(f'{c}', end = ' ', flush=True)
			sleep(0.5)
		
			

def personal():
	print('-'*20)
	print()
	print('Now it\'s your turn')
	x = int(input('Initial: '))
	y = int(input('Finally: '))
	z = int(input('Counter: '))
	count(x,y,z)
	print('-'*20)



			
#Main	
count(1,10,1)
count(10,0,-2)
personal()
print()
print()
print('FINISH!')