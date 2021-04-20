
#Exercício Python 67: Faça um script que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. v1.0 = EX9 e v2.0 = EX49
#from time import sleep

print('~'*15)
print('TABUADA v3.0')
print('~'*15)
while True:
	valor = int(input('What is value are you want multiply?\n[Enter a negative value to exit]: '))
	if valor < 0:
		print('Good bye, bro.')
		break
	for c in range(0,11):
		print(f'{valor} x {c} = {valor * c}')
	
	