#Este script lerá uma frase e um caractere e dirá quantas vezes esse caractere aparece na frase.
def count_char(phrase,char):
	c = 0
	for letter in phrase:
		if letter == char:
			c+=1
	print(f'{char} appeared {c} time(s) in the phrase.')



p = str(input('Phrase: ')).strip().upper()
c = str(input('Charactere: ')).strip().upper()

count_char(p,c)
