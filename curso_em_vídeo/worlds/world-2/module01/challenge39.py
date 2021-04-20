# programa lerá as informações do cadastrado e dirá sua situação com alistamento.

from datetime import date

name = str(input('NAME: '))
yr = int(input('YEAR OF BIRTH: '))


x = 18
atual = date.today().year
age = atual - yr

print('{}, you were born in {} and you have {} in {}' .format(name,yr,age,atual))
if age == 18:

    print('Report to the nearest military base.')

elif age < 18:

    print('You don\'t need to introduce yourself yet.\nYou still have {} years to perform.' .format(x - age))

elif age > 18:

    print('You are indebted to the union for {} years, if you present the nearest military base.' .format(age - x))
