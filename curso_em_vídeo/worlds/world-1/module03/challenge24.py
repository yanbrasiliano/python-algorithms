## programa lerá o nome de uma cidade e dirá se há ou não o nome SANTO.

x = str(input('Enter name of the city: ')).strip()

print(x[:5].upper() == 'SANTO') ## coloca todo o nome em maiúsculo para fazer a verificação.



