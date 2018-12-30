'''
Paths with Sum:
   Method 2: Traverse through the tree using DFS. As we visit each node:

   1. Track its runningSum.We'll take this in as a parameter and immediately increment it by node.val
   2. Look up runningSum - targetSum in the hash table. The value there indicates the total number. Set totalPaths to this value
   3. If runningSum == targetSum in the hash table, then there's one additional path that starts at the root. Increment totalPaths.
   4. Update runningSum to the hash table.
   5. Recurse left and right, counting the number of paths with sum targetSum.
   6. After we're done recurring left and right, decrement the value of runningSum in the hash table. This is essentially
   backing out of our work; it reverses the changes to the hash table so that other nodes don't use it.

   Time Complexity: O(N), where N is the number of nodes in the tree. We
   travel to each node just once, doing O(1) operation each time.

   Space Complexity: O(logN) in a balanced tree. O(N) in an unbalanced tree.
'''


def paths_with_sum(bt, val):
   if bt is None:
       return None
   if bt.root is None:
       return 0
   sums_table = { 0 : 1 } # Keeps track of the number of times you've seen that sum (If sum = 0, one more path)
   return count_paths_with_sum(bt.root, 0, val, sums_table)

def count_paths_with_sum(x, running_sum, target_sum, sums_table):
   if x is None:
       return 0
   running_sum += x.data # Keep track of running sum
   if running_sum in sums_table:   # Track the running sum and keep track of the number of times it appeared
       sums_table[running_sum] += 1
   else:
       sums_table[running_sum] = 1
   if (running_sum - target_sum) in sums_table: # This indicates the total paths seen so far at that value
       total_paths = sums_table[running_sum - target_sum]
   else:
       total_paths = 0
   total_paths += count_paths_with_sum(x.left, running_sum, target_sum, sums_table) # Recurse right and left
   total_paths += count_paths_with_sum(x.right, running_sum, target_sum, sums_table)
   sums_table[running_sum] -= 1 # Backtracking so that the other nodes don't use the new value
   return total_paths


