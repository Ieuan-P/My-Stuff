# Mastermind
# Generate a random four digit number. The player has to keep inputting four digit numbers until they guess the randomly generated number. After each unsuccessful try it should say 
# how many numbers they got correct, but not which position they got right. At the end of the game should congratulate the user and say how many tries it took.
# Extensions: 
# 1. Let the user pick an easy mode which shows the user which position that they guessed correctly
# 2. Let the user pick a hard mode that gives five digits instead of four
# 3. After the game is finished, ask the user for their name and input their score into a table. Show them the high score at the start of the game so that it gives a sense of competition

import random
def generate_random_number(length):
    return ''.join(random.choices('0123456789', k=length))
def count_correct_digits(secret, guess):
    return sum(1 for s, g in zip(secret, guess) if s == g)
def mastermind():
    length = 4
    secret_number = generate_random_number(length)
    attempts = 0
    print("Welcome to Mastermind! Try to guess the 4-digit number.")
    
    while True:
        guess = input("Enter your guess: ")
        attempts += 1
        
        if guess == secret_number:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break
        else:
            correct_digits = count_correct_digits(secret_number, guess)
            print(f"You have {correct_digits} correct digits.")

mastermind()