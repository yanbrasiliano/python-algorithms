#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

def h(c):
	help(c)


def title(msg):
	t = len(msg) + 4 
	print('*'*t)
	print(msg)
	print('*'*t)

#Main
command = ' '
while True:
	title('PYHELP QUERY SYSTEM')
	command = str(input('Library Function: '))
	
	if command.upper() == 'FINISH':
		break
	else:
		h(command)
