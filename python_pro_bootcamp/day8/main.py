"""
  Challenge Day 8: 	Caesar Cipher
  Details: 					Script to simulate caesar cipher.
  Author: 					Yan Brasiliano Silva Penalva <yanpenabr@gmail.com>
  Date: 						14 APR 2021
  Course:   				Python Pro Bootcamp for 2021
  Level:	 					Beginner
	
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']

direct=input('Encode to encrypt, decode to decrypt: ').lower()
text=input("Message: ").lower()
shift=int(input("Shift number: "))

def caesar(text,shift,direct):
	end=""
	if direct == "decode":
		shift*=-1
	for letter in text:
		position = alphabet.index(letter)
		position+=shift
		if position > 25: 
			end = end + alphabet[position - 26]
		else:
			end = end + alphabet[position]
	print(f"Here's the {direct} result: {end}.")


caesar(text,shift,direct)