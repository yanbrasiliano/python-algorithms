# programa para análisar triâNGULOS versão 2.0

a = float(input('Enter first value: '))
b = float(input('Enter second value: '))
c = float(input('Enter third value: '))


# condição de existência e tipo do triângulo.

if a < b + c and b < a + c and c < a + b:
    print('The segments {}, {} and {} form a triangle' .format(a, b, c))
    if a == b == c:
            print('Type: EQUILATERAL TRIANGLE.')
    elif a != b != c:
            print('Type: SCALENE TRIANGLE')
    else:
        print('Type: ISOSCELES TRIANGLE.')


else:
    print('The segments {}, {} and {} not form a triangle' .format(a, b, c))
