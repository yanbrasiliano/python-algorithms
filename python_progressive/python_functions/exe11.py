#5. A série de Fibonacci é uma sequência de números, cujos dois primeiros são 0 e 1. O termo seguinte da sequência é obtido somando os dois anteriores. Faça uma script em Python que solicite um inteiro positivo ao usuário, n. Então uma função exibe todos os termos da sequência até o nésimo termo. Use recursividade.


def fibonacci(n):
	while True:
		if n == 1:
			return 0
		elif n == 2:
			return 1
		elif n < 1:
			break
		else:
			return fibonacci(n-1) + fibonacci(n-2)

def menu():
	x = int(input('Enter a number to calculate Fibonnaci Serie[term greater than 2]: '))
	fibonacci(x)
	for v in range(1,x+1):
		print(f'{fibonacci(v)} --- ', end='')

menu()
