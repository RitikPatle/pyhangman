# Hangman Python Script
#   A python Script for CLI based Hangman Game
#   Developed by : Ritik Patle [https://ritik-patle.web.app]

# Importing Requirments
import random   # To select randomly
from db import wordsList    #File acting as database for game

# Declaring Colors to display in CLI
redColor = "\033[0;31m"         # Light red color
blueColor = "\033[1;34m"        # Blue color
greyColor = "\033[1;30m"        # Grey color
greenColor = "\033[0;32m"       # Light green color
purpleColor = "\033[0;35m"      # Purple color
yellowColor = "\033[0;33m"      # Yellow color
brightRedColor = "\033[1;31m"   # Bright Red color
brightGreenColor = "\033[1;32m" # Bright Green color

# To get word from db
def getWord():
    word = random.choice(wordsList)
    return word.upper()

# To start game
def playGame(word):
    wordCompletion = "_" * len(word) # To display length of word as '_'
    guessed = False # Initially guessed -> False
    guessedLetters = [] # To store guessed letters
    guessedWords = [] # To store guessed words
    tries = 6 # Maximum tries

    print(purpleColor,end="")
    print("Hangman...") # Title of game

    print(greenColor,end="")
    print(f" $ Life Remaning = {tries}") # Remaning tries / lives

    print(blueColor,end="")
    print(displayHangman(tries)) # To display hanging man skeleton

    print(greyColor,end="")
    print(wordCompletion) # To display completed words as _o_d_
    print("\n")

    while not guessed and tries > 0: # While word is not guessed do
        
        # Take user input as word or letters
        print(blueColor,end="")
        guess = input(" > Please guess a letter or word: ").upper()
        
        # Condition if input is a letter
        if len(guess) == 1 and guess.isalpha():

            if guess in guessedLetters: # Condition if user has entered this earlier
                print(yellowColor,end="")
                print(f" ! You've already guessed the letter {guess}.")
            elif guess not in word: # Condition if letter is not in the word
                tries -= 1 # Life = Life - 1
                guessedLetters.append(guess)
                print(redColor,end="")
                print(f" !!Opps, {guess} is not in the word.")
            else: # Condition if letter is in the word
                guessedLetters.append(guess)
                print(greenColor,end="")
                print(f" # Congrats, You've moved one step ahead.\n   {guess} is in the word.")
                wordAsList = list(wordCompletion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    wordAsList[index] = guess
                wordCompletion = "".join(wordAsList)
                if "_" not in wordCompletion:
                    guessed = True

        # Condition if input is a word
        elif len(guess) == len(word) and guess.isalpha():

            if guess in guessedWords: # If user has guessed this previously
                print(yellowColor,end="")
                print(f" ! You've already guessed the word {guess}.")
            elif guess != word: # If word does not matches with input
                tries -= 1
                guessedWords.append(guess)
                print(redColor,end="")
                print(f" !! Opps, {guess} is not the word.")
            else: # If user guessed the word
                guessed = True
                wordCompletion = word
        
        # Condition if user have entered other than alphabets.
        else:
            print(redColor,end="")
            print(f" !! Not a valid guess.")

        # To print Life remaning / Tries left after each term
        print(greenColor,end="")
        print(f" $ Life Remaning = {tries}")

        # To display hanging man skeleton after each term
        print(blueColor,end="")
        print(displayHangman(tries))

        # To display how many letters left of the word after each term
        print(greyColor,end="")
        print(wordCompletion)
        print("\n")

    # Condition if User guessed Correctly [User won the game]
    if guessed:
        print(brightGreenColor,end="")
        print(f" ### Congrats, You've guessed the word {guess}.")
    # Condition if User did not guessed it [User lost the game]
    else:
        print(brightRedColor,end="")
        print(f" !!! Opps, You could not guess the word {word}.\n     Better Luck Next Time!!!.")


def displayHangman(tries):
    stages = [
        # Final Stage [User Lost] [Remaning Lives 0]
        """
            ---------
            |       |
            |       O
            |      \|/
            |       |
            |     ./ \.
        ---------
        """,
        # [Remaning Lives 1]
        """
            --------
            |      |
            |      O
            |     \|/
            |      |
            |     / 
        ---------
        """,
        # [Remaning Lives 2]
        """
            --------
            |      |
            |      O
            |     \|/
            |      |
            |      
        ---------
        """,
        # [Remaning Lives 3]
        """
            --------
            |      |
            |      O
            |    --|
            |      |
            |     
        ---------
        """,
        # [Remaning Lives 4]
        """
            --------
            |      |
            |      O
            |      |
            |      |
            |     
        ---------
        """,
        # [Remaning Lives 5]
        """
            --------
            |      |
            |      O
            |    
            |      
            |     
        ---------
        """,
        # Initial State [Remaning Lives 6]
        """
            --------
            |      |
            |      
            |    
            |      
            |     
        ---------
        """,
    ]
    return stages[tries]

# Declaring Main Function -> Entry Point of Game
def main():
    # To get a word from db
    word = getWord()
    # To start the game
    playGame(word)

    # Condition -> while user enters 'Y' play game again
    print(blueColor,end="")
    while input(" > Do you want to play again (Y/N) : ").upper() == "Y":

        # To declare end of old game
        print(greyColor,end="")
        print("___________________________________________________________\n")

        # To restart a new game
        word = getWord()
        playGame(word)

# To execute code [To call entry point at execution]
if __name__ == "__main__":
    main()