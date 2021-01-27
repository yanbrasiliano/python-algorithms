'''3. Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';'''

name = str(input('Name: '))
while len(name) < 3:
	print('TRY AGAIN!\nName must be longer than 3 characters!')	
	name = str(input('Name: '))

age = int(input('Age: '))
while age > 150 or age <= 0:
	print('TRY AGAIN!\nAge needs to be between 0 and 150.')
	age = int(input('Age: '))

salary = float(input('Salary:$ '))
while salary <=0:
	print('TRY AGAIN!\nSalary needs to be higher than 0.')
	salary = float(input('Salary:$ '))

gender = str(input('Gender:[M/F]')).strip().upper()
while gender not in 'MF':
	print('TRY AGAIN!\nEnter the gender MALE OR FEMALE [M/F]')
	gender = str(input('Gender:[M/F]')).strip().upper()

status = str(input('Civil Status[S/C/V]: ')).strip().upper()
while status not in 'SCV':
	print('TRY AGAIN!\n Enter the your civil status correct.')
	status = str(input('Civil Status[S/C/V]: ')).strip().upper()

print('~*~'*30)
print(f'USER:{name}.')
print(f'AGE:{age}.')
print(f'GENDER:{gender}.')
print(f'SALARY:{salary}.')
print(f'CIVIL STATUS:{status}.')
print('~*~'*30)