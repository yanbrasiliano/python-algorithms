"""1. Faça um programa que mostre todos os primos entre 1 e N sendo N um
número inteiro fornecido pelo usuário. 
2. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos;serão avaliados o funcionamento, o estilo e o número de testes (divisões)
executados."""

n = int(input('Number: '))

prime = []
for v in range(1,n+1):
	print(f'{v}')
	if n % v == 0:
		prime.append(v)

print(prime)
