def increase(price=0, rate=0, format =False):
    x = price + (price * rate/100)
    return x if format is False else coin(x)


def decrease(price=0, rate=0, format = False):
    x = price - (price * rate/100)
    return x if format is False else coin(x)


def double(price = 0, format = False):
    x = price * 2
    return x if format is False else coin(x)


def half(price = 0, format = False):
    x = price / 2
    return x if format is False else coin(x)

def coin (price = 0, coin = 'R$'):
	return f'{coin}{price:>.2f}'.replace('.',',')


def resume(price = 0, rateA = 10, rateB=10):
	print('*'*30)
	print('Overview Values'.center(30))
	print('*'*30)
	print('')
	print(f'Price Analyzed:\t\t{coin(price)}')
	print(f'Double {coin(price)}:\t\t{double(price,True)}')
	print(f'Half {coin(price)}:\t\t{half(price,True)}')
	print(f'{rateA}% increase:\t\t{increase(price,rateA,True)}')
	print(f'{rateB}% decrease:\t\t{decrease(price,rateB,True)}')
	print('*'*30)