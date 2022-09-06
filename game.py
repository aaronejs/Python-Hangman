from random import randint
import random as r
import collections as c

# Initialize variables
score = 0
mistakes = 0
newWord = True
notFirstWord = False
correctChars = []
incorrectChars = []

# List of words
words = ['Gazelle', 'Automobile', 'Telephone', 'Elephant', 'Laptop', 'Phone', 'Whiteboard', 'Blackboard'] 

# Functions
def chooseWord(wordList):
    word = list(r.choice(wordList))                         # Get a random word from the list of words and store it as a list
    correctChars.extend(word[0] * word.count(word[0]))      # Add first and last character from word to the list of correct characters
    correctChars.extend(word[-1] * word.count(word[-1]))
    if " " in word:                                         # Did this so the user doesn't have to guess empty spaces
        correctChars.extend(" " * word.count(" "))

    return word

def displayWord(word):
    for character in range(0, len(word)):       # Loop through every character inside the chosen word,
        if word[character] in correctChars:     # displaying only characters which are already guessed correctly
            print(word[character], end="") # and displaying the rest of characters with a '_'
        elif word[character] == " ":
            print(" ", end="")
        else:
            print("_", end="")            

def isCorrectChar(character, word):             # Function to check if the entered character is correct or not
    if character in word and character not in correctChars:
        global score
        score += 1
        correctChars.extend(character * word.count(character))  # Using extend because if word has multiple of the same characters
        return True                                             # it adds however many characters there are to the list of correctChars.
    else:                                                       # This is necessary for isWordCompleted() function as it uses collections.Count
        global mistakes
        mistakes += 1
        incorrectChars.append(character)
        return False

def isWordCompleted(word):
    if c.Counter(word) == c.Counter(correctChars):  # This is the reason to use list.extend() function as mentioned previously as this
        return True                                 # collection stores elements as dictionary keys and their counts are stored as dictionary values
    else: 
        return False

def startGame():
    global newWord, notFirstWord
    while mistakes < 10:
        if newWord:
            if notFirstWord:        # Check is here to not display the message when game is started
                for char in x:
                    msg += char     # from list to string
                print(msg + '\nWord guessed correctly! You have ' + str(score) + ' points.\n')

            msg = ''
            incorrectChars.clear()  # Clear the character lists
            correctChars.clear()
            x = chooseWord(words)   # Choose a new word
        
        displayWord(x)
        guess = input('\nGuess a letter: ')

        if len(guess) > 1:
            print('\nPlease enter one character!\n')
        else:
            if not isCorrectChar(guess, x):
                print('\n"'+ guess + '" is the wrong guess! You have ' + str(mistakes) + ' mistake(s).\n')
            else:
                print('\nCorrect guess! You received 1 point\n')
            
            newWord = isWordCompleted(x)
            if not newWord:             # Did this so the message for guessing a word correctly
                notFirstWord = True     # wouldn't show up when the game is started

    print('\nGame over! You have ' + str(score) + ' points!')

# Call functions
startGame()