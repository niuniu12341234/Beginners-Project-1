import os
def guess(word="code"):
    HMpics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]
    correct = len(word)
    current = "_ "*len(word)
    count = 0
    wrong = 0
    guessed = set()
    word = word.lower()
    while correct != 0:
        os.system("clear")
        print("===Hangman Game===")
        print(HMpics[count])
        print(current)
        print("Letters guessed:",", ".join(guessed))
        if count >= 6:
            print("Nope\nHe died RIP:(")
            break
        letter = input("Guess a letter: ")
        while letter in guessed or letter in current:
            print("You've already got it!")
            letter = input("Guess a letter: ")
        while len(letter) > 1 or not letter.isalpha():
            print("Invaild input.")
            letter = input("Guess a letter: ")
        times = 0
        for n in word:
            if n != letter:
                wrong += 1
            if n == letter:
                current = current[:times] + (current[times].replace("_",letter)) + current[times+1:]
                correct -= 1
            times += 2
        if wrong == len(word):
            count += 1
            guessed.add(letter)
        wrong = 0
    if correct == 0:
        os.system("clear")
        print("===Hangman Game===")
        print(HMpics[count])
        print(current)
        print("Letters guessed:",", ".join(guessed))
        print("You got it!")
    print("The word was:",word)
guess("excellent")
