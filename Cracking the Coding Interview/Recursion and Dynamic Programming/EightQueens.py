'''
Eight Queens:
   Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board so that
   none of them share the same row, column or diagonal. In this case, "diagonal" means all
   diagonals, not just the two that bisect the board.
'''

def n_queens(n):
   ways = list()
   helper(n, 0, list(), ways)
   return ways

def helper(n, c, queens, ways):
    if c == n:
        ways.append(queens)
        return None
    for r in range(n):
        position = [ r, c ]
        if is_valid(position, queens): # checks to see if there are any queens in the same row or column or diagonal
            queens_cp = queens.copy() # makes a shallow copy so the copy doesn not reference queens (would be overwritten)
            queens_cp.append(position) 
            helper(n, c+1, queens_cp, ways)

def is_valid(position, queens):
    for queen in queens:
        if queen[0] == position[0]: # check the row
            return False
        if queen[1] == position[1]: # check the column
            return False
        if (abs(queen[0] - position[0]) == abs(queen[1] - position[1])): # check the diagonal
            return False
    return True


