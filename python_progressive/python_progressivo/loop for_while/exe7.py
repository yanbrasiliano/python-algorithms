#7. Faça um programa que leia 5 números e informe o maior número.

maior = menor = 0

for c in range (1,6):
	n = int(input(f'Enter a {c}° number: '))
	if c == 1:
			maior = n
	else:
			if maior > n:
				maior = n
			if menor < n:
				menor = n

print(f'Highest value: {maior}.')
print(f'Lowest value: {menor}.')
