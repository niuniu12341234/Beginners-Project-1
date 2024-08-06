# Beginners-Project1
Term 4 Beginners Project 1
## Hangman Game


Create a program that allows you to play hangman! Preferably, I’d like it to resemble an actual hangman game (with the lines representing letters and drawing the hangman himself). 


Example with the word ‘code’ : (Input is in bold) 
_This scenario is if the word was guessed in time:_

"_ _ _ _"


Guess a letter: **a**

Nope

Letters guessed: a

Guess a letter: **c**

c _ _ _

Letters guessed: a

Guess a letter:**g**

Nope

Letters guessed: a g

Guess a letter: **d**

c _ d _

Letters guessed: a g

Guess a letter: **o**

c o d _

Letters guessed: a g

Guess a letter: **e**

You got it! The word was: code

_This scenario is if the word wasn’t guessed in time:
(After a few guesses)_
Nope
He died rip :(
The word was: code

**Note:** if the user enters a letter previously given, just tell them off:

E.g. the letter g was already given

Guess a letter: **g**

You already guessed that!

Guess a letter: 

**P.S.** You can add the drawing if you’d like! Here’s an ascii art that you could use:

    HMpics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]

It’s in a list format so keep that in mind!
