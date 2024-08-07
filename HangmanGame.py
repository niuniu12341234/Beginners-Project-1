print("===Hangman Game===")
def guess(word="code",round=8):
    correct = len(word)
    current = "_ "*len(word)
    count = 0
    wrong = 0
    guessed = set()
    word = word.lower()
    print(current)
    while correct != 0:
        if count >= round:
            print("Nope\nHe died RIP:(")
            break
        letter = input("Guess a letter: ")
        while letter in guessed or letter in current:
            print("You've already got it!")
            letter = input("Guess a letter: ")
        while len(letter) > 1 or not letter.isalpha:
            print("Invaild input.")
            letter = input("Guess a letter: ")
        times = 0
        for n in word:
            if n != letter:
                wrong += 1
            if n == letter:
                current = current[:times] + (current[times].replace("_",letter)) + current[times+1:]
                print(current)
                correct -= 1
            times += 2
        if wrong == len(word):
            count += 1
            guessed.add(letter)
            print("Nope")
        print("Letters guessed:",guessed,"\n")
        wrong = 0
    if correct == 0:
        print("You got it!")
    print("The word was:",word)
guess("oxygen",9)
