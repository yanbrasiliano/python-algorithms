"""
Faça um script que exibe uma lista de 10 elementos, contados de 1 até 10.
Depois, dobre cada valor dessa lista e exiba. Veja que agora são todos
pares.
"""

list = []
for v in range(1,11):
	list.append(v)
for v in range(0,len(list)):
	list[v]*=2

print(list)