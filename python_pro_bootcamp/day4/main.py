"""
		Challenge Day 4: Stone, Paper or Scissors.
		Details: This program simulates a stone, paper or scissors game. 
		Author:  Yan Brasiliano Silva Penalva <yanpenabr@gmail.com>
		Date: 	 23 MAR 2021
		Course:  Python Pro Bootcamp for 2021
		Level:	 Beginner
		Details: Rock wins against Scissors.
						 Scissors wins against Paper.
						 Paper wins against Rock.


"""

# Game images.d
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Lib random for choose computer.
import random

# List containing the images.
images = [rock,paper,scissors]

# Choose user and random computer
user = int(input('0. Rock\n1. Paper\n2. Scissors\n\nChoose: '))
if user >= 3 or user < 0:
	print('You typed an invalid number, you lose!')
else:
	print(images[user])
computer = random.randint(0,2)
print(images[computer])
print(f'Computer choose {computer}.')
# Logic of the game.
if user == 0 and computer == 2:
	print('Congratulations, you win!')
elif computer == 0 and user == 2:
	print('You lose!')
elif computer > user:
	print('You lose!')
elif user > computer:
	print('You lose!')
elif user == computer:
	print("It's a draw!")
