## programa para calcular o valor a se pagar de um carro alugado; baseado no km rodado x dias alugados.

day = int(input('rented days: '))
km = float(input('km traveled: '))

car = 60
x = 0.15
print('total pay is R${}'.format((car*day) + (km * x)))