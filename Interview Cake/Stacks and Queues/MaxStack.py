'''
Max Stack:
    Use your Stack class to implement a new class MaxStack with a 
    method get_max() that returns the largest element in the stack.
'''
 
class MaxStack(object):
    
    def __init__(self):
        self.stack = []
        self.max = []

    def push(self, item):
        """Add a new item to the top of our stack."""
        self.stack.append(item)

        if not self.max or item >= self.max[-1]: # add if empty or if greater
            self.max.append(item)

    def pop(self):
        """Remove and return the top item from our stack."""
        item = self.stack.pop()

        if item == self.max[-1]: # pop if the same element
            self.max.pop()

        return item

    def get_max(self):
        """The last item in max is the max item in our stack."""
        return self.max[-1]


