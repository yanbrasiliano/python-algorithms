# programa lerá um número e dirá se ele é par ou ímpar.

x = int(input('Enter the number: '))


if x % 2 == 0:
    print('The number {} is even.' .format(x))
else:
    print('The number {} is odd.' .format(x))
