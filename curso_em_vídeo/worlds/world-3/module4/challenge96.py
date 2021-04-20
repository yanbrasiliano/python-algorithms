#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l,c):
	a = l * c 
	print(f'The area of a land  {l}x{c} is {a}m.')



print('Terrain Control')
print('='*20)
l = int(input('Enter a width: '))
c = int(input('Enter a length: '))
area(l,c)

