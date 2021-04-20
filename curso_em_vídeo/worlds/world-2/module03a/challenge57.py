# script para validar dados por while.

n = str(input('Enter your gender[M/F]: ')).strip().upper()[0]

while n not in 'MF':
    n = str(input('Try again, unrecognized gender.Enter your gender: ')).strip().upper()

print('\n')
print('Registered!\nGender: {}.' .format(n))
print('\n')
