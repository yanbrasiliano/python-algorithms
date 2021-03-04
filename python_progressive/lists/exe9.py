x  = []
y = []

for people in range(1,5):
	x.append(str(input('Name: ')))
	x.append(int(input('Age: ')))
	y.append(x[:])
	x.clear()

print(y)