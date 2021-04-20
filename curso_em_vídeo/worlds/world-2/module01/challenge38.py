# programa lerá 2 valores e dirá qual deles é maior ou se são iguais.

v1 = int(input('First value: '))
v2 = int(input('Second value: '))


first = v1
second = v2

if first > second:
    print('First value is greater than the second.')

elif second > first:
		print('Second value is greater than the first.')

else:
		print('The values are same.')
