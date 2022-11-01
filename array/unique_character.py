# Here using the while loop if any character matches return False else return true
def uni_char(s):
    l = len(s)
    i = 1
    while i < l:
        if s[i] == s[i-1]:
            return False
        i += 1
    return True

print(uni_char("aaabsjdddkds"))
print(uni_char("abcdef"))
print(uni_char("aabcdef"))


# Simply used the set function of python to find unique character
def uni_char2(s):
    return len(set(s)) == len(s)

print(uni_char2("aaabsjdddkds"))
print(uni_char2("abcdef"))
print(uni_char2("aabcdef"))
