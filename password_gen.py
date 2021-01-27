
#Este script serve para gerar senhas de 10 dígitos de forma automática e aleatória.

from random import choice
import string

'''string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 0123456789
string.punctuation # <=>?@[\]^_`{|}~'''

size = int(input('Enter the password size: '))

while size <= 5:
	print('Easy password to break, recommended: 8 or more characters.')
	size = int(input('Enter the password size: '))

v= string.ascii_letters + string.digits + string.punctuation 


password =' '

for i in range (size):
	password+=choice(v)
print()
print(f'Password generated: {password}')