'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

teams = ('Bahia', 'EC Vitória', 'Chapecoense', 'Vasco da Gama',
         'São Paulo', 'Internacional', 'Grêmio', 'CRB', 'CSA',
         'Santa Cruz', 'Sport', 'Náutico', 'Fortaleza', 'Ceará',
         'Sampaio Correia', 'Confiança', 'Botafogo', 'Fluminense',
         'Flamengo', 'Athletico Paranaense')

#a) Os 5 primeiros times.
print('Top Five')
print('-=-'*29)
print(teams[0:5])
print('-=-'*29)

print('\n')

#b) Os últimos 4 colocados.
print('Last Five Placed')
print('-=-'*29)
print(teams[16:0])
print('-=-'*29)

print('\n')

#c) Times em ordem alfabética.
print('Alphabetical Teams')
print('-=-'*29)
print(sorted(teams))
print('-=-'*29)

print('\n')

#d) Em que posição está o time da Chapecoense.
print('Position Chapecoense Team')
print('-=-'*29)
print(teams.index('Chapecoense'))
print('-=-'*29)

