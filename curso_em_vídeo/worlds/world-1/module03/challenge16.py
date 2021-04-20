## lê um número float e retornar sua porção inteira ints

from math import trunc

n = float(input('hi! enter the number: '))

print('the value you entered was {} and its entire portion is {}' .format(n, trunc(n)))