'''
Faça um script que pede um número inteiro positivo ao usuário.
Em seguida, cria uma lista com igual número de itens, onde o primeiro termo
é 1!, o segundo é 2!, o terceiro é o valor de 3!, etc, até o termo que ele
digitou. Ou seja, se digitou n, vai exibir até o termo de índice n-1, e lá na lista
vai ter o valor de (n-1)!.
'''

number = int(input('Factorial of: '))
fat = [1]

for values in range(1,number):
	term = fat[values - 1] * values
	fat += [term]
print(fat)