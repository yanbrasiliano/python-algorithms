'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''


print('~FAST BOX - 24 HOURS BANK ~')
print('Available ballots: R$50, R$20, R$10 and R$1 ')
valor = int(input('What value do you want to withdraw?'))
total = valor
montante = 0 
cédula = 50

while True:
	if total >= cédula:
		total-=cédula
		montante+=1
	else:
		if montante > 0:
			print(f'total {montante} of ballots of {cédula} ')
		if cédula == 50:
			cédula = 20
		elif cédula == 20:
			cédula = 10
		elif cédula == 10:
			cédula = 1
			montante == 0
		if total == 0:
			break
		