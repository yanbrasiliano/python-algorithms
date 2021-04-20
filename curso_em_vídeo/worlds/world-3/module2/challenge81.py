'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Leia:                                                                                                         A) Quantos números foram digitados.                                                                                                    B) A lista de valores, ordenada de forma decrescente.                                                                                         
C) Se o valor 5 foi digitado e está ou não na lista.'''

counter = 0 
orderlist = list()
x = 0

while True:
	orderlist.append(int(input('Enter a value: ')))
	counter+=1
	
	option = ' '
	while option not in 'YN':
		option = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
	if option == 'N':
			break

print('~=~'*30)
print(f'{counter} values typed.')
print(f'{orderlist} values typed.')
orderlist.sort(reverse=True)
print(f'{orderlist} values typed in descending order.')

if 5 in orderlist:
	print(f'Number 5 is on the list.')
else:
	print('Number 5 is not on the list.')