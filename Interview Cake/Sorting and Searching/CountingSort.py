'''
Counting Sort:
    Sort an array in descending order with a given highest possible score
'''

def sort_scores(unsorted, highest_possible):

    arr = [0] * highest_possible # initialize an array of length max
    for x in unsorted:
        arr[x] += 1 # add at every index where there is a mathc
    
    output = []
    for i in range(len(arr) - 1, -1, -1): # range function going backward
        for x in range(arr[i]):
            output.append(i) # append for every instance of the number 

    return output