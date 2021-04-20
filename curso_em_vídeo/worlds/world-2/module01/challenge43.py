# programa para calcular imc
weight = float(input('Weight: '))
height = float(input('Height: '))

imc = weight/(height * height)

if imc <= 18.5:
    print('Under weight.')
elif imc <= 25:
    print('Ideal weight.')
elif imc <= 30:
		print('Overweight.')
elif imc <= 40:
		print('Obesity.')
elif imc > 40:
		print('Morbid Obesity.')