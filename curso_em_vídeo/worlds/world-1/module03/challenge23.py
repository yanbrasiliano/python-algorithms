## programa lerá um número e entregará ele por extenso em unidade, dezena, centena e milhar.

# strip = retira os espaços de antes e depois.
n = int(input('Enter with a number: ')).strip()
##n = str(num)

print('\nAnalyzing the number...\n')

# // = divisão inteira ; a lógica é: divide o número e pega seu resto e divide por 10;o resultado é a unidade. O mesmo equivale para todos os outros.
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Thousand: {}.' .format(u))
print('Hundred: {}.' .format(d))
print('Dozen: {}.' .format(c))
print('Unit: {}.' .format(m))
