'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''
'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''
#SOLUÇÃO OTIMIZADA.
totalid = totalh = totalsex = 0

while True:
	print('~REGISTRATION OF PEOPLE~')
	idade = int(input('What is your age?[-]: '))
	sexo = ' '
	while sexo not in 'MF':
		sexo = str(input('Gender - [M/F]: ')).strip().upper()[0]
	if idade >= 18:
		totalid += 1
	if sexo == 'M':
		totalh+=1
	if sexo == 'F' and idade < 20:
		totalsex+=1
	opção = ' '
	while opção not in 'YN':
		opção = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
	if opção == 'N':
			break
print(f'There\'re {totalid} people with 18 years old.')
print(f'There\'re {totalh} men.')
print(f'There\'re {totalsex} women under the age 20.')


'''
#MINHA SOLUÇÃO
from time import sleep
contador = 0
totalsex = 0
opção = 'Y'
sexo = ' '
while True:
	idade = int(input('What is your age?[-]: '))
	contador += 1
	while sexo not in 'MF':
			print('\n')
			print('~REGISTRATION OF PEOPLE~')
			sexo = str(input('Gender - [M/F]: ')).strip().upper()[0]
			totalsex += 1
			while option not in 'YN':
				opção = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]


	if sexo == 'F' and idade < 20:
			print('\n')
			print(f'There\'re {contador} women under the age of 20.')
	else:
			print('\n')
			print('There\'re 0 women under the age of 20.')
	print(f'There\'re {contador} people with 18 years old.')
	print(f'There\'re {totalsex} men.')
	print('\n')
	print('Finishing...')
	sleep(1)
	print('Bye!')
	sleep(1)
'''