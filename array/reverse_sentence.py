# Here we are just using the python builtin functions to reversed the sentence string
def rev_word1(string):
    # split function split the function and store them in list then we reversed
    # the list and join them.
    return " ".join(reversed(string.split()))

print(rev_word1("you are here"))
print(rev_word1("    I am here"))
print(rev_word1("No I am not there    "))



# This function reversed the sentence but not eliminate the leading whitespaces
def rev_word2(string):
    spaces = " "
    lst = []
    index = 0
    start = 0
    # Here we are loop through the string
    for letter in string:
        # Check for the last index and append the last word into the list
        if index == len(string)-1:
            lst.append(string[start:index+1])
        # Here check for the whitespaces to break the sentence on word
        # and  set the start index for every new word
        if letter == spaces:
            lst.append(string[start:index])
            start = index+1
        # Increase the index on every iteration.
        index += 1
    return " ".join(lst[::-1])

print(rev_word2("you are here"))
print(rev_word2("    I am here"))
print(rev_word2("No I am not there    "))



# This function will eliminate the whitespaces as well as reversed the sentence
def rev_word(s):
    # This will fpr checking the whitespaces
    spaces = [" "]
    length = len(s)
    word = []
    # Here i is for maintaining the index of the character.
    i=0
    # Do the following till i less than length of the sentence
    while i < length:
        # Check for character is whitespaces or not if its not then we maintain
        # the word_start as start index and again used conditional loop if still
        # character persist then simply increase the i index.
        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in  spaces:
                i += 1
            # On nested while loop condition failure we append the word in list
            word.append(s[word_start:i])
        # Here we increase the index if a whitespaces occurs
        i += 1
    return " ".join(word[::-1])

print(rev_word("you are here"))
print(rev_word("    I am here"))
print(rev_word("No I am not there    "))
