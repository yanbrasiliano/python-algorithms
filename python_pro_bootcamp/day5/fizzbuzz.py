# The fizzbuzz job interview question coding.

for n in range(0, 60):
	# Divisible by both 3 and 5;
	if n % 3 == 0 and n % 5 == 0:
		print('Fizzbuzz')
	# Divisible by 3;
	elif n % 3 == 0:
		print('Fizz')
	# Divisible by 5;
	elif n % 5 == 0:
		print('Buzz')
	# General
	else:
		print(n)
