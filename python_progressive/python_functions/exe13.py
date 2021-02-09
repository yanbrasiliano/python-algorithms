#7. Um número é dito perfeito quando ele é igual a soma de seus fatores. Por exemplo, os fatores de 6 são 1, 2 e 3 (ou seja, podemos dividir 6 por 1, por 2 e por 3) e 6=1+2+3, logo 6 é um número perfeito. Escreva uma função que recebe um inteiro e dizer se é perfeito ou não. Em outra função, peça um inteiro n e mostre todos os números perfeitos até n.

def perfect(nb):
	s = 0
	for c in range(1,nb):
		if nb % c == 0:
			s += c
	if s == nb:
		return True
	else:
		return False

def show():
	x = int(input('Display perfect numbers up to: '))

	for c in range(1,x + 1):
		if (perfect(c)):
			print(f'{c}')

while True:
	show()
