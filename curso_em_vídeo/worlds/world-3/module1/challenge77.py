# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

word = ('Pants', 'Car', 'Rude', 'Pencil', 'Group',
           'School', 'Bus', 'Green', 'Yellow', 'Orange')



for c in word:
	print(f'\nIn the word {c.upper()} we have the vowels ', end='')
	for letter in c:
		if letter.lower() in 'aeiou':
			print(letter,end='')

print('\n')

