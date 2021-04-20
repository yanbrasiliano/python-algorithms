def read(msg):
	v = False
	while not v:
		x = str(input(msg))
		if x.isalpha():
			print(f'ERROR: {x} is not valid!')
		else:
			return float(x)