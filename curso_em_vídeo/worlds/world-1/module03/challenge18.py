# programa que calculará seno, cosseno e tangente de um ângulo usando a lib math.

from math import radians, tan, sin, cos
print('========== SEN / COS / TANG ========== ')
print('\n')
x = float(input('enter the angle value: '))


print('Sen: {:.2f} \nCos: {:.2f} \nTan: {:.2f}' .format(
    sin(radians(x)), cos(radians(x)), tan(radians(x)))) ## radians e para converter o valor do ângulo digitado para radiando, assim fazendo o cálculo de forma correta.
