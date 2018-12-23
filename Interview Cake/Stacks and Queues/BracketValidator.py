'''
Bracket Validator:
    Write a function to check whether the opener's and closers are properly nested
    Input: '{ [ ] ( ) }'
    Output: True
'''

def is_valid(string):
    open_close = {'(' : ')','{' : '}','[' : ']'}
    openers = set(open_close.keys())
    closers = set(open_close.values())

    stack = []
    for char in string:
        if char in openers:
            stack.append(char)
        elif char in closers:
            if not stack: # if the stack it empty it's false
                return False
            else:
                if not open_close[stack.pop()] == char: # if the closer does not corren
                    return False

    return not stack


