#9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

for c in range(1,51):
	if c % 2 == 1:
		print(f'[{c:^3}]',end='')