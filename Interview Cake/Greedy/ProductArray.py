'''
Product Array:
    Write a function that takes a list of integers and returns a list of the products.
'''

def product_array(int_list):

    if not int_list or len(int_list) == 1:
        raise IndexError('Too few elements')
        
    output = [1] * (len(int_list))
    product = 1
    for i in range(len(int_list)): # go through and add everything before it
        output[i] *= product
        product *= int_list[i]
        
    product = 1 # reset the product to 1
    for j in range(len(int_list) - 1, -1, -1): # then add everything in front
        output[j] *= product
        product *= int_list[j]

    return output



