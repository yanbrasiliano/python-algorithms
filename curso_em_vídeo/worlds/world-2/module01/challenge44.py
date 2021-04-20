# programa calculará o o valor a ser pago de um produto a partir das condições estabelecidas.
from time import sleep

product = str(input('Product: '))
value = float(input('Value:R$ '))


print(''''Choose the option:\n
[1]- Cash payment / check = descount 10%%.
[2]- Cash payment on card = descount 5%%.
[3]- 2x card = R${}.
[4]- 3x or more =	20%% interest.''' .format(value/2))

option = int(input('\nOption: '))

print('\n')
print('\tLoading...')
sleep(2)

if option == 1:
    print('Product: {}\nAmount to be paid:R${}\nDiscounted value:R${}' .format(
        product, value, value - (value*0.1)))

elif option == 2:
		print('Product: {}\nAmount to be paid:R${}\nDiscounted value:R${}' .format(
        product, value, value - (value*0.05)))
	
elif option == 3:
		print('Product: {}\nAmount to be paid:R${}\nParcel: 2x of R${} \nDiscounted value: none' .format(
        product,value,(value/2)))
elif option == 4:
		totalparc = int(input('\nParcels: '))

		print('\nProduct:{}\nAmount to be paid:R${}\nParcel:{} of R${}\nTotal:R${}' .format(
        product, value, totalparc,(value + (value * 0.2))/2, value + (value * 0.2)))  