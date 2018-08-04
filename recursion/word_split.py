# check for whether the phrase will split in words of list available to us.
# Here we give output as parameter because dont want to Initialize
# at every recursive call.
def word_split(phrase, list_of_words, output = None):
    # Initialize onnly at first call.
    if output == None:
        output = []
    # Loop  through the words of list.
    for word in list_of_words:
        # check for phrase start with word or not if so then append to output.
        if phrase.startswith(word):
            output.append(word)
            # recursively call for remaining phrase and updated output.
            return word_split(phrase[len(word):],list_of_words,output)
    return output


print(word_split("hellohihow",["hello", "hi", "how"], ))
print(word_split("lohihow",["hello", "hi", "how"], ))
