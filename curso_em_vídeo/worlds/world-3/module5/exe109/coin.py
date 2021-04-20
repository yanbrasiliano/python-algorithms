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
	return f'{coin}{price}'.replace('.',',')