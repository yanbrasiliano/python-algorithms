##programa lerá 3 valores e dirá se ele pode ser uma triângulo ou não.
## A condição existente de um triângulo é: a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas.

a = float(input('Enter first value: '))
b = float(input('Enter second value: '))
c = float(input('Enter third value: '))


## condição de existência

if a < b + c and b < a  + c and c < a + b:
	print('The segments {}, {} and {} form a triangle' .format(a,b,c))

else:
	print('The segments {}, {} and {} not form a triangle' .format(a,b,c))