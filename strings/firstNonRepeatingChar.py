# Python program to print the first non-repeating character 
NO_OF_CHARS = 256
  
# Returns an array of size 256 containg count 
# of characters in the passed char array 
def getCharCountArray(string): 
    count = [0] * NO_OF_CHARS 
    for i in string:
        print(ord(i))
        count[ord(i)]+=1
    return count

def firstNonRepeating(string): 
    count = getCharCountArray(string) 
    index = -1
    k = 0
  
    for i in string: 
        if count[ord(i)] == 1: 
            index = k 
            break
        k += 1
  
    return string[index]

print(firstNonRepeating("aabbcde"))
# print(firstNonRepeating("aabbdce"))