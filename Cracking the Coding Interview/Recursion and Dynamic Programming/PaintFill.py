'''
Paint Fill:
    Given a 2D array, a point and a color, fill the surrounding area with the same init
'''

def paint_fill(arr, target, loc, init=None):
    dims = arr.shape
    if loc[0] >= dims[0] or loc[1] >= dims[1] or loc[0] < 0 or loc[1] < 0:
        return  # end recursion (1) if the loc is invalid
    if init is None:
        init = arr[loc[0], loc[1]]
    if arr[loc[0], loc[1]] == target or arr[loc[0], loc[1]] != init:
        return  # end recursion (2) if cell color is already the target color or (3) if  cell color is not initial color
    arr[loc[0], loc[1]] = target
    paint_fill(arr, target, (loc[0] - 1, loc[1]), init)
    paint_fill(arr, target, (loc[0] + 1, loc[1]), init)
    paint_fill(arr, target, (loc[0], loc[1] - 1), init)
    paint_fill(arr, target, (loc[0], loc[1] + 1), init)
    return