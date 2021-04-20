#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média


dates = dict()
people = list()
s = m = 0
## capturando dados
while True: 
	dates.clear()
	dates['name'] = str(input('Name: ')).strip().upper()
	while len(dates['name'])< 0:
		print('TRY AGAIN!\nName must be longer than 0 characters!')	
		dates['name'] = str(input('Name: ')).strip().upper()
	
	dates['gender'] = str(input('Gender [M/F]: ')).strip().upper()[0]
	while dates['gender'] not in 'MF':
		print('TRY AGAIN!\nEnter the gender MALE OR FEMALE [M/F]')
		dates['gender'] = str(input('Gender [M/F]: ')).strip().upper()[0]

	dates['age'] = int(input('Age: '))
	while dates['age'] <= 0:
		print('TRY AGAIN!\nAge needs to be longer than 0.')
		dates['age'] = int(input('Age: '))
	s+=dates['age']

	people.append(dates.copy())
	option = ' '
	while option not in 'YN':
		option=str(input('CONTINUE? [Y/N]')).strip().upper()[0]
	if option == 'N':
		break

print(f'A- Total people registered: {len(people)}.')
media = s / len(people)
print(f'B - Age media: {media:.2f}')

cont = 0
for p in people:
	if p['gender'] in 'Ff':
		cont+=1
print(f'C - Total girls is: {cont} ')
print('D - People over average ages')
for p in people:
    if p['age'] >= m:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()