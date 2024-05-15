#Beg Programming:Python Final Project
#This Project Is A Game Of Hangman
#Created By Kia'iKeone

import random
import unittest

print("Let's play Hangman!")

# Shows correct letters guessed in random word
def displayWord(randWord, correctGuesses):
    displayWord = ""
    for letter in randWord:
        if letter in correctGuesses:
            displayWord += letter
        else:
            displayWord += "_"

    return displayWord

# Starts game
def game():
    randomWord = getword()
    randomWord = randomWord.lower()

    correctGuesses = []
    playerGuesses = []
    tries = 6

# If there's guesses left, game continues to play
    while tries > 0:
        keepRunning = True
        while(keepRunning == True):
            guess = input("Guess a letter!\n ")
# Lowercases any letters that are guessed
            guess = guess.lower()
            if guess.lower() in playerGuesses:
                print("You already guessed this letter, please try again. \n")
# Checks guess to make sure letter is in guess
            elif not guess.isalpha():
                print("Your guess is not a letter. Please try again. \n")
            else:
                keepRunning = False
# Check to see if letter is in word. If it is add it to correctGuesses and keep track of letter used
        if guess in randomWord:
            playerGuesses.append(guess)
            correctGuesses.append(guess)
            print(f"{guess} is in the word!\n")
# If letter is not in word take away a try and keep track of letter used
        else:
            playerGuesses.append(guess)
            tries -= 1
            print(f"{guess} is not in the word!\n")

# Show what letters are in word
        disWord = displayWord(randomWord, correctGuesses)
        print(disWord)
# Show guessed letters
        print("Guessed letters:")
        for i in playerGuesses:
            print(i, end=" ")
# If player wins
        if disWord == randomWord:
            print("You Win!")
            result = "Won"
            writeword(randomWord, tries, result)
            break
# If player loses
        if tries < 1:
            print("You lose")
            result = "Lost"
            writeword(randomWord, tries, result)
        print(f"\nYou have {tries} guess(es) left")

# Driver function
def main():

    keepRunning = True
# Keeps game running until user quits
    while(keepRunning == True):
        game()

        answer = True
        while(answer == True):
            print("Do you want to play again? [y/n]")
            response = input()

            if response == 'n':
                answer = False
                keepRunning = False

            if response == "y":
                answer = False

            else: 
                print("Please enter y or n")
            
# Unit testing
class test(unittest.TestCase):
    s = ['c', 'o']
    d = ['m', 'r', 'k']
    m = ['r', 'm']

    def testDisplayWord(self):
        self.assertEqual(displayWord("cool", self.s), "coo_")
        print("Test 1 Passed")
        self.assertEqual(displayWord("maverick", self.d), "m___r__k")
        print("Test 2 Passed")
        self.assertEqual(displayWord("programming", self.m), "_r__r_mm___")
        print("Test 3 Passed")

# The word bank file is imported into the program
def getword():
    file=open("wordbank.txt", "r")
    words=file.read()
    return random.choice(words.split())

# Output is written in output text
def writeword(randomWord, tries, result):
    with open("output.txt", "a") as file:
        file.write(f"The word was {randomWord}. ")
        file.write(f"The number of guesses remaining was {tries}. ")
        file.write(f"You {result}.")
        file.write("\n")

if __name__=="__main__":
    main()
    unittest.main()