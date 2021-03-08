"""
Faça um script que peça ao usuário o número de matérias da escola, ou
seja, um inteiro positivo.
Em seguida, ele vai digitando o valor de cada nota, de cada matéria e isso
será armazenado numa lista.
Ao final, seu script deverá fornecer a média geral do aluno.
"""

matter = int(input('Number of school materials: '))
notes = []
tot = 0
for i in range (matter):
	value = float(input(f'Enter your note at {i+1}° materials: '))
	tot+=value
	notes.append(value)

print(f'Total notes sum: {tot}') 
print(f'Average: {tot/matter}')

