#Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import coin

v = float(input('Enter a value in: R$ '))

print()
print(f'Value: {coin.coin(v)}')
print(f'Half the value: {coin.half(v,True)}')
print(f'Double {coin.coin(v)} is: {coin.double(v,True)}')
print(f'10% flat rate for increase. New value: {coin.increase(v,10,True)}')
print(f'10% flat rate for decrease. New value: {coin.decrease(v,10,True)}')

