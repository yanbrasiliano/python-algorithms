#Exercício Python 65: Crie um script que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

from time import sleep
num = 0
cont = 0
soma = 0
negativo = 'N'
positivo = 'Y'
option = negativo = positivo
while option in 'Yy':
	num = int(input('Enter the number: '))
	option=str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
	cont +=1
	soma +=num
	media = soma/cont
	if cont == 1:
		maior=menor=num
	else:
		if num > maior:
				maior=num	
		if num < menor:
			menor = num
print('\n')
print('You type {} values,the media between the values is: {} and the largest number is {} and the smallest number is {}. '.format(cont,media,maior,menor))
print('\n')
print('Finishing...')
sleep(1)
print('Bye!')
sleep(1)
