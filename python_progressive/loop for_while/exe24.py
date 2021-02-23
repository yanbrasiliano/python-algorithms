#24. Faça um programa que calcule o mostre a média aritmética de N notas.
t = 0
m = 0

for n in range(1,6):
	n = float(input(f'Enter a {n}° note: '))
	t +=n
	m+=1

x = t/m

print(f'Average: {x}')

	
	