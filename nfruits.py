def nfruits(fruit, eaten): 
    """
    fruit is a non-empty dictionary containing type of fruit 
    and its quantity initially with Python when he leaves home (length < 10)
    eaten is a 'string' pattern documenting types and # of fruits eaten along 
    journey.    
    After each fruit he eats (except the last one which he eats just on 
    reaching the campus), 
    adds 1 fruit of each type other than the one just had.
    returns max value of 3 keys in dict
    """
    #assert length of dict 'ifruits' is between 0 and 10
    assert 0 < len(fruit) < 10 
    #loop through fruits eaten to decrease value of key i in dict fruit
    for i in eaten:
        fruit[i] -= 1
    #loop through fruits eaten, exlcuding last 1, to increase value 
    #of other keys, non-i, in dict fruit
    for i in eaten[:-1]: 
        for key in fruit:
            if key != i:
                fruit[key] += 1
    return max(fruit.values())
          

