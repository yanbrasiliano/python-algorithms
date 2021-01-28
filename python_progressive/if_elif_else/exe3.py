##APOSTILA PYTHON PROGRESSIVO

# NÚMERO POR EXTENSO
from time import sleep

n = int(input('Number: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000  % 10

print(f'Analyzing number {n}...')
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print(f'M:{m}\nC:{c}\nD:{d}\nU:{u}')
