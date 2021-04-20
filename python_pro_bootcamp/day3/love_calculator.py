"""
	This script calculates how much you and your crush have compatibility. 
	Logic:
	1. User types his name and that of his crush. 
	2. The script will count how many times the letters of the word TRUE and LOVE appear in the two names and will generate 2 algorisms that together will form a percentage number.

	Calculate based in BUZZFEED Notice.
"""

name = input('Your name: ').lower()
crush = input('Crush name: ').lower()

combined_string = name + crush

# Count TRUE in COMBINED_STRING.
t = combined_string.count('t')
r = combined_string.count('r')
u = combined_string.count('u')
e = combined_string.count('e')
true = t + r + u + e

# Count LOVE in COMBINED_STRING.
l = combined_string.count('l')
o = combined_string.count('o')
v = combined_string.count('v')
e = combined_string.count('e')
love = l + o + v + e

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f'Your score is {score}%; you go together like coke and mentos.')
elif score >= 40 and score <= 50:
	print(f'Your score is {score}%; you are alright together.')
else:
	print(f'Your score is {score}%. ')
