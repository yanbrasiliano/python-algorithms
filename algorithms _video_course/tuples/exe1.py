#TUPLE


tuple = ('zero','one','two','three','four','five','six','seven','eight','nine','ten',
				'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen',
				'nineteen','twenty')
	
#Function
def extensive(x):	
	while True:
		if x < 0 or x > 20:
			print('ERROR 0 - Enter a number between 0 and 20.')
			x = int(input('Enter a number between 0 and 20: '))
		
		else:
			print(f'You typed {tuple[x]}')
			break		

	

#Main
n = int(input('Enter a number between 0 and 20: '))
extensive(n)	
	
