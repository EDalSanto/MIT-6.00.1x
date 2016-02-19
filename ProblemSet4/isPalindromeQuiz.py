#Write a Python function that returns True if aString is a palindrome 
#(reads the same forwards or reversed) and False otherwise. 
#Do not use Python's built-in reverse function or aString[::-1] to reverse strings.

#This function takes in a string and returns a boolean.

def isPalindrome(aString):
    '''
    aString: a string
    '''
    def reverse(aString):
        '''
        takes in string and reverses it
        '''
        if len(aString) == 0:
            return ""
        elif len(aString) == 1:
            return aString[0]
        else:
            return reverse(aString[1:]) + aString[0]        
    return aString == reverse(aString)
            