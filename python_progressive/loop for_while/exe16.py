#Exercício 16 - Apostíla Python Progressivo

print('*'*25)
print("~ Fibonnaci Sequence ~")
print('*'*25)

n = int(input('Number: '))
last = 1
penultimate = 1

if n == 1 or n == 2:
	print('Result: 1')
else:	
	count = 3 
	while count <= n:
		term = last + penultimate
		penultimate = last
		last = term
		count +=1

	print(term)
