"""25. Faça um programa que peça para n pessoas a sua idade, ao final o
programa devera verificar se a média de idade da turma varia entre 0 e 25,26
e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa,
conforme a média calculada."""
t = 0
m = 0 

for i in range(1,6):
	n = int(input(f'Enter a {i}° age: '))
	
	t +=n
	m+=1

x = t/m

print(f'Average: {x}')
if x > 0 and x < 25:
	print('CLASS A.')
if x > 25 and x < 60:
	print('CLASS B.')
if x > 60:
	print('CLASS C.')