def factorial(n=1):
	f = 1 
	for c in range(n,0,-1):
		f*=c
	return f 

x = int(input('enter a first number to calculate the factorial: '))
y = int(input('enter a second number to calculate the factorial: ')) 
print(f'The factorial of the number {x} is {factorial(x)}.\nThe factorial of the number {y} is {factorial(y)}.')