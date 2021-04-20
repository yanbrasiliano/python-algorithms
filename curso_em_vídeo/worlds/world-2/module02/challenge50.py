# programa lerá 6 números e somará apenas os números pares.
s = 0
cont = 0
for c in range(0, 7):
    x = int(input('Enter number [{}]: '.format(c)))
    if x % 2 == 0:
        s += x
        cont += 1

print('There\'re {} values par and sum this values is: {}'.format(cont,s))
