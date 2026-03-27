# Mastermind
# Generate a random four digit number. The player has to keep inputting four digit numbers until they guess the randomly generated number. After each unsuccessful try it should say 
# how many numbers they got correct, but not which position they got right. At the end of the game should congratulate the user and say how many tries it took.
# Extensions: 
# 1. Let the user pick an easy mode which shows the user which position that they guessed correctly
# 2. Let the user pick a hard mode that gives five digits instead of four
# 3. After the game is finished, ask the user for their name and input their score into a table. Show them the high score at the start of the game so that it gives a sense of competition

import random
from statistics import mode

def easymode():
    random_number = str(random.randint(1000, 9999))
    tries = 0
    while True:
        user_input = input("Enter a four digit number: ")
        tries += 1
        if user_input == random_number:
            print(f"Congratulations! You've guessed the number in {tries} tries.")
            break
        else:
            correct_positions = sum(1 for a, b in zip(user_input, random_number) if a == b)
            correct_positions = sum(1 for a, b in zip(user_input, random_number) if a == b)
            correct_digits = [i for i, (a, b) in enumerate(zip(user_input, random_number)) if a == b]
            print(f"You got {correct_positions} digits correct and in the right position at position(s): {correct_digits}")

def hardmode():
    random_number = str(random.randint(10000, 99999))
    tries = 0
    while True:
        user_input = input("Enter a five digit number: ")
        tries += 1
        if user_input == random_number:
            print(f"Congratulations! You've guessed the number in {tries} tries.")
            break
        else:
            correct_digits = sum(1 for a in user_input if a in random_number)
            print(f"You got {correct_digits} digits correct but not necessarily in the right position.")

def invalid_input():
    print("Invalid mode selected. Please choose E for Easy or H for Hard.")
    mode = input("Choose a mode: Easy (E) or Hard (H): ").upper()
    if mode == 'E':
        easymode()
    elif mode == 'H':
        hardmode()
    else:
        invalid_input()

def main():
    print("Welcome to Mastermind!")
    mode = input("Choose a mode: Easy (E) or Hard (H): ").upper()
    if mode == 'E':
        easymode()
    elif mode == 'H':
        hardmode()
    else:
        invalid_input()

main()