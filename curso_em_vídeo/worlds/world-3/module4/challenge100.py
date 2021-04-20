#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep
numbers = []

def draw(list):
	print('Sorting 5 values in the list: ', end=' ')
	for c in range (0,5):
		n = randint(1,50)
		numbers.append(n)
		print(f' {n} ',end='', flush=True)
		sleep(0.5)
		

draw(numbers)

def sumPar(list):
	s = 0 
	for v in numbers:
		if v % 2 == 0:
			s+=v
	print(f'\nTotal sum par in list {numbers} is {s}.')


sumPar(numbers)





