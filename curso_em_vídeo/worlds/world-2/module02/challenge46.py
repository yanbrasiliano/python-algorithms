# programa simulará a contagem regressiva para o ano novo.
from time import sleep, time
from datetime import date

x = date.today().year

for c in range(10,-1,-1):
	print(c)
	sleep(0.5)


print('Welcome to {}!' .format(x))
