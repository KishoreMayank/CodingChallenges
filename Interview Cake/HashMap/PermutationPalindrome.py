'''
Permutation Palindrome:
    Write an efficient function that checks whether any permutation of an input string is a palindrome.
    Ex: "ivicc" should return True
        "civil" should return False
'''

def permutation_palindrome(string):
    unpaired = set() # Track characters we've seen an odd number of times

    for char in string:
        if char in unpaired:
            unpaired.remove(char) # remove if even number of times
        else:
            unpaired.add(char) # add if odd number of times

    return len(unpaired) <= 1 # more than one odd means no permutation





