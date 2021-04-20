'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

v = (int(input('Enter the first number: ')),
		int(input('Enter the second number: ')),
		int(input('Enter the third numbers: ')),
		int(input('Enter the fourth numbers: ')))

print(f'You type this numbers {v}.')

print(f'9 appeared {v.count(9)} times.')

if 3 in v:
	print(f'3 appeared {v.index(3)} times. ')
else:
	print('3 was not typed.')

print('Numbers Pars are: ',end='')
for par in v:
	if par % 2 == 0:
	 print(par, end ='')


