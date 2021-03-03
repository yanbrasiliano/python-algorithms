#Faça um script que cria uma lista de 10 elementos, preenchendo eles de 0 até 9, usando laço for. Depois, print essa lista.

list = []

for values in range(10):
	list.append(values)
for values in list:
	print(f'{values}')
	#sum+=values
print(f'Total: {sum(list)}')
