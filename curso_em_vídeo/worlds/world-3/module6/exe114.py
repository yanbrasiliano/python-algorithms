#Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
	website = urllib.request.urlopen('ENTER URL HERE!')
except:
	print(f'THE WEBSITE {website} is OFFLINE!')
else:
	print(f'THE WEBSITE {website} is ONLINE!')
