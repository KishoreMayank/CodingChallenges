'''
InPlace Shuffle
Write a function for doing an in-place shuffle of a list
'''
import random

def shuffle(the_list):

    for i in range(len(the_list)):
        randind = random.randrange(i, len(the_list) - 1) # find random index from current to end
        if randind != i:
            the_list[randind], the_list[i] = the_list[i], the_list[randind]


