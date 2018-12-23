'''
Reverse Words:
    Write a function that takes a message as a list of characters and reverses the order of the words in place
    Input:  message = [ 'c', 'a', 'k', 'e', ' ',
                        'p', 'o', 'u', 'n', 'd', ' ',
                        's', 't', 'e', 'a', 'l' ]
    Output: 'steal pound cake'
'''

def reverse_words(message):
    reverse_chars(message, 0, len(message)-1) # Reverse entire message

    start = 0

    for i in range(len(message) + 1):
        if (i == len(message)) or (message[i] == ' '): # Reached the end of a word
            reverse_chars(message, start, i - 1)
            start = i + 1

def reverse_chars(message, left, right):
    while left < right: # Walk towards the middle, from both sides
        message[left], message[right] = message[right], message[left] # Swap the left and right
        left  += 1
        right -= 1
