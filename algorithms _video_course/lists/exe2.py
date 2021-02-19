#LISTS - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


v = []

while True:
	x = int(input('Enter a value: '))
	if x not in v:
		print('ADDED NUMBER.')
		v.append(x)
	else:
		print('Try Again!The number has already been entered. ')	

	r = ' '
	if r not in 'YN':
		r = str(input('CONTINUE? Y/N: ')).strip().upper()[0]
	if r == 'N':
		break

print(v)
print(sorted(v))	

