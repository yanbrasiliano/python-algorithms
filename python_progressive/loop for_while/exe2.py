#2.Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 
print('\t~REGISTER~')
name = input('Login: ')
password = input('Password: ')
while name == password:
	print('try again, name and password cannot be the same.')
	password = input('Password: ')
print('SUCCESSFULLY REGISTERED')
	