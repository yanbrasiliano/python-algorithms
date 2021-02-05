#Calcular o perimetro e a área do círculo com uma variável global.

pi = 3.14

def perimeter(radius):
	p = 2 * pi * radius
	print(f'Perimeter: {p}')

def area(radius):
	a = pi * (radius ** 2)
	print(f'Area: {a}')




r = float(input('Type the radius of the circumference: '))
perimeter(r)
area(r)