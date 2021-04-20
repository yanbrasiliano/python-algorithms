#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

#minha solução.
values = list()

for c in range(1,6):
	values.append(int(input(f'Enter {c}° value: ')))

print(f'You type the {values}.')
print(f'Highest value typed is {max(values)} and you position is {values.index(max(values))} in the list.')
print(f'Lower value typed is {min(values)} and you position is {values.index(min(values))} in the list.')

'''solução proposta pelo professor.
values = []
maior = menor = 0

for c in range(1,6):
	values.append(int(input(f'Enter {c}° value: ')))

	if c == 0:
		maior = menor = values[c]
	else:
		if values > maior:
			maior = values
		if values < menor:
			menor = values 
			
print(f'você digitou os valores {values}')
print(f'O maior valor digitado foi {maior} e o menor valor digitado foi {menor}.')
for i, v in enumerate(values):
	if v == maior:
		print(f'{i}...')
print()
	if v == menor:
		print(f'{i}...')
print()
			'''
