#Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import coin

v = float(input('Enter a value in: R$ '))

print()
print(f'Value: R${coin.coin(v)}')
print(f'Half the value: R${coin.coin(coin.half(v))}')
print(f'Double {coin.coin(v)} is: R${coin.coin(coin.double(v))}')
print(f'10% flat rate for increase. New value: R${coin.coin(coin.increase(v,10))}')
print(f'10% flat rate for decrease. New value: R${coin.coin(coin.decrease(v,10))}')

