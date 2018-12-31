'''
Robot Grid:
    Create an algorithm to find a path for the robot from the top left to the bottom right only going down or right
'''

def getPath(maze):
    if maze == None or len(maze) == 0:
        return None
    path = []
    failedPoints = [] # keep track of all of the points that don't lead to a path
    if isPath(maze, len(maze)-1, len(maze[0])-1, path, failedPoints):  # start from the bottom right
        return path
    return None

def isPath(maze, row, col, path, failedPoints):
    if col < 0 or row < 0 or not maze[row][col]: # if out of bounds or blocked, don't return
        return False
    
    point = (row,col)

    if point in failedPoints: # if the cell has been visited, just return
        return False

    isAtOrigin = (row == 0) and (col == 0)

    # If there's a path from start to my current location, add my location
    # Recurse going to the left and going up and check if it is valid and not visited
    # If so, return and append the point accoringly to the path
    if isAtOrigin or isPath(maze, row, col-1, path, failedPoints) or isPath(maze, row-1, col, path, failedPoints):
        path.append(point)
        return True

    failedPoints.append(point) 
    return False