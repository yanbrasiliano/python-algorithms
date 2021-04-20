#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

y = [[],[]]
value = 0
for n in range(1,8):
	value = int(input(f'Enter value {n}: '))

	if value % 2 == 0:
		y[0].append(value)
	else:
		y[1].append(value)

print()
print('~=~'*20)
y[0].sort()
y[1].sort()
print(f'All values par {y[0]}')
print(f'All values ímpar {y[1]}')
print('~=~'*20)