#Função para descobrir o maior e o menor  entre 3 números.

#function
def biggest(x,y):
	max = 0
	if y == 1:
		max = y
	else:
		if y > max:
			max = y
	return max

#function	
def smallest(x,y):
	min = 0
	if y == 1:
		min = y
	else:
		if y < min:
			min = y
	return min

#main
for c in range(0,3):
	x = int(input(f'Enter {c+1}° number: '))
	c+=1


print(f'The biggest is: {biggest(x,c)}')
print(f'The smallest is: {smallest(x,c)}')



