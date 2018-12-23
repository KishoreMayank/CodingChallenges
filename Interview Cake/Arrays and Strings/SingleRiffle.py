'''
Single Riffle:
    write a function to tell us if a full deck of cardsshuffled_deck is a single riffle of two other halves half1 and half2.
    Input: [1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6]
    Output: True
'''

def is_single_riffle(half1, half2, shuffled_deck):
    i, j = 0, 0

    for card in shuffled_deck:
        if i <= len(half1) - 1 and card == half1[i]: # if half1 is not empty and the top is the same
            i += 1
        elif j <= len(half2) - 1 and card == half2[j]: # if half2 is not empty and the top is the same
            j += 1
        else: # top card does not match
            return False
    return True


