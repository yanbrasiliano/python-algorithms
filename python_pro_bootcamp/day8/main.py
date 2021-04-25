"""
  Challenge Day 8: 	Caesar Cipher
  Details: 					Script to simulate caesar cipher.
  Author: 					Yan Brasiliano Silva Penalva <yanpenabr@gmail.com>
  Date: 						14 APR 2021
  Course:   				Python Pro Bootcamp for 2021
  Level:	 					Beginner
	
"""

import random

logo = [''' 

  ___   _   ___ ___   _   ___    ___ ___ ___ _  _ ___ ___ 
 / __| /_\ | __/ __| /_\ | _ \  / __|_ _| _ \ || | __| _ \
| (__ / _ \| _|\__ \/ _ \|   / | (__ | ||  _/ __ | _||   /
 \___/_/ \_\___|___/_/ \_\_|_\  \___|___|_| |_||_|___|_|_\


''']
print(logo)

def encrypt(text,shift):
	cipher=" " # lista vazia para receber código cifrado.
	for letter in text:
		position=alphabet.index(letter) # posição das letras da frase/texto digitadas.
		new_position=position+shift # a nova posição será a posição atual + os saltos solicitados.
		new_letter=alphabet[new_position] # a nova letra baseada nos saltos.
		cipher+=new_letter # a junção das letras.
	print(f'Encoded message: {cipher}')	# exposição do código cifrado.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = input("Message: ").lower()
shift = int(input("Shift number: "))
encrypt(text,shift)


