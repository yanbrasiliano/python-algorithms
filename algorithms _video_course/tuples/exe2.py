#TUPLE

#Library
from random import randint
tuple = (randint(1,10),randint(1,10),randint(1,10),
				randint(1,10),randint(1,10))
#Function
def varied():
	print(f'Values = {tuple}')
	print(f'Max value = {max(tuple)}.')
	print(f'Min value = {min(tuple)}.')
#Main
varied()
