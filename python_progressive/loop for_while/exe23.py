"""1. Faça um programa que mostre todos os primos entre 1 e N sendo N um
número inteiro fornecido pelo usuário. 
2. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos;serão avaliados o funcionamento, o estilo e o número de testes (divisões)
executados."""


n = int(input('Enter a value: '))
t = 0
for c in range(1, n+1):
    if n % c == 0:
      t += 1
    else:
        print(f'\033[35m',end='')
    print(f'{c} ', end=' ')
print(f'\n\033[33m{n} divisible {t} times.\033[33m')

if t == 2:
    print('\nIt is prime')
else:
    print('\nDo not prime.')



