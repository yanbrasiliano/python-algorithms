# programa calculará o preço da passagem por km. 0.5 por viagens até 200km e 0.45 por viagens acima de 200km.

from time import sleep

km = float(input('Enter the distance in km to calculate the ticket price: '))
print('\n')

print('Analyzing...')
sleep(2)

print('\n')

if km >= 200:

    print('Ticket value is:R${} ' .format(km*0.5))

else:
    print('Ticket value is:R${} '.format(km * 0.45))

print('\n')
