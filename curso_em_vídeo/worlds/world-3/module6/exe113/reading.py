def readint(m):
	while True:
		try:
			n = int(input(m))
		except(ValueError,TypeError):
			print('\033[31mERROR.INVALID NUMBER; TRY AGAIN\033[m')
			continue
		except KeyboardInterrupt:
			print('\nData entry interrupted.')
			return 0
		else:
			return n	

def readfloat(m):
	while True:
		try:
			n = float(input(m))
		except(ValueError,TypeError):
			print('\033[31mERROR.INVALID NUMBER; TRY AGAIN\033[m')
			continue
		except KeyboardInterrupt:
			print('\nData entry interrupted.')
			return 0
		else:
			return n	
	