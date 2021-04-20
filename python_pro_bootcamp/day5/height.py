## Calcute average height insert in a list.
students_heights=input('Input a list with a values: ').split() 
average=total=0
for v in range(0,len(students_heights)):
	students_heights[v]=float(students_heights[v])
	total+=students_heights[v]
	average=students_heights[v]/len(students_heights)
print(f'total sum values: {total:.2f} ')
print(f'average: {average:.2f}')
print(f'approaching the media: {round(average)}')