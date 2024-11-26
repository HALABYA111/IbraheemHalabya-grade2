# "Word Scramble Game"

import random

word_list = ["apple", "banana", "grape", "orange", "peach", "cherry", "mango", "kiwi", "pear", "melon"]

original_word = random.choice(word_list)

scrambled_word = ''.join(random.sample(original_word, len(original_word)))

attempts = 5

print("Welcome to the Word Scramble Game!")
print(f"Try to guess the original word from the scrambled word: {scrambled_word}")
print(f"You have {attempts} attempts.\n")

while attempts > 0:
    player_guess = input("Enter your guess: ").strip()

    if not player_guess:
        print("Invalid input! Please enter a word.\n")
        continue

    if player_guess.lower() == original_word:
        print("Congratulations! You guessed the correct word!")
        break

    attempts -= 1
    if attempts > 0:
        print(f"Incorrect! Try again. You have {attempts} attempts left.\n")
    else:
        print(f"You're out of attempts! The correct word was: {original_word}")
