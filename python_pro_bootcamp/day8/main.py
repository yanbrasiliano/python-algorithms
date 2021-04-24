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

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text,shift):
	cipher=""
	for letter in alphabet:
		pos=alphabet.index(letter)
		newpos=pos+shift
		newletter=alphabet[newpos]
			



direction = input("Type 'encode' to encrypt or type 'decode' to decrypt: ")
text = input("Message: ").lower()
shift = int(input("Shift number: "))