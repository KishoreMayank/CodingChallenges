'''
Sum Lists:
    Given two numbers represented in reverse in a linked list, output the sum in reverse.
    Input: (7 -> 1 -> 6) + (5 -> 9 -> 2) - 617 + 295
    Ouput:  2 -> 1 -> 9 - 912
'''
def sum_lists(n1, n2):
    result = set() # l1 = LinkedList() IS THE CORRECT THING AT THIS LINE
    carry = 0
    while n1 or n2:
        result = carry # set the result as the current carry
        if n1:
            result += n1.value # if the is a node in the first list, add its value and increment
            n1 = n1.next
        if n2:
            result += n2.value # if the is a node in the second list, add its value and increment
            n2 = n2.next

        result.add(result % 10) # build the new linked list (mod 10 because if it is over 10 then it needs to have a carry)
        carry = result // 10 # do integer division to get the carry

    if carry:
        result.add(carry) # if there is a final carry, add it to the end

    return result
