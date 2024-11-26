#"Guess the Secret Number Game"

import random

def guess_the_secret_number():
    secret_number = random.randint(1, 100)
    attempts = 7  

    print("Welcome to the 'Guess the Secret Number' game!")
    print("I have chosen a number between 1 and 100. You have 7 attempts to guess it.")

    while attempts > 0:
        try:
            guess = int(input(f"Attempt {8 - attempts}: Enter your guess: "))

            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} correctly!")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")

            attempts -= 1
            if attempts > 0:
                print(f"You have {attempts} attempts left.")
            else:
                print(f"Sorry, you've run out of attempts! The correct number was {secret_number}.")

        except ValueError:
            print("Invalid input! Please enter a valid number between 1 and 100.")

guess_the_secret_number()
