#6. Crie uma função que recebe um inteiro positivo e teste para saber se ele é primo ou não. Faça um script que recebe um inteiro n e mostra todos os primos, de 1 até n.


def prime(n):
	while True:
		for v in range(2,n):
			if n % 2 == 0 and n != 2:
				return False
		return True

def show():
	n = int(input('Show range to value: '))
	for v in range(2,n+1):
		if (prime(v)):
			print(f'{v}->',end=' ')



while True:
	show()
