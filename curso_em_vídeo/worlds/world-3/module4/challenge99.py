#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

#My script.
from time import sleep
def biggest(* n):
	count = 0
	count =+1
	x = max(n)

	print('-=-'*10)

	print(f'Analyzing the numbers {n}.', flush='True')
	sleep(1)

	print(f'Total numbers analyzed: {count}')

	sleep(1)
	print(f'biggest number is {x}.')
	print('-=-'*10)
	print()




#Main
biggest(5,4,3,2,1,10)
biggest(1,2,3)
biggest(4,55,1213243,4584,3333)

'''
#Script Guanabara
from time import sleep
def biggest(* n):
	count = big = 0
	count+=1
	print('\nAnalyzing the numbers...', flush=True)
	sleep(1)
	for value in n:
		print(f'{value}', end = ' ')
	if count == 0:
		big = value
	else:
		if value > big:
			big = value
	count+=1
	print(f'Total numbers: {count}')
	print(f'Biggest value is: {big}')	


#Main
biggest(5,4,3,2,1,10)
biggest(1,2,3)
biggest(4,55,1213243,4584,3333)
'''
