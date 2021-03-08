loginPass = {'Joao': 'rush',
				'Maria': 'pico',
				'Duarte': 'americo'}

login = str(input('Login: '))
passwd = input('Password: ')

if loginPass[login] == passwd:
	print('Access OK!')
else:
	print('Access Blocked!')