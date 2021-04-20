# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

# from math import factorial #

def fact(n, show=False):
    #	factorial(n) #
	f = 1
	for c in range(n, 0, -1):
	
		if show:
			print(c, end ='')			
			if c > 1:
				print(' x ', end='')
		else:
			print(' = ', end='')
		f *= c
	return f


num = int(input('Enter a number to calculate the factorial: '))
print(fact(num, show=True))
