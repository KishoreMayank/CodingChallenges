'''
Parenthesis Matching:
    Given the index of the opening parenthesis, give the index of the close parenthesis
'''

def close_index(sentence, open_index):
    stack = []
    i = 0
    while i < len(sentence):
        if sentence[i] is '(': # push in all of the open parens
            stack.append(i)
        if sentence[i] is ')': # pop out the open parens when a close one comes
            out = stack.pop()
            if out is open_index: # if it is the index we are looking for, return index
                return i
        i += 1
    return -1