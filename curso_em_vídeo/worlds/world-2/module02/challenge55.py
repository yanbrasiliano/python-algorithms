# programa lerá o peso de 5 pessoas e dirá qual o maior e qual o menor peso.
maior = 0
menor = 0


for c in range(1, 6):
    peso = float(input('Enter the height {}° person: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('The bigest height is: {}kg '.format(maior))
print('The smallest height is: {}kg '.format(menor))