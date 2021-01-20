#1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 

while True:
	n = int(input('Enter a value between 0 - 10: '))
	if n <= 10:
		print(f'typed {n}, accepted.')
		break
	else:
		print('try again!') 
