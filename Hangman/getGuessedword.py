def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    Guessedword = [] #empty list that starts with n " _ " denoting n lettes in secretWord
    secretWord_List =[] #list of secret word char
    for char in secretWord: #for each character in string secretWord
        Guessedword.append(" _ ") #add underscore to Guessedword List
        secretWord_List.append(char) #and add that character to List version of secretword
    for count,char in enumerate(secretWord_List): #for each char in secretWord_List, add index
        if char in lettersGuessed:
             Guessedword[count] = char
    return "".join(Guessedword)

   
  
