numbers = []


for n in range(1,6):
	numbers.append(int(input(f'{n}° number: ')))

print(f'Max value in list: {max(numbers)} // Position: {numbers.index(max(numbers))}')
print(f'Min value in list: {min(numbers)} //	Position: {numbers.index(min(numbers))}')
