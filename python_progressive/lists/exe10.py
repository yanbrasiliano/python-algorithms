person  = []
people = []
mai = men = tot = 0
while True: 
	person.append(str(input('Name: ')))
	person.append(float(input('Weight: ')))
	if len(person) == 0:
		mai = men = 0
	else:
		if person[1] > mai:
			mai = person[1]
		if person[1] < men:
			men = person[1]
	people.append(person[:])
	person.clear()
	
	option = ' '
	while option not in 'YN':
		option = str(input("CONTINUE? [Y/N]")).upper().split()[0]
	if option == 'N':
		break
print(f'Registered: {len(people)}')
print(f'Greater Weight: {max(people)}')
print(f'Smallest Weight: {min(people)}')
