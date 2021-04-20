"""
  Challenge Day 5: Password Generator.
  Details: 	This program generates secure and random passwords 
  Author: 	Yan Brasiliano Silva Penalva <yanpenabr@gmail.com>
  Date: 		09 APR 2021
  Course:   Python Pro Bootcamp for 2021
  Level:	  Beginner

"""
import random

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter= int(input('Quantity of letters: '))
symbol= int(input('Quantity of symbols: '))
number= int(input('Quantity of numbers: '))

password_list = []

for char in range(1, letter + 1):
  password_list.append(random.choice(letters))

for char in range(1,symbol + 1):
  password_list += random.choice(symbols)

for char in range(1,number + 1):
  password_list += random.choice(numbers)

#print(password_list)
#random.shuffle(password_list)
#print(password_list)

passwd=""
for char in password_list:
  passwd+=char

print(f"Your password is: {passwd}")