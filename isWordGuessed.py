def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWord_List =[]
    test_List = []
    for x in secretWord:
        secretWord_List.append(x)
    for val in secretWord_List:
        if val in lettersGuessed:
            test_List.append(val)
    return secretWord_List == test_List
    
