"""
  Challenge Day 7: 	Hangman
  Details: 					Hangman game.
  Author: 					Yan Brasiliano Silva Penalva <yanpenabr@gmail.com>
  Date: 						12 APR 2021
  Course:   				Python Pro Bootcamp for 2021
  Level:	 					Beginner
	Verify the complete code in repository Hangman-Game :D
"""
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Add the words to the game and create display/lives.
word_list = ['banana', 'apple', 'space']
word = random.choice(word_list)
display = []
lives = 6
# Create Blanks
for letter in word:
    display.append('_')
print(display)

# Start Game
end_game = False
while not end_game:
	# Guess a letter.
	guess = input('Guess a letter: ').lower()

	# Loop to cycle through the letters of the chosen word; if the letter exists, fill in the blank. 	
	for position in range(len(word)):
		letter = word[position]
		if letter == guess:
			display[position] = letter
	
	# Count lives; if lives == 0 : break the game and the player lose!
	if guess not in word:
		lives -= 1
		if lives == 0:
			end_of_game = True
			print("You lose.")
			break
	
	print(f"{' '.join(display)}")

	
	# Win logic! If the player completing blank files, he's winner.
	if '_' not in display:
		end_game = True
		print('You win!')
		break
	
	# Print stage hangman.
	print(stages[lives])
