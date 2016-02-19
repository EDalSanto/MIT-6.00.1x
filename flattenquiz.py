#Write a function to flatten a list. The list contains other lists, strings, or ints. 
#For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5]

#Recursion is extremely useful for this question. You will have to try to flatten every element of the original list. 
#To check whether an element can be flattened, the element must be another object of type list.

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flattened_list = []
    for item in aList:
        if type(item) == type([]):
            flattened_list.extend(flatten(item))
        else:
            flattened_list.append(item)
    return flattened_list
    


   


