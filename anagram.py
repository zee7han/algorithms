# First approach simple based on sorting
def anagram(s1, s2):
    # Replace the whitespaces and  convert all of them to in lower case
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    # Sort the both string and make comparison between them
    return sorted(s1) == sorted(s2)


print(anagram("dog","god"))
print(anagram("no one is here", "someone is here"))


# Second approach based on the dictionary to maintain the count of each letter and handling the edge cases.
def anagram2(s1, s2):
    # Replace the whitespaces and  convert all of them to in lower case
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Handle the edge cases
    if len(s1) != len(s2):
        return False

    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        if not letter in count:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        if not letter in count:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False
        return True


print(anagram2("dog","god"))
print(anagram2("no one is here", "someone is here"))
