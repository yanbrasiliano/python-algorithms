##programa lerá o primeiro termo e a razão de uma PA e mostrará os 10 primeiros termos de uma progressão.

p = int(input('Enter first PA term: '))
r = int(input('Enter reason PA: '))
ten = p + (10-1) * r

for c in range (p,ten,r):
	print('{}'.format(c))