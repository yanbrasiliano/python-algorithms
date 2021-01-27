# 4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
# 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''4. paisA=80000
paisB=200000
ano=0

while paisA<paisB:
paisA*=1.03
paisB*=1.015
ano+=1
'''
# 5.

popA = int(input('Population city A: '))
while popA < 0:
    print('Population must be greater than 0')
    popA = int(input('Population city A: '))
rateA = float(input('Growth rate city A: '))
popB = int(input('Population city B: '))
while popB < 0:
    print('Population must be greater than 0')
    popB = int(input('Population city B: '))
rateB = float(input('Growth rate city B: '))
year = 0
while popA < popB:
	year += 1
	popA = int((1 + (rateA/100)*popA))
	popA = int((1 + (rateB/100)*popB))

print(f'{year}')
print(f'Population A: {popA}')
print(f'Population B: {popB}')
print(f'Exceeds in the year {year}.')
