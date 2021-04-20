#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
n = (randint(1,21), randint(1,21), randint(1,21), 
		randint(1,21), randint(1,21))
print(f'Drawn values = {n}.')
print(f'Lower value: {min(n)}')
print(f'Highest value: {max(n)}')