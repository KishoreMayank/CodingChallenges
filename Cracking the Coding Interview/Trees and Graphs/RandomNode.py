'''
Random Node:
    A binary tree class that can return random node
'''
import random

class Node():
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right
    self.count = 1 # each node has a count of the number of children plus itself
    if self.left:
      self.count += self.left.count
    if self.right:
      self.count += self.right.count

  def get_random_node(self):
    rand_int = random.randint(0, self.count - 1) # will return a number from 0 to (count of the root's children)
    return self.get_numbered_node(rand_int)

  def get_numbered_node(self, number):
    if number == 0:
      return self
    if self.left:
      if number - 1 < self.left.count: # if the number - 1 is less, then go left and subtract 1 (trying to get to 0)
        return self.left.get_numbered_node(number - 1)
      elif self.right: # if not, go right and subtrack 1 and the count at the left
        return self.right.get_numbered_node(number - 1 - self.left.count)
    if self.right: # otherwise go right
      return self.right.get_numbered_node(number - 1)
    return None
