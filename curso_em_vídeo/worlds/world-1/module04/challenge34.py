## este progama calculará o valor do aumento de um funcionário baseado nos dados informados.


n = str(input('Name: '))
s = float(input('Salary:R$ '))




if s >= 1250:
	print('The new salary of the {} is R${}' .format(n,(s * 0.1) + s))

else:
	print('The new salary of the {} is R${}' .format(n,(s * 0.15) + s))