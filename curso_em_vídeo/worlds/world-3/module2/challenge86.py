#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

array = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):  ## for para alimentar a matriz
	for c in range(0,3):

		array[l][c] = int(input(f'Enter a value for [{l}] [{c}]: '))

print()
print('-'*15)
for l in range(0,3):  ## for para mostrar a matriz
	for c in range(0,3):
		print(f'[{array[l][c]:4^}]',end='')
	print()
print('-'*15)	