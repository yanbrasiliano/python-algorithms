# programa calculará valor do empréstimo baseado nas informações solicitadas pelo user.

from time import sleep

n = str(input('Name: '))
h = float(input('Value house:R$ '))
s = float(input('Personal Salary:R$ '))
y = int(input('Time to pay for home(YEARS): '))


p = h / (y * 12)
media = s * 30 / 100


print('\n')
print('\tAnalyzing...')
sleep(2)

if p > media:
    print('Sorry, {}! You can\'t buy this house.\nYour salary is R${:.2f} and the value parcels is: R${:.2f}' .format(n, s, p))
    print('This value exceeds 30%% of th your salary.\nCheck another house!')

elif p <= media:
    print('Congratulations, {} !\nYou can buy this house.'.format(n))
    print('Your salary is R${:.2f} and the value parcels is: R${:.2f}'.format(
        s, p))
