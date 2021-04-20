# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

counter = ('zero', 'one', 'two', 'three', 'four',
                                        'five', 'six', 'seven', 'eight', 'nine',
                                        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen'
                                        'fiveteen', 'sixteen', 'seventeen', 'eighteen',
                                        'nineteen', 'twenty')


while True:
		n = int(input('Enter a number between 0 and 20: '))
		if n < 0 or n > 20:
			print('Invalid number. Try again!\n', end=' ')
		else:
			print(f'You type the number {counter[n]}.')
		r = ' '
		while r not in 'YN':
			r = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
		if r == 'N':
			break
print('Goodbye!')
