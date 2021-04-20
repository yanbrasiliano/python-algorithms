# calcular hipotenusa com lib math; sabendo que a formula é h² = (C.O)² + (C.A)², mais conhecido como teorema de pitágoras.

from math import hypot
print('===== PYTHAGOREAN THEOREM =====')
print('\n')
x = float(input('enter value opposite side: '))
y = float(input('enter value adjacent side: '))
print('\n')
print('========== RESULT ==========')
print('\n')
print('the value of the hypotenuse is: {:.2f}' .format(hypot(x,y)))
print('\n')
