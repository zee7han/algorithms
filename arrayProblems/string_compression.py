# This solution using the for loop and not handling the edge cases
def compress(s):
    count = 1
    new_string = ""
    # Here we loop through the string from 1 to length of string
    for i in range(1,len(s)):
        # If character matches we increase the count
        if s[i] == s[i-1]:
            count += 1
        # character not matches we append the alphabet and its count to the str
        # set the count to 1
        else:
            new_string = new_string + s[i-1] + str(count)
            count =1
    # Here we are handling the last alphabet case to add it and its count
    new_string = new_string + s[i] + str(count)
    return new_string

print(compress("AAABBBCCCDDDEEahdkkewwwddddwwwwwq"))



# This solution is using the while loop
def compress1(s):
    r = ""
    l = len(s)
    # Handling the edge cases
    if l == 0:
        return ""
    if l == 1:
        return s + "1"
    # Initialize the index and count
    i = 1
    cnt = 1
    # While loop till index less than length
    while i < l:
        # If character matches we increase the count
        if s[i] == s[i-1]:
            cnt += 1
        # character not matches we append the alphabet and its count to the str
        # set the count to 1
        else:
            r = r + s[i-1] + str(cnt)
            cnt = 1
        # Increase the index
        i += 1
    # Here we are handling the last alphabet case to add it and its count
    r = r + s[i-1] + str(cnt)
    return r

print(compress1("AAABBBCCCDDDEEahdkkewwwddddwwwwwq"))
