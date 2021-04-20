# programa lerá 3 números e mostrará o maior e o menor.
from time import sleep
x = int(input('\nEnter first number: '))
y = int(input('\nEnter second number: '))
z = int(input('\nEnter third number: '))

# verificar o menor número.
small = x

if y < x and y < z:
    small = y

if z < x and z < y:
    small = z

# verificar o maior número

big = x

if y > x and y > z:
    big = y

if z > x and z > y:
    big = z

print('\n')
print('\tAnalyzing...')
sleep(2)
print('\n')
print('The largest number is: {}' .format(big))
print('The smallest number is {}' .format(small))
