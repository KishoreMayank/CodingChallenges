'''
Queue with Two Stacks:
    Implement a queue with two stacks
'''
class QueueTwoStacks:
    
    def __init__(self):
        self.in_stack  = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:

            while len(self.in_stack) > 0: # Move items from in_stack to out_stack, reversing order
                self.out_stack.append(self.in_stack.pop())

            if len(self.out_stack) == 0: # If out_stack is still empty, raise an error
                raise IndexError("Can't dequeue from empty queue!")

        return self.out_stack.pop()


