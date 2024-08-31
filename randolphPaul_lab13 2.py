# Randolph Paul 4/14/2024 randolphPaul_lab13
"""The purpose of this program is to generates a random number in the range
of 1 through 100, and ask a user to guess what the number is."""

import random

print("""\nInstructions: 
This program generates a random number in the range
of 1 through 100. You have 7 guesses to get the 
correct number before a new number is chosen.""")

for i in range(1, 8):
    guess = int(input("Guess a number between 0 and 100: "))
    random_number = random.randint(0, 100)
    if guess == random_number:

    elif
        break
    print(i)

print(random_number)