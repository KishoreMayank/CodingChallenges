'''
Group Anagrams:
    Write a method to sort an array of strings so that all of the anagrams are next to each other.
'''

def GroupAnagrams(strings):
    anagrams = {}
    for i in range(len(strings)):
        key = "".join(sorted(strings[i].lower())) # get the key by sorting the word
        if key not in anagrams: # check if the dictionary has the key
            anagrams[key] = [] # if it doesn't, then add the key : []
        anagrams[key].append(strings[i]) # then add the string to the value list
    keys = anagrams.keys()
    index = 0
    for i in range(len(keys)): # build the sorted list
        values = anagrams.get(keys[i])
        for j in range(len(values)): # looping through every value in the key list
            strings[index] = values[j]
            index += 1
    return strings