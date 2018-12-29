'''
Sum Lists 2:
    Same as tot lists but the numbers are in the right order
    Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 8 -> 0 -> 7
'''
def addTwoNumbers(l1, l2):
        s1 = []
        s2 = []
        
        while l1:
            s1.append(l1.val) # push in all of l1
            l1 = l1.next

        while l2:
            s2.append(l2.val) # push in all od l2
            l2 = l2.next
        
        tot = 0
        output = ListNode(0)
        while s1 or s2:
            if s1:
                tot += s1.pop()
            if s2: 
                tot += s2.pop()
            output.val = tot % 10 # set the value of the node
            head = ListNode(tot // 10) # put the value of the carry into the node
            head.next = output # set the next of the head to the current node
            output = head # move output to the head (because the head has the carry amount) 
            tot = tot // 10 # initialize tot for the next loop with the carry amount
        
        if output.val == 0:
            return output.next # if the carry was 0

        return output # otherwise return the head

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None