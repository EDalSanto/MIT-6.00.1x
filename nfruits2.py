def nfruits2(fruit, eaten): 
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
    for key in fruit:
        if key in eaten:
            fruit[key] -= eaten.count(key)
            if key == eaten[-1]:
                fruit[key] += len(eaten)-eaten.count(key)
            else: 
                fruit[key] += len(eaten[:-1])-eaten.count(key)
    return max(fruit.values())