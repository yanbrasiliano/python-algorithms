#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas – A maior nota – A menor nota – A média da turma  – A situação (opcional)

def note(*n,situation=False):
	r = dict()
	r['Total: '] = len(n)
	r['Greater: '] = max(n)
	r['Smaller: '] = min(n)
	r['Average: '] = sum(n)/len(n)

	if 	r['Average: '] >= 7:
		print('\033[1:34mOK!\033[m')
	elif 	r['Average: '] >= 5:
		print('\033[1:35mMore os Less!\033[m')
	else: 
		print('\033[1:31mVery bad!\033[m')

	return r

#Main

answer = note(5.5,4,8,2,3,situation=True)
print(answer)