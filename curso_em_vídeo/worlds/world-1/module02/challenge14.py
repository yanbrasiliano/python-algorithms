##conversor de temperaturas

c = float(input('enter the temperature in °C: '))

print('the temperature {}°C equals {:.2f}°F.'.format(c, (1.8*c) + 32))
print('the temperature {}°C equals {}°K.'.format(c, (c+273)))

## K = C + 273.
## F = 1.8C + 32.