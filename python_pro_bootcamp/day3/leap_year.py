""" 
Script to check if the year is a leap year. 
The year is a leap year if: 
1. Divisible by 4. Therefore, the division is exact with the remainder equal to zero; 
2. It cannot be divisible by 100. As a result, the division is not exact, that is, it leaves a remainder other than zero; 
3. It may be divisible by 400. If it is divisible by 400, the division must be exact, leaving the rest equal to zero.

"""

year = int(input('Typed an year: '))

if year % 4 != 0:
	print(f'{year} is not leap year.')
elif year % 4 == 0 or year % 400 == 0:
	print(f'{year} is leap year.')
else:
	print('ERROR.')