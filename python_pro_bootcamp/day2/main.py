"""
  Challenge Day 2: Tip Calculator.
  Details: This program will calculate what percentage each person must pay from the bill and tip.
  Author: Yan Brasiliano SIlva Penalva <yanpenabr@gmail.com>
  Date: 18 MAR 2021
  Course:  Python Pro Bootcamp for 2021
  Level: Beginner

"""

print ("Welcome to the tip calculator.")
payment = float(input('Total payable:$ '))
percentage = float(input('Choose a percentage: '))
people = int(input('How many people to split the bill: '))

if payment <= 0:
	print('ERROR.')	
if percentage <= 0:
	print('ERROR.')
if people <= 0:
	print('ERROR.')


total_pay = (payment + (payment*percentage/100))/people

print(f'Each person should pay: ${total_pay:.2f} !')
