"""
A ideia inicial de uma pesquisa binária é substituir a pesquisa simples, mas como?
Numa pesquisa simples, com 50 possibilidades, o usuário teria que tentar 50 vezes até conseguir achar o valor exato. 
-
Numa pesquisa binária, a pesquisa é feita com o tempo logarítmico: 0(log n). Isso nos diz que as tentativas girariam em torno de de 5 a 8. Isso não é interessante?
-
Source: Entendendo Algoritmos - Aditya Y. """

#My Algorithm
from random import randint
machine = randint(0,50)
choice = 0
user = 0
while user != machine: 
	user = int(input('Your bet: '))
	choice+=1

	if user > machine:
		print('Entered value is higher.')
	elif user < machine:
		print('Entered value is less.')
	else:
		print('Entered value is correct.')
		print(f'Total attempts: {choice}')
		break 
#
#
#
"""
#Algorithm book.

def search_binary(list,item):
	lower = 0
	highest = len(list) - 1

	while lower <= highest:
		half = (lower + highest)/2
		attempt = list[half]
		if attempt == item:
			return half
		if attempt > item:
			highest = half - 1
		else:
			lower = half + 1
		return None

my_list = [1,3,5,7,9]
print (f'{search_binary(my_list,3)}')
print (f'{search_binary(my_list,-1)}')
"""