def word_count(s):
    count = {}
    # change to all lowercase to make case insensitive
    words = s.lower()

    # ignore these characters " : ; , . - + = / \ | [ ] { } ( ) * ^ &
    ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(' ')
    # replace ignored characters with ''
    for char in ignore:
        words = words.replace(char, '')

    # split string at spaces to count total words in string
    words = words.split()
    
    # iterate through words
    for word in words:
        # if input contains no characters, return empty dictionary
        if word == '':
            return {}
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

    





if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))