#Section B - 2019

def main():
    word2 = input("Enter a word: ")
    word1 = input("Enter another word: ")
    letters = {}
    for letter in word2:
        letters[letter] = letters.get(letter, 0) + 1
    possible = True
    for letter in word1:
        if letter not in letters or letters[letter] == 0:
            possible = False
            break
        letters[letter] -= 1
    if possible:
        print("Yes, word 1 can be made from the letters in word 2")
    else:
        print("No, word 1 cannot be made from the letters in word 2")

main()