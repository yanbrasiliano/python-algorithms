#Exercício 14 - Apostíla Python Progressivo
totp = toti = 0

for n in range(0,10):
	x = int(input(f'Enter {n+1}° number: '))
	while x < 0:
		print('try again; number doens\'t negative.')
		x = int(input(f'Enter {n+1}° number: '))
	if x % 2 == 0:
		totp+=1
	elif x % 2 == 1:
		toti+=1
print('~'*30)
print(f'Numbers typed par is: {totp};\nNumbers typed ímpar is: {toti}.')
