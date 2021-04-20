## script para ler vários números e calcular a sua sequência; parar quando digitar o 999 e mostrar = cálculo e quantidade de números digitados.
from time import sleep
num = cont = soma = 0 
num = int(input('Hello, enter the first number[ENTER 999 to STOP]: '))
while num != 999:
	soma += num
	cont += 1
	num = int(input('Hello, enter the first number[ENTER 999 to STOP]: '))
print('You type {} numbers and the sum is {}.' .format(cont, soma))
print('Finishing...')
sleep(1)
print('Bye!')
sleep(1)
