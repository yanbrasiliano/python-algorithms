'''36. Desenvolva um programa que faça a tabuada de um número qualquer
inteiro que será digitado pelo usuário, mas a tabuada não deve
necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem
ser informados também pelo usuário.'''


#entrando com os dados
main_num = int(input('Multiplication Table of: '))
first_num = int(input('Enter a first number in the range: '))
last_num =int(input('Enter a first number in the range: ')) 

if first_num > last_num: #teste lógico, caso o usuário digite o primerio valor maior que  o segundo.
	tmp = first_num # cria-se uma variável temporária para armazenar o valor digitado.
	first_num = last_num #valor digitado é enviado para variável correta, no caso, a varíavel que deve receber o maior número.
	last_num = tmp #variável com valor maior é igual a variável temporária, que no primeiro processo recebeu o maior número.

#loop para retornar resultado.
for v in range(first_num,last_num+1):
	print(f'{main_num} x {v} = {main_num*v}')


