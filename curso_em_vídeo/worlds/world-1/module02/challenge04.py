x = str(input('enter something: '))
print('the primitive type is ', type(x)) ## qual o tipo primitivo? por padrão, será stringg, mas as perguntas abaixo definirão mais detalhadamente o tipo.
print('is there only spaces? ',x.isspace()) ## contem só espaços?
print('is a number? ',x.isnumeric()) ## é um número?
print('is alphabetic? ', x.isalpha()) ## é alfabético?
print('is alphanumeric? ', x.isalnum()) ##é alfanumérico? - números e letras
print('is in uppercase? ', x.isupper()) ##está em maiúsculo?
print('is in slowercase? ', x.islower()) ##está em minúsculo?
print('is a capitalized? ', x.istitle()) ##está com o valor em maiúsculo e minúsculo?

