# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open("/Users/ejds001/Desktop/words.txt", 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWord_List =[]#list of secretWord letters
    test_List = []#list of letters in secretWord_List also in lettersGuessed used to test if word guessed
    for x in secretWord: #for every letter in secretWord
        secretWord_List.append(x)#add to secretWord_List
    for val in secretWord_List: #for every val in secretWord_List
        if val in lettersGuessed: #if that val is in lettersGuessed
            test_List.append(val) #add to test_List
    return secretWord_List == test_List #boolean that compares secretWord as list to test_List


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    Guessedword = [] #empty list that starts with n " _ " denoting n letters in secretWord
    secretWord_List =[] #list of secret word char
    for char in secretWord: #for each character in string secretWord
        Guessedword.append(" _ ") #add underscore to Guessedword List
        secretWord_List.append(char) #and add that character to List version of secretword
    for count,char in enumerate(secretWord_List): #for each char in secretWord_List, add count
        if char in lettersGuessed: #if char in secretWord_List also in lettersGuessed
             Guessedword[count] = char #replace item in Guessedword with corresponding letter at each count 
    return "".join(Guessedword) #turn list Guessedword into string


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string 
    Letters_List = [] #list of letters
    for char in string.ascii_lowercase: #for all lowercase letters in alphabet
        Letters_List.append(char) #add them to Letters_List above
    for char in lettersGuessed: #for all items in lettersGuessed
        if char in Letters_List: #if letters in Letters_List
            Letters_List.remove(char) #remove these letters
    return "".join(Letters_List) #return Letters_List as string

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = [] #list to keep track of lettersGuessed
    num_guesses = 8 #predefined limit on guesses
    print "Welcome to the game Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."#introduces game and length of word
    while num_guesses > 0 and isWordGuessed(secretWord, lettersGuessed) == False:#loops while they're still more than 8 guesses remaining and the word has not been guessed
        print " ------------- "
        print "You have " + str(num_guesses) + " guesses left." #established number of guessed to user
        print "Available letters: " + getAvailableLetters(lettersGuessed) #shows possible letters
        guess = raw_input("Please guess a letter:" ) #prompts user for input of letter
        guessInLowerCase = guess.lower() #converts input to lowercase
        lettersGuessed.append(guessInLowerCase) #adds lowercase input to lettersGuessed list
        if lettersGuessed.count(guessInLowerCase) <= 1: #controls to make guessInLowerCase has not already been guessed before evaluating further if statements
            if guessInLowerCase in secretWord: 
                print "Good guess: " + getGuessedWord(secretWord, lettersGuessed) #gives user feedback that they guessed a correct letter and shows them their updated guessed word
            elif guessInLowerCase not in secretWord:
                print "Oops! That letter is not in my word:" + getGuessedWord(secretWord, lettersGuessed)
                num_guesses -= 1 #informs user letter not in word and substract guess
        else:#once a letter has been guessed above, a prompt informs user 
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
    print " ------------- "
    #now busted out of loop, either the word has been guessed, or no, and the number of guesses has been exhausted
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print "Congratulations, you won!"
    else:
        print "Sorry, you ran out of guesses. The word was " + secretWord



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
