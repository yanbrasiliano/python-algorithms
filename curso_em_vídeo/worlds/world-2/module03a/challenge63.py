# Calculadora Fibonacci
# Fibonnaci Calculator simula o cálculo fibonnaci, que funciona da seguintes forma: começa do 0 e 1, e os números seguintes são a soma do anterior com o atual, fazendo um sequencial.

print('*'*25)
print("Fibonnaci Calculator v1.0")
print('*'*25)


n = int(input('Enter the number to be calculated: '))

t1 = 0
t2 = 1

print('-'*25)
print('{} -> {}'.format(t1, t2), end='')
count = 3

while contador <= n:
	t3 = t1 + t2
	print(' -> {}' .format(t3), end='')
	t1 = t2
	t2 = t3
	count += 1


print(' -> Finish!')
print('-'*25)