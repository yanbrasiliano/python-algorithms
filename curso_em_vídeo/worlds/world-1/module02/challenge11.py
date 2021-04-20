b = float(input('width of the wall is: '))
h = float(input('height of the wall is: '))

a = b * h
l = a / 2 


print('Your wall has the dimensions {}x{} and your area is {:.2f}m². \nYou will need {:.2f}l to paint your wall'.format(b,h,a,l))
