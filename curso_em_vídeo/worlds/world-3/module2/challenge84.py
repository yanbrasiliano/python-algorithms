''' Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.  
C) Uma listagem com as pessoas mais leves.'''

people = []
new = []
max = min = 0

while True:
	people.append(str(input('Name: ')))
	people.append(float(input('Weight: ')))

	
	if len(new) == 0:
		max = min = people[1]
	else:
		if people[1] > max:
			max = people[1]
		if people[1] < min:
			min = people[1]
	
	new.append(people[:])
	people.clear()
		
	option = ' '
	while option not in 'YN':
		option = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
	if option == 'N':
			break
print()
print('*'*35)
print(f'Total Registered {len(new)}.')
print(f'Highest weight: {max}kg - ', end='')
for p in new:
	if p[1] == max:
		print(f'User: [{p[0]}]')
print()
print(f'Lower weight: {min}kg - ', end='')
for p in new:
	if p[1] == min:
			print(f'User: [{p[0]}]', end='')
print()
print('*'*35)
		
