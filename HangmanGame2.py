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
        while letter.lower() in guessed or letter.lower() in current:
            print("You've already guessed that!")
            letter = input("Guess a letter: ")
        while not letter.isalpha() or len(letter) > 1:
            print("Invaild input.")
            letter = input("Guess a letter: ")
        letter = letter.lower()
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
        print("You got it!!")
    print("The word was:",word)

# if you want another person to give you the word use the code below(from line61 to line70):
# os.system("clear")
# print("===Hangman Game===")
# w = input("Enter a word to guess:\n>>")
# while not w.isalpha() or len(w) <= 1:
#     print("Invaild input.")
#     w = input("Please enter a word to guess:\n>>")
# os.system("clear")
# print("===Hangman Game===")
# input("Are you ready?\nClick the enter key to start! ")
# guess(w)

# otherwise just put the word into the brackets of the guess function:
guess("rainbow")
