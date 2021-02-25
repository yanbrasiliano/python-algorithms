'''6. Desenvolva um programa que faça a tabuada de um número qualquer
inteiro que será digitado pelo usuário, mas a tabuada não deve
necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem
ser informados também pelo usuário.'''

first_num = int(input('Enter a first number in the range: '))
last_num =int(input('Enter a first number in the range: ')) 

for v in range(first_num,last_num+1,1):
	