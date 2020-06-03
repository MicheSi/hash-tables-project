def no_dups(s):
    # create dictonary for duplicate words
    duplicates = {}
    # create list to store string w/o duplicates
    no_duplicates = []
    # split string at spaces into list
    words = s.split(' ')
    # iterate through list
    for word in words:
        # if word not already in dictionary
        if word not in duplicates:
            duplicates[word] = 1
            # add word to list
            no_duplicates.append(word)
    # join words into a string with space in between them
    return ' '.join(no_duplicates)





if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))