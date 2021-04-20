# strip = retira os espaços de antes e depois.
print('\tANALYZE NAME INFORMATION')
print('\n')
name = str(input('enter your complete name: ')).strip()
print('Analyzing your name...')
print('\n')
print('Your name: {}. \nYour name upper: {}. \nYour name lower: {}. \nYour name have {} letters.\nYour first name have {} letters	'
      .format(name, name.upper(), name.lower(), len(name) - name.count(' '), name.find(' ')))
