#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

import reading
x = reading.readint('Enter a int number: ')
y = reading.readfloat('Enter a float number: ')
print(f'You typed {x}.')
print(f'You typed {y}.')

