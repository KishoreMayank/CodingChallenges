'''
Power Set:
    Return all the subsets of a set
'''

def getSubsets(sets, index):
    allSets = []
    if len(sets) == index: # base case, add an empty set
        if [] not in allSets:
            allSets.append([])
    else:
        allSets = getSubsets(sets, index+1) # recurse to the end of the array and add the empty set
        item = sets[index] # get the element at index
        moreSets = []
        for subset in allSets: # for all the subsets in allSubset
            newSets = []
            [newSets.append(value) for value in subset if value not in newSets] # create a new subset with the existing val
            newSets.append(item) # add the new item to the end of the subset
            moreSets.append(newSets) # then add it to the set of subsets
        [allSets.append(value) for value in moreSets if value not in newSets] # add this new set to the total set
    return allSets

print(getSubsets([1,2], 0))