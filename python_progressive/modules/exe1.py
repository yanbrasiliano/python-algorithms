"""
Crie um script em Python que gere 6 números aleatórios para a Mega-Sena
(neste jogo, você pode escolher dezenas de 1 até 60). Não pode repetir
dezena.
"""

from random import randint

sort = 0 
x = randint(1,60)
for i in range(1,7):
	sort = randint(1,60)
	if sort != x:
		x = sort

	print(f'{i}° == {x}')
