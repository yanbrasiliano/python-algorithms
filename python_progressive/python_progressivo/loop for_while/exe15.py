#15. A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.


print('*'*25)
print("~ Fibonnaci Sequence ~")
print('*'*25)

first = 0
second = 1


n = int(input('Number: '))

if n == 1 or n == 2:
	print('Result: 1')
else:	
	count = 3 
	while count <= n:
		term = first + second
		second = first
		first = term
		count +=1

		print(term)
