#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

list = []
par = []
ímpar = []

while True: 
	list.append(int(input('Enter a value: ')))

	option = ' '
	while option not in 'YN':
		option = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
	if option == 'N':
			break


for v in enumerate(list):
	if v % 2 == 0:
		par.append(list)
	else:
		ímpar.append(list)

print(f'Values typed in the list are: {list}.')
print(f'The complete list par is {par}.')
print(f'The complete list par is {ímpar}.')