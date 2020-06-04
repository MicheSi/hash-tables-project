import random


# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
following_words = {}
start_word = {}
end_word = {}

words_array = words.split()

stop_punc = ['.', '?', '!']

# loops through words array
for i in range(len(words_array)):
    # if there is a next word, add it to the list
    if i + 1 < len(words_array):
        # if the word is already in the dict
        if words_array[i] in following_words:
            # add next word to following words dict
            following_words[words_array[i]].append(words_array[i + 1])
        else:
            # if word not already in dict, add that word
            following_words[words_array[i]] = [words_array[i + 1]]
     # otherwise no following words
    else:
        following_words[words_array[i]] = []

# TODO: construct 5 random sentences




# Loop through
# Print word
# If it's a 'stop" word, stop
# Else choose a random word to follow this one

