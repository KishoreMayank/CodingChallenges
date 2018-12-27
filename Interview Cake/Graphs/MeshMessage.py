'''
Mesh Message:
    Find the shortest route for a message from one user (the sender) to another (the recipient). 
    Return a list of users that make up this route.
'''
def bfs_get_path(graph, start, end):

    if start not in graph or end not in graph: # error if the nodes are not in the graph
        raise Exception("start or end not in graph")

    visited = set() # a set of visited nodes
    parents = {} # a map that contains that shortest path from the child to the parent
    
    queue = [] # a queue to bfs
    queue.append(start)
    
    while queue:
        node = queue.pop(0)
        for neighbhor in graph[node]:
            if neighbhor not in visited:
                queue.append(neighbhor) # add all the neighbhors to the queue
                visited.add(neighbhor) # add the neighbhors to the visited set
                parents[neighbhor] = node # set the child : parent binding
    path = []
    curr = end # start at the end node
    while curr is not start: # build the path until the start value
        path.insert(0, curr)
        if curr not in parents: # if it gets to the node with no parent, then it is not possible
            return None
        curr = parents[curr] # go to the parent of the current
    
    path.insert(0, start) # finally, insert the start node in

    return path
