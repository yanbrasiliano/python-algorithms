# este programa contará quantas letras A tem na frase, em que posição a primeira e a ultima aparecem.
phrase = str(input('Enter any sentence or word: ')).strip()

x = phrase.upper()
print('A appears {} times, starts in position {} and end in position {}'
      .format(x.count('A'), phrase.find('A')+1, phrase.rfind('A') + 1))

