#16.A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.



print('*'*25)
print("~ Fibonnaci Sequence ~")
print('*'*25)

last = 1
penultimate = 1
print(last)
print(penultimate)
term = 0

while term < 500:
		term = last + penultimate
		penultimate = last
		last = term

		if term < 500:
			print(term)
		else:
			print('ERROR')
