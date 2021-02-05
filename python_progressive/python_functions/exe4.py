#Função para descobrir o maior entre 3 números.

#function
def biggest(num,count):
	m = 0
	if  count == 1:
		m = num
	else:
		if num > m:
			m = num
	print(f'The largest number typed is: {m}')	
	

#main
for c in range(0,3):
	x = int(input(f'Enter {c+1}° number: '))
	c+=1

biggest(x,c)




