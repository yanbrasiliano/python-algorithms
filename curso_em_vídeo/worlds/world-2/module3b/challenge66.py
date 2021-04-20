#Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

from time import sleep
num = cont = soma = 0
while num != 999:
	num = int(input('Enter the number[type 999 for stop the count]: '))
	if num == 999:
		break
	cont +=1
	soma +=num
print('\n')
print(f'You type {cont} values and the sum between numbers is: {soma}. ')
print('\n')
print('Finishing...')
sleep(1)
print('Bye!')
sleep(1)
