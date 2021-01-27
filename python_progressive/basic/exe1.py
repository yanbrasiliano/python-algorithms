#calcular perimetro e área do círculo.

import math


c = float(input('Enter value radius°: '))

p = 2 * c * math.pi

a = math.pi * c**2

print(f'Circumference Area: {a:.2f};\nPerimeter Area: {p:.2f}.')


