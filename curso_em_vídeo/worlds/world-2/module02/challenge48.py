sum = 0
cont = 0


for c in range(1, 500, 2):
    if c % 3 == 0:
        cont += 1
        sum += c
print('Sum {} numbers impares = {}' .format(cont, sum))
