# progama lerá as informações e dará a média de idade, o nome do homem mais velho e quantas mulheres tem menos de 20 anos.


# média de idade
soma = 0
media = 0
# nome do mais velho
maior = 0
n = ''
# mulher com menos de 20
totgirl = 0

for p in range(1, 5):

    nome = str(input('Name {}° person: '.format(p))).strip()
    idade = int(input('Age: '))
    sexo = str(input('Gender[M/F]: ')).strip()
    print('\n')
    soma += idade  # lógica da média.
    if p == 1 and sexo in 'Mm':
        maior = idade
        n = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        n = nome  # lógica do nome.

        if sexo in 'Ff' and idade > 20:
            totgirl += 1  # lógica da idade.


media = soma/4  # lógica da média.
print('Average is: {:.2f}'.format(media))  # resultado da média.
print('The old man has {} years old and your name is {}.'.format(
    maior, n))  # resultado do nome
# resultado do total de idade.
print('There are {} women under the age 20 years old.'.format(totgirl))
