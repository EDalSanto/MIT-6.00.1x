def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    Letters_List = []
    for char in string.ascii_lowercase:
        Letters_List.append(char)
    for char in lettersGuessed:
        if char in Letters_List: 
            Letters_List.remove(char)
    return "".join(Letters_List)
        

