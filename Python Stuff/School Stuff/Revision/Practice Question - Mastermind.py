# Mastermind
# Generate a random four digit number. The player has to keep inputting four digit numbers until they guess the randomly generated number. After each unsuccessful try it should say 
# how many numbers they got correct, but not which position they got right. At the end of the game should congratulate the user and say how many tries it took.
# Extensions: 
# 1. Let the user pick an easy mode which shows the user which position that they guessed correctly
# 2. Let the user pick a hard mode that gives five digits instead of four
# 3. After the game is finished, ask the user for their name and input their score into a table. Show them the high score at the start of the game so that it gives a sense of competition

import random
from statistics import mode
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
easy_leaderboard = os.path.join(script_dir, "easymode_leaderboard")
hard_leaderboard = os.path.join(script_dir, "hardmode_leaderboard")

def easymode():
    random_number = str(random.randint(1000, 9999))
    tries = 0
    while True:
        user_input = input("Enter a four digit number: ")
        tries += 1
        if user_input == random_number:
            print(f"Congratulations! You've guessed the number in {tries} tries.")
            name = input("Enter your name for the leaderboard: ")
            with open(easy_leaderboard, "a") as f:
                f.write(f"{name},easy,{tries}\n")
            print("Do you want to play again or view the leaderboard? (Y/N/V):")
            choice = input().upper()
            if choice == 'Y':
                main()
            elif choice == 'V':
                view_leaderboards()
            else:
                print("Thanks for playing!")
            break
        else:
            correct_positions = [i for i, (a, b) in enumerate(zip(user_input, random_number)) if a == b]
            display = ['?' if i not in correct_positions else user_input[i] for i in range(len(user_input))]
            print(f"You got {len(correct_positions)} digits correct and in the right position: {display}")
            

def hardmode():
    random_number = str(random.randint(10000, 99999))
    tries = 0
    while True:
        user_input = input("Enter a five digit number: ")
        tries += 1
        if user_input == random_number:
            print(f"Congratulations! You've guessed the number in {tries} tries.")
            name = input("Enter your name for the leaderboard: ")
            with open(hard_leaderboard, "a") as f:
                f.write(f"{name},hard,{tries}\n")
            print("Do you want to play again or view the leaderboard? (Y/N/V):")
            choice = input().upper()
            if choice == 'Y':
                main()
            elif choice == 'V':
                view_leaderboards()
            else:
                print("Thanks for playing!")
            break
        else:
            correct_positions = sum(1 for a, b in zip(user_input, random_number) if a == b)
            print(f"You got {correct_positions} digits correct and in the right position.")

def view_leaderboards():
    try:
        with open(easy_leaderboard, "r") as f:
            easy_entries = [line.strip().split(',') for line in f if line.strip()]
    except FileNotFoundError:
        easy_entries = []
    easy_entries.sort(key=lambda x: int(x[2]))
    print("Easy Mode Leaderboard:")
    if easy_entries:
        for entry in easy_entries:
            print(f"{entry[0]}: {entry[2]} tries")
    else:
        print("No entries yet.")
    print()
    try:
        with open(hard_leaderboard, "r") as f:
            hard_entries = [line.strip().split(',') for line in f if line.strip()]
    except FileNotFoundError:
        hard_entries = []
    hard_entries.sort(key=lambda x: int(x[2]))
    print("Hard Mode Leaderboard:")
    if hard_entries:
        for entry in hard_entries:
            print(f"{entry[0]}: {entry[2]} tries")
    else:
        print("No entries yet.")
    print()
    input("Press enter to return to menu.")
    main()

def invalid_input():
    print("Invalid choice selected. Please choose E for Easy, H for Hard, or V for View Leaderboards.")
    mode = input("Choose a mode: Easy (E), Hard (H), or View Leaderboards (V): ").upper()
    if mode == 'E':
        easymode()
    elif mode == 'H':
        hardmode()
    elif mode == 'V':
        view_leaderboards()
    else:
        invalid_input()

def main():
    print("Welcome to Mastermind!")
    mode = input("Choose a mode: Easy (E), Hard (H), or View Leaderboards (V): ").upper()
    if mode == 'E':
        easymode()
    elif mode == 'H':
        hardmode()
    elif mode == 'V':
        view_leaderboards()
    else:
        invalid_input()

main()