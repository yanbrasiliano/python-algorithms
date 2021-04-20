#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

ordList = list()
for c in range(0, 5):
	n = int(input('Enter a value: '))
	if c == 0 or n > ordList[-1]:
		ordList.append(n)	
		print('Added to the end of the list.')
	else:
		pos = 0
		while pos < ordList[-1]:
			if n <= ordList[pos]:
				ordList.insert(pos,n)
				print(f'Added in the {pos} position of the list.')
				break
			pos+=1
print('\n')
print(f'The values entered, in order, are: {ordList}')

