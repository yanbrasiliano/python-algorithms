# programa para escolher o nome de forma aleatória e a ordem, tudo isso usando a lib random.

from random import choice
print('========== Who is going to fall? ==========')
print('\n')
# podemos usar o while/for, mas essa é a forma básica.
a1 = str(input('First student: '))
a2 = str(input('Second student: '))
a3 = str(input('Third student: '))
a4 = str(input('Fourth student: '))
print('\n')
# cria-se uma lista para conter quem vai participar; os nomes são os das variáveis.
list = [a1, a2, a3, a4]

n1 = 1°
n2 = 2°
n3 = 3°
n4 = 4°

list1 = [n1, n2, n3, n4]


x = choice(list)
y = choice(list1)
print('\n')
print("Student: {}{} " .format(y,x))
print("Student: {}{} " .format(y,x))
print("Student: {}{} " .format(y,x))
print("Student: {}{} " .format(y,x))
