import string

def histo():
    # open and read file
    with open('robin.txt', 'r') as f:
        file = f.read()

    # split strings at whitespace
    words = file.split()
    # justify to left by using longest word
    longest_word = ''
    # loop through words
    for i in range(len(words)):
        new_word = ''
        # ignore special characters
        for j in words[i]:
            # using alnum string method, add only alphanumeric characters to new word
            if j.isalnum():
                new_word += j
        # ignore case - change everything to lowercase
        words[i] = new_word.lower()
        # if length of new word is longer than longest word
        if len(words[i]) > len(longest_word):
            # assign new word to longest word
            longest_word = words[i]
    
    # store count of word frequency in dict
    count = {}

    # loop through and count number of words
    for word in words:
        # if word in count, add # for each occurrence
        if word in count:
            count[word] += '#'
        # word not in count, assign # for that word
        else:
            count[word] = '#'

    # sort by number of frequency
    num_of_freq = {key: val for key, val in sorted(
        count.items(), key=lambda e: len(e[1]), reverse=True
    )}

    # sort alphabetically
    freq_by_alpha = {key: val for key, val in sorted(
        count.items(), key=lambda e: e
    )}

    # print number of frequency
    for key in num_of_freq:
        print(f"""{key.ljust(len(longest_word), ' ')} {num_of_freq[key]}""") #ljust string method returns string left justified in a string of length width

    # print in alphabetical order
    for key in freq_by_alpha:
        print(f"""{key.ljust(len(longest_word), ' ')} {freq_by_alpha[key]}""")

print(histo())