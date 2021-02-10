#98) Crie um programa que tenha uma função SuperSomador(), que vai receber dois números como parâmetro e depois vai retornar a soma de todos os valores no intervalo entre os valores recebidos. 

def gap(x,y):
	s = 0 
	for c in range (x,y+1,1):
		s +=c


	print(f'Sum of the interval between {x} and {y} is {s}.')






a = int(input('Enter first value: '))
b = int(input('Enter second value: '))
gap(a,b)