from random import randint
import random as r
import collections as c

# Initialize variables
score = 0
mistakes = 0
newWord = True
correctChars = []
incorrectChars = []

# List of words
words = ['Gazelle', 'Automobile', 'Telephone', 'Elephant', 'Laptop', 'Motorcycle', 'Whiteboard', 'Blackboard']

# Functions
def choose_word(wordList):
    incorrectChars.clear()
    correctChars.clear()
    word = list(r.choice(wordList))                         # Get a random word from the list of words and store it as a list
    correctChars.extend(word[0] * word.count(word[0]))      # Add first and last character from word to the list of correct characters
    correctChars.extend(word[-1] * word.count(word[-1]))
    if ' ' in word:                                         # Did this so the user doesn't have to guess empty spaces
        correctChars.extend(' ' * word.count(' '))

    return word

def display_word(word):
    for character in range(len(word)):          # Loop through every character inside the chosen word,
        if word[character] in correctChars:     # displaying only characters which are already guessed correctly
            print(word[character], end="")      # and displaying the rest of characters with a '_'
        elif word[character] == " ":
            print(" ", end="")
        else:
            print("_", end="")

def isCorrectChar(character, word):             # Function to check if the entered character is correct or not
    global score, mistakes
    if character in word and character not in correctChars:
        score += 1
        correctChars.extend(character * word.count(character))  # Using extend because if word has multiple of the same characters
        return True                                             # it adds however many characters there are to the list of correctChars.
    else:                                                       # This is necessary for isWordCompleted() function as it uses collections.Count
        mistakes += 1
        incorrectChars.append(character)
        return False

def isWordCompleted(word):
    if c.Counter(word) == c.Counter(correctChars):  # This is the reason to use list.extend() function as mentioned previously as this
        return True                                 # collection stores elements as dictionary keys and their counts are stored as dictionary values
    else:
        return False

def start_game():
    global newWord
    while mistakes < 10:
        if newWord:
            word = choose_word(words)
            msg = ''

        display_word(word)
        guess = input('\nGuess a letter: ')

        if isCorrectChar(guess, word):
            print('\nCorrect guess! You received 1 point.\n')
        else:
            print('\n"'+ guess + '" is the wrong guess! You have ' + str(mistakes) + ' mistake(s).\n')

        newWord = isWordCompleted(word)
        if newWord:
            for char in word:
                msg += char
            print(msg + '\nWord guessed correctly! You have ' + str(score) + ' points.\n')

    print('\nGame over! You have ' + str(score) + ' points!')

# Function calls
start_game()