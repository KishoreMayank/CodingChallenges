'''
BST Sequences:
    Print all arrays that could have led to this tree.
'''
class Node:
    def __init__(self, key=None):
        self.data = key
        self.left = None
        self.right = None

def bstSequences(root):
    return permute([[]], [root])

def permute(permutations, options):
    if len(options) == 0:
        return permutations
    total_permutations = []
    for i in range(len(options)):
        option = options[i]
        new_options = options[:i] + options[i+1:]
        if option.left:
            new_options.append(option.left)
        if option.right:
            new_options.append(option.right)
        new_permutations = []
        for permutation in permutations:
            new_permutations.append(permutation[:])
        for new_permutation in new_permutations:
            new_permutation.append(option.data)
        total_permutations.extend(permute(new_permutations, new_options))
    return total_permutations

def main():
    node_2 = Node(2)

    node_1 = Node(1)
    node_2.left = node_1
    for sequence in bstSequences(node_2): print(sequence)
    print("")

    node_3 = Node(3)
    node_2.right = node_3
    for sequence in bstSequences(node_2): print(sequence)
    print("")

    node_5 = Node(5)
    node_3.right = node_5
    for sequence in bstSequences(node_2): print(sequence)
    print("")

    node_0 = Node(0)
    node_1.left = node_0
    for sequence in bstSequences(node_2): print(sequence)

main()
