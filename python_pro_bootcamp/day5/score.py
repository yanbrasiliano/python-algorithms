## Calculate highest score in a list.
students_scores=input('Input a list with a values: ').split()
max=min=score=0
for v in range(0,len(students_scores)):
	students_scores[v]=int(students_scores[v])
			
print(f'List: {students_scores}')

for score in students_scores:
	if score > max:
		max = score
	elif score < max:
		min = score

print(f'Highest value: {max}\nLowest value: {min}')

