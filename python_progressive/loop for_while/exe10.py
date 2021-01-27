#10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
n1 = int(input('Enter a 1° value: ')) 
n2 = int(input('Enter a 2° value: ')) 

while n2 < n1:
	print('Try again, first number cannot be greater than second number.')
	n1 = int(input('Enter a 1° value: ')) 
	n2 = int(input('Enter a 2° value: ')) 
else:
	for c in range(n1,n2,1):
		print(f'{c}')
