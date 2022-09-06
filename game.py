from random import randint
import collections as c

# initialize variables
score = 0
mistakes = 0
newWord = True
notFirstWord = False
correctChars = []
incorrectChars = []

#list of words
words = ['Gazelle', 'Automobile', 'Mathematics', 'Elephant'] 

def chooseWord(wordList):
    word = list(wordList[randint(0, len(wordList)-1)])      # Get a random word from the list of words and store it as a list
    correctChars.extend(word[0] * word.count(word[0]))      # Add first and last character from word to the list of
    correctChars.extend(word[-1] * word.count(word[-1]))    # correct characters
    if " " in word:
        correctChars.extend(" " * word.count(" "))

    return word

def displayWord(word):
    for character in range(0, len(word)):   # Loop through every character inside the chosen word,
        if word[character] in correctChars: # displaying only characters which are already guessed correctly
            print(word[character], end="")  # and displaying the rest of characters with a '_'
        elif word[character] == " ":
            print(" ", end="")
        else:
            print("_", end="")            

def isCorrectChar(character, word):         # Function to check if the entered character is correct or not
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
    global newWord, correct
    while mistakes < 10:
        if newWord:     # Check if newWord is true
            if notFirstWord:
                for char in x:
                    msg += char     # from list to string
                print(msg + '\nWord guessed correctly! You have ' + str(score) + ' points.\n')

            msg = ''
            incorrectChars.clear()  # Clear the character lists
            correctChars.clear()
            x = chooseWord(words)   # Choose a new word
            
        displayWord(x)
        guess = input('\nGuess a letter: ')

        if not isCorrectChar(guess, x):
            print('\n"'+ guess + '" is the wrong guess! You have ' + str(mistakes) + ' mistake(s).\n')
        else:
            print('\nCorrect guess! You received 1 point\n')
        
        newWord = isWordCompleted(x)
        if newWord == False:        # Did this so the message for guessing a word correctly
            notFirstWord = True     # wouldn't show up when the game is started

    print('\nGame over! You have ' + str(score) + ' points!')

# Call functions
startGame()