import random
import secrets
l = ['!','#','%','&']
x = random.randint(0,15)
y = random.choice(l)
for c in range (0,x):
	print(f'{x}{y}',end='')
