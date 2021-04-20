# programa lerá a velocidade e dirá se o user vai ser multado ou não.

print('\tELECTRONIC RADAR\n')
vel = float(input('Enter the speed: '))

x = 7
if vel > 80:
    print('YOU HAVE BEEN FINED!\nValue: R${:.2f}' .format((vel-80)*7))
else:
    print('Have a good day, you can go!')
	