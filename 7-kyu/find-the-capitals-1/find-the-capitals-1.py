def capitals(word):
    #your code here
    # create empty list
    word_list = []
    # turn word into list
    for l in word:
        word_list.append(l)
    
    new_list = []
    
    for i, l in enumerate(word_list):
        if l == l.upper():
            new_list.append(i)
        else:
            continue
    return new_list
        