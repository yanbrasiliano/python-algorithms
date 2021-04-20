#Line of the map drawn in lists
row1=['⚠️','⚠️','⚠️']
row2=['⚠️','⚠️','⚠️']
row3=['⚠️','⚠️','⚠️']

#Linked List Map.
map = [row1, row2, row3]
print()
print(f'{row1}\n{row2}\n{row3}')
print()

#Asking.
position = input('Where do you want to put the treasure: ')

#Logic to winner the game.
horizontal=int(position[0])
vertical=int(position[1])

map[vertical-1][horizontal-1]="⚛️"

print(f'{row1}\n{row2}\n{row3}')