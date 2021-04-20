def increase(price, rate):
    x = price + (price * rate/100)
    return x


def decrease(price, rate):
    x = price - (price * rate/100)
    return x


def double(price):
    x = price * 2
    return x


def half(price):
    x = price / 2
    return x
