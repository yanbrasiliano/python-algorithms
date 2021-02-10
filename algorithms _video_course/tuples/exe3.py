#TUPLE
def even(v):
	print('Even numbers is: ', end='')
	for even in v:
		if even % 2 == 0:
			print(f'{even} ',end='')
def three(v):
	if 3 in v:
		print()
		print(f'3 appeared {v.index(3)} times. ')
	else:
		print()
		print('3 was not typed.')
def nine(v):
		
		print(f'9 appeared {v.count(9)} times.')
v = (int(input('Enter the first number: ')),
		int(input('Enter the second number: ')),
		int(input('Enter the third numbers: ')),
		int(input('Enter the fourth numbers: ')))
print()
print(f'You type this numbers {v}.')
even(v)
three(v)
nine(v)



