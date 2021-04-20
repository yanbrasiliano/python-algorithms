# progama calculará o fatorial de um número com while/for/módulo factorial

'''
# fatorial com while.
from time import sleep

numero = int(input('Factorial of: '))
contador = numero
f = 1

print('Calculating factorial {}!......' .format(numero))
sleep(2)


while contador > 0:
	print('{}'.format(contador), end = '')
	print('x' if contador > 1 else '=', end = '')
	f *= contador
	contador -= 1
print('{}'.format(f))'''

# fatorial com lib math/module factorial
'''from math import factorial

numero = int(input('Factorial of: '))
f=factorial(numero)

print('Factorial of {} is {}'.format(numero,f))'''

'''
# fatorial com for
numero = int(input('Factorial of: '))
resultado=1

for n in range(1,numero+1):
    resultado *= n

print('Factorial of {} is {}' .format(numero,resultado)) '''
