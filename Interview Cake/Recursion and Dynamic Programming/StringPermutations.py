'''
String Permutations:
    Write a recursive function for generating all permutations of an input string.
'''

def get_permutations(string):

    if len(string) <= 1:
        return set([string]) # if we have the first character, then we can start the recursion

    all_but_last = string[:-1] # everything but the last
    last_char = string[-1] # the last charater

    permutations_all_but_last = get_permutations(all_but_last) # keep calling till there is one character

    # Put the last char in all possible positions for each of
    # the above permutations
    permutations = set()
    for substring in permutations_all_but_last: # for every character in the set
        for i in range(len(all_but_last) + 1): # at every index of current length + 1

            # permute by concatenating the strings together
            # go through the loop and for the indicies, you should be able to get outputs
            # ex: substring = 'a' and last_char = 'b'
                # i = 0; permutation = ('' + 'b' + 'a') -> 'ba'
                # i = 1; permutation = ('a' + 'b' + '') -> 'ab'
            permutation = (substring[:i] + last_char + substring[i:])
            permutations.add(permutation) # add each permutation to the overall set

    return permutations # return it to the -> permutations_all_but_last

def main():
    print(get_permutations('abc'))
    
main()


