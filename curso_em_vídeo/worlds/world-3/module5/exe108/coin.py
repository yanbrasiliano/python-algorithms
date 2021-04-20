def increase(price=0, rate=0):
    x = price + (price * rate/100)
    return x


def decrease(price=0, rate=0):
    x = price - (price * rate/100)
    return x


def double(price = 0):
    x = price * 2
    return x


def half(price = 0):
    x = price / 2
    return x

def coin (price = 0, coin = 'R$'):
	return f'{coin}{price}'.replace('.',',')