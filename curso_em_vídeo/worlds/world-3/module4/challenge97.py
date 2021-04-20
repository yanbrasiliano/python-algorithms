#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def write(msg):
	t = len(msg)+5
	print('-'*t)
	print(f'{msg}')
	print('-'*t)


write('Hello, bro.')
write('I am yan.')
write('This is my first experience with function.')