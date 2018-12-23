'''
Merge Intervals:
    Write a function that takes a list of multiple meetings time ranges and returns a list of condensed ranges
    Input:  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    Output: [(0, 1), (3, 8), (9, 12)]
'''
def merge_ranges(meetings):
    
    # Merge meeting ranges
    meetings.sort(key = lambda x : x[0])
    merged = [] # Create a list for outputting the merged meetings

    for meeting in meetings:
        if not merged or merged[-1][1] < meeting[0]: # Check if the arr is empty or if the meeting overlaps
            merged.append(meeting)                   # Append if it is
        else:
            merged[-1] = (merged[-1][0], max(meeting[1], merged[-1][1]))

    return merged