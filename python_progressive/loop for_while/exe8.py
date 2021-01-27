#8. Faça um programa que leia 5 números e informe a soma e a média dos números. 

maior = menor = soma = media = 0

for c in range (1,6):
	n = int(input(f'Enter a {c}° number: '))
	soma+=n
	media = soma / 5
	if c == 1:
			maior = n
	else:
			if maior > n:
				maior = n
			if menor < n:
				menor = n

print(f'Highest value: {maior}.')
print(f'Lowest value: {menor}.')
print(f'Total sum: {soma}.')
print(f'Media: {media}.')