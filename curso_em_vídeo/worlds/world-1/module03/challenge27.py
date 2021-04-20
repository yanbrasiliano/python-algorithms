name = str(input('Enter name: ')).strip()

x = name.split()

print('First name: {} \nLast name: {}' .format(x[0], name[len(name)-1]))