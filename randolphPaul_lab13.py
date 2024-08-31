# Randolph Paul 4/14/2024 randolphPaul_lab13
"""The purpose of this program is to generates a random number in the range
of 1 through 100, and ask a user to guess what the number is."""


# Import the module to generate random numbers
import random


# Set global constants
min_guess = 1
max_guess = 100


# Explain the game to the user
print("""\nInstructions: 
This program generates a random number in the range
of 1 through 100. You have 7 guesses to get the 
correct number before a new number is chosen.""")


# Ask user for a guess
def get_user_guess():
    while True:
        try:
            guess = int(input("Guess the number (1-100): "))
            if min_guess <= guess <= max_guess:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Please enter a valid number.")


# Run the main program
def play_game():
    wins = 0
    losses = 0
    counter = 1
    max_attempts = 7
    while True:
        random_number = random.randint(min_guess, max_guess)
        guesses = 0
        for _ in range(max_attempts):
            guesses += counter
            print(f"\nAttempt {guesses}:")
            user_guess = get_user_guess()
            if user_guess > random_number:
                print("Too high, try again.")
            elif user_guess < random_number:
                print("Too low, try again.")
            else:
                print(f"Congratulations! You guessed the number in {guesses} guesses.")
                wins += counter
                break
        else:
            print(f"\nSorry, you didn't guess the number. The correct number was {random_number}.")
            losses += counter

        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again.lower() == 'no':
            break
    print(f"Total wins: {wins:,}, Total losses: {losses:,}")


# Entry point of the program
if __name__ == "__main__":
    play_game()
