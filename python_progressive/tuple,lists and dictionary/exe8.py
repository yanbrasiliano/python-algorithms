'''
Crie uma matriz 4 x 4 (ou seja, 4 linhas e 4 colunas, ou seja, 4 listas dentro
de uma lista maior).
Enxerte essa lista com números de 0, 1, 2, 3 etc
'''
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