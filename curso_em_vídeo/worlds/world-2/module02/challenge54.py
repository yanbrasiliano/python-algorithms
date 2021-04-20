# programa lerá o ano de nascimento de 7 pessoas e dirá quantas ainda não são maiores de idade.
from datetime import date

x = date.today().year
maior = 0
menor = 0

for c in range(1,8):
	birth = int(input('Date of birth [{}°] person: '.format(c)))
	age = x - birth

	if age >= 21:
		maior+=1
	
	else: 
		menor+=1
		
print('Legal age {} people'.format(maior))
print('Minor age {} people'.format(menor))
