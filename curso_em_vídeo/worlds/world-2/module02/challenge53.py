#verifica se a frase é um palíndromo.

phrase = str(input('Enter the phrase: ')).strip().upper()
w = phrase.split()
wf = ''.join(w)
x = ''

for c in range (len(wf) - 1, -1, -1): ## poderia ser substituído por um fatiamento de string. ficaria: x = wf[::-1]
	x += wf[c]
if x == wf:
	print('There are Palindrómo!\nPhrase:{}\nPalindrómo:{}'.format(wf,x))
else:
	print('Phrase not is Palindrómo!\nPhrase:{}\nResult:{}'.format(wf,x))