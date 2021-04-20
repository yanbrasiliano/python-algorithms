#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘) 

def read(m):
	x = False
	value = 0 
	while True: 
		n=(str(input(m)))
		if n.isnumeric():
			value = int(n)
			x = True
		else:
			print('\033[0;31mERROR 101 - INVALID SYNTAX.\033[m')
		if x == True:
			break

	return value


n = read('Enter a number: ')
print(f'You typed {n}.')