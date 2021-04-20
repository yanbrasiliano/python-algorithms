### programa para escolher o nome de forma aleatória usando a lib random.

from random import choice
print('========== Who is going to fall? ==========')
print('\n')
a1 = str(input('First student: ')) ## podemos usar o while/for, mas essa é a forma básica.
a2 = str(input('Second student: '))
a3 = str(input('Third student: '))
a4 = str(input('Fourth student: '))
print('\n')
list = [a1,a2,a3,a4] ## cria-se uma lista para conter quem vai participar; os nomes são os das variáveis.

x = choice(list)
print('\n')
print("Student chosen: {} " .format(x))
print('\n')