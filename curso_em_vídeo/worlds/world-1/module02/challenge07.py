name = str(input('student name: '))
n0 = int (input('first overall note: '))
n1 =  int (input('second overall note: '))
media = (n0+n1)/2

print('The student {} has media : {:.2f}' .format(name,media))