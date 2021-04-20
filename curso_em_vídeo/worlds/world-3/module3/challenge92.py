# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
worker = dict()
actually = date.today().year

worker['name'] = str(input('Name: '))
worker['age'] = int(input('Year of birth: '))
while worker['age'] < 0:
    print('Try Again, age cannot less than 0.')
    worker['age'] = int(input('Year of birth: '))
worker['ctps'] = int(input('CTPS[O - Don\'t have.]: '))
while worker['ctps'] < 0:
    print('Try Again, CTPS cannot less than 0.')

worker['gender'] = str(input('Gender[M/F]: ')).upper().split()

'''while worker['gender'] != 'MF':
    worker['gender'] = str(input('Gender[M/F]: ')).upper().split()
    print('Try Again, the accepted genders are male and female[M or F].'''

if worker['ctps'] == 0:
    print()
    print('-=-'*20)
    print(f'Name is {worker["name"]}.')
    print(f'Age:{actually - worker["age"] }.')
    print('CTPS: It\'s not registered.')
elif worker['ctps'] != 0:
    worker['hire'] = int(input('Year of hiring: '))
    worker['salary'] = float(input('Salary:$ '))
    print()
    print('-=-'*20)
		
    # for k,v in worker.items():
    if worker['gender'] == m:
        print(f'Retirement: {worker["age"] + m}.')
    elif worker['gender'] == f:
        print(f'Retirement: {worker["age"] + f}.')

    print(f'Name is {worker["name"]}.')
    print(f'Age:{actually - worker["age"] }.')
    print(f'CTPS Number: {worker["ctps"]}.')
    print(f'Year of hiring: {worker["hire"]}')
    print(f'Salary is: ${worker["salary"]}.')


'''option = ' '
while option not in 'YN':
	print('CONTINUE? [Y/N]: ')
	if option == 'N':
		break'''
