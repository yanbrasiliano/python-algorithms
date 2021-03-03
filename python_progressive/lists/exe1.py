# Crie um programa que pergunta se o usuário deseja adicionar uma nova banda na Lista ou exibir a lista.
x = []

while True:
    choice = int(input('''
	1 - Add item to list.
	2 - Show list.
	3 - List size.\n
	Option: '''))
    if choice == 1:
        value = int(input('Add value: '))
        x.append(value)
    if choice == 2:
        print(f'List: {x}.')
    if choice == 3:
        print(f'Size is: {len(x)}')
