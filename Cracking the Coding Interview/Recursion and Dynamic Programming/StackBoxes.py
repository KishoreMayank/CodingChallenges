'''
Stack of Boxes:
    Stack of n boxes, with width, heights, and depths. Can only be stacked on larger bottoms. Find the largest stack
'''

def stack_boxes(boxes):
    sorted_boxes = sorted(boxes, lambda a, b: a.height > b.height) # Sort the boxes based on the height
    return stack_more_boxes(sorted_boxes, None, 0)

def stack_more_boxes(boxes, base, index):
    if index >= len(boxes):
        return 0
    without_box_height = stack_more_boxes(boxes, base, index + 1) # this gets a lone box to add
    box = boxes[index] # get the box
    if (not base) or box.fits_on(base):
        with_box_height = box.height + stack_more_boxes(boxes, box, index + 1)
        if with_box_height > without_box_height: # if the height with the new box is more, add it
            return with_box_height
    return without_box_height

class Box():
  def __init__(self, height, width, depth):
    self.height, self.width, self.depth = height, width, depth
  
  def fits_on(self, base):
    return base.height > self.height and \
           base.width  > self.width  and \
           base.depth  > self.depth