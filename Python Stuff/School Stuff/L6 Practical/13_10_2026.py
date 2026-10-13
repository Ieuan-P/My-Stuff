#Section B - 2019

def B2019():
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

#B2019()

#Section B - 2020

def B2020():
    Num_of_digits = int(input("How many numbers do you want to enter? "))
    numbers = []
    for i in range(Num_of_digits):
        numbers.append(int(input("Enter a number: ")))
    Most_Frequent = max(set(numbers), key=numbers.count)
    frequency = numbers.count(Most_Frequent)
    if sum(1 for number in set(numbers) if numbers.count(number) == frequency) > 1:
        print("Data was multimodal")
    else:
        print(f"The most frequent number is: {Most_Frequent}, which appears {frequency} times")

#B2020()