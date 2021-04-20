# programa lerá as informações e dirá a categoria do aluno para a competição.
from datetime import date

name = str(input('Enter the name: '))
bt = int(input('Year of birth: '))


actually = date.today().year

age = actually - bt


if age <= 9:
    print('Name: {}\nCategoria Mirim.' .format(name))

elif age <= 14:
    print('Name: {}\nCategoria infantil.'.format(name))


elif age <= 19:
    print('Name: {}\nCategoria Junior.'.format(name))

elif age <= 24:
    print('Name: {}\nCategoria Sênior.'.format(name))

else:
    print('Name: {}\nCategoria Master.'.format(name))
