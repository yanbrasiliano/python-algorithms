#APOSTILA PYTHON PROGRESSIVO

# LETRA DIGITADA É VOGAL OU CONSOANTE.

w = str(input('Enter a letter: ')).strip().upper()[0]

if w == 'A' or w == 'E' or w == 'I' or w == 'O' or w == 'U':
	print('This letter is vowel.')
else:
	print('This letter is consonant.')
