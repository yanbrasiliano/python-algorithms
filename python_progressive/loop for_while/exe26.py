'''	
	26. Numa eleição existem três candidatos.
	1 - Faça um programa que peça o número total de eleitores.
	2 - Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
	'''
print('''
\tELECTIONS 2020
[1] Donald Trump - REP
[2] Joe Biden - DEM
[3] Jo Jorgensen - LP
[4] Howie Hawkins - GP
[5] Null''')

a = b = c = d = e = f = 0
while True:
	vote = int(input('Vote Option[1-5]: '))
	e += 1
	if vote == 1:
		a+=1
	if vote == 2:
		b+=1
	if vote == 3:
		c +=1
	if vote == 4:
		d+=1
	if vote == 5:
		f+=1
	while vote > 6 or vote < 1:
			print('INVALID NUMBER!')
			break
	res = ' '
	while res not in 'YN':
		res = str(input('CONTINUE? [Y/N]')) .upper().split()[0]
	if res == 'N':
		break
	
print(f'Total votes: {e}.')
print()
print(f'Candidate - Donald Trump - REP\nVotes:{a}')
print()
print(f'Candidate - Joe Biden - DEM\nVotes:{b}')
print()
print(f'Candidate - Jo Jorgensen - LP\nVotes:{c}')
print()
print(f'Candidate - Howie Hawkins - GP\nVotes:{d}')
print()
print(f'NULL\nVotes:{f}')