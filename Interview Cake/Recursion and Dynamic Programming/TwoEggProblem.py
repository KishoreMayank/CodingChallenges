'''
Two Egg Problem:
    You are given two eggs and you need to figure out what is the max floor you can drop it from without breaking
'''

def eggDrop(n, k): # n -> number of eggs, k -> number of floors
    # A 2D table where entery eggFloor[i][j] will represent minimum 
    # number of trials needed for i eggs and j floors. 
    eggFloor = [[0] * (k + 1) for x in range(n+1)] 
  
    for i in range(1, n+1): # all of the first floor drops will take one drop
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0
  
    for j in range(1, k+1): # go though an increment the number of drops linearly for one egg
        eggFloor[1][j] = j 
  
    for i in range(2, n+1): 
        for j in range(2, k+1): 
            eggFloor[i][j] = float('inf')
            for x in range(1, j): 
                # max of the number of eggs you need from the xth floor
                    # if it does break, only need to look below, the problem reduces to x-1 floors and n-1 eggs
                    # if it doesn't break, only need to look above, the problem reduces to k - x floors and n eggs
                # you check the max for every floor and choose the one that yields the min
                res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x])
                if res < eggFloor[i][j]: 
                    eggFloor[i][j] = res 
  
    # eggFloor[n][k] holds the result 
    return eggFloor[n][k] 
  
def main():
    n = 2
    k = 100
    print("Minimum number of trials in worst case with" + str(n) + "eggs and " 
        + str(k) + " floors is " + str(eggDrop(n, k))) 
main()