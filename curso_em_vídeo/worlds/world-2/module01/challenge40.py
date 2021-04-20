# programa lerá os dados e dirá se o aluno está aprovado ou reprovado.

name = str(input('Name: '))
note1 = float(input('First note: '))
note2 = float(input('Second note: '))

average = (note1+note2)/2

if average >= 7: 
	print('Congratulations {}, you was approved!' .format(name))
elif average >=5 | average <= 6.9:
	print('{}, are in recovery.' .format(name))
elif average < 5:
	print("{}, are reproved." .format(name))