#Conversão de celsius para farenheit e vice-versa. F1: celsius - farenheit, F2: farenheit - celsius e F3 - Menu 


def celsius(f):
	c = (f - 32) * 5/9
	
	return c

def farenheit(c):
	f = (c*9/5)+32
	return f


def menu():
	while True:
		print('\t CONVERTER CELSIUS - FARENHEIT')
		print()
		option = int(input(''' 
1. Celsius to Farenheit
2. Farenheit to Celsius
3. Exit
\n
Option: '''))

		while option > 3 or option < 0:
			print('ERROR 100 - TRY AGAIN!')
			option = int(input('Option: '))
		if option == 3:
			print()
			print('Bye')
			break
		if option == 1:
			print()
			print('\tCELSIUS TO FARENHEIT')
			v = float(input('Enter a temeparature in celsius: '))
			print()
			x = farenheit(v)
			print(f'{x:.2f}F°')
		if option == 2:
			print()
			print('\tFARENHEIT  TO CELSIUS')
			v = float(input('Enter a temeparature in farenheit: '))
			print()
			y = celsius(v)
			print(f'{y:.2f}C°')




menu()

