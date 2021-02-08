#Função para descobrir o maior e o menor  entre 3 números.

#function
def biggest(num,count):
	m = 0
	if count == 1:
		m = num
	else:
		if num > m:
			m = num
	

#function	
def smallest(num,count):
	n = 0
	if  count == 1:
		n = num
	else:
		if num < n:
			n = num
	print(f'The smallest number typed is: {n}')	

#main
for c in range(0,3):
	x = int(input(f'Enter {c+1}° number: '))
	c+=1


biggest(x,c)
smallest(x,c)




