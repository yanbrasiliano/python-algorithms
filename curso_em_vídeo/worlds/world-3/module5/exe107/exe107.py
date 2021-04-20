#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import coin

v = float(input('Enter a value in: R$ '))

print()
print(f'Value: R${v}')
print(f'Half the value: R${coin.half(v)}')
print(f'Double is: R${coin.double(v)}')
print(f'10% flat rate for increase. New value: R${coin.increase(v,10)}')
print(f'10% flat rate for decrease. New value: R${coin.decrease(v,10)}')

