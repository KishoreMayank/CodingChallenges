'''
URLify:
    Write a method to replace all the spaces in a string with '%20'. The string has sufficient space to hold it
    Input:  "Mr John Smith    "
    Output: "Mr%20John%20Smith"
'''

def urlify(string, length): # takes in a string as a list
    new_index = len(string) # start from the back of the array

    for i in reversed(range(length)): # reverses the range
        if string[i] == ' ':
            string[new_index - 3 : new_index] = '%20' # when you find a space, replace it with chars
            new_index -= 3
        else:
            string[new_index - 1] = string[i] # otherwise, keep moving the characters one towards the back of the array
            new_index -= 1

    return string

def main():
    urlify(list('Mr John Smith    '), 13)
main()