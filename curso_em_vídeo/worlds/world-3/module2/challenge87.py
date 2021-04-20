''' Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.  
C) O maior valor da segunda linha.'''

array = [[0,0,0],[0,0,0],[0,0,0]]
par = scolumn = mline = 0
for l in range(0,3):  ## for para alimentar a matriz
	for c in range(0,3):
		array[l][c] = int(input(f'Enter a value for [{l}] [{c}]: '))
print()
print('-'*15)
for l in range(0,3):  ## for para mostrar a matriz
	for c in range(0,3):
		print(f'[{array[l][c]:5^}]',end='')
		if array[l][c] % 2 == 0: ## if para somar valores pares da matriz.
			par+= array[l][c]
	print()
print('-'*15)	
print(f'A - List sum VALUES par: {par}.') #resultado par.
for l in range (0,3): ## for para somar valores da terceira coluna.
	scolumn += array[l][2]
print('-'*15)		
print(f'Sum values of the column third is: {scolumn}')
for c in range (0,3): ## for para somar valores da terceira coluna.
	if c == 0:
		mline = array[1][c]
	elif c > mline:
		mline = array[1][c]
print('-'*15)
print(f'The biggest value second line is {mline}.')

