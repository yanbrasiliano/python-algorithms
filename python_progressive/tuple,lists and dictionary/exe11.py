array = [[0,0,0],[0,0,0],[0,0,0]]

#Criando a Matriz
for l in range(0,3):  ## for para alimentar a matriz
	for c in range(0,3):

		array[l][c] = int(input(f'Enter a value for [{l}] [{c}]: '))

print()
print('-'*15)
for l in range(0,3):  ## for para mostrar a matriz de forma organizada.
	for c in range(0,3):
		print(f'[{array[l][c]:4^}]',end='')
	print()
print('-'*15)	

#A soma de todos os valores pares digitados.
par = 0
for l in range(0,3):  
	for c in range(0,3):
		if array[l][c] % 2 == 0:
			par +=array[l][c]

print(f'Total sum par: {par}')

#A soma dos valores da terceira coluna.
scolumn = 0
for l in range(0,3):  
	scolumn+= array[l][2]

print(f'Total Sum Column 3: {scolumn}')

#O maior valor da segunda linha.

print(f'Big value line 2: {max(array[1])}')