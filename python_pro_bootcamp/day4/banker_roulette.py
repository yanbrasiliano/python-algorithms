# Banker Roulette - Who Will pay the bill?
import random

names = input('Typed all names, separated by a comma: ').split(", ")

# total_items = len(names)
# random_choice = random.randint(0, total_items - 1)
# person_who_will_pay = names[random_choice]
# print(f"{person_who_will_pay} is going to buy the meal today!")


print(f'{random.choice(names)} is going to buy thea meal today!')
