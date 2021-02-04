#Função recebe um número e retorna o quadrado e o cubo dele.

def square(n):
	t1 = n ** 2
	print(f'{n} ^ 2 = {t1}.')
	
def cube(n):
	t2 = n ** 3
	print(f'{n} ^ 3 = {t2}.')

x = int(input('Number: '))
square(x)
cube(x)	