#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

#FUNCTION
def vote(year):
	"""
	year: variável para receber ano de nascimento.
	current: ano atual.
	age: idade do usuário.
	"""
	from datetime import date, datetime
	current = date.today().year
	age = current- year 
	if age < 15:
		return f'With {age} years old: DENIED!'
	elif age <= 16 or age < 18:
		return f'With {age} years old: OPTIONAL!'
	else:
		return f'With {age} years old: OBLIGATORY!'




#MAIN
y = int(input("Year of birth:  "))
print(vote(y))


