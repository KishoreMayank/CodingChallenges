'''
Route Between Nodes:
    Given a directed graph, figure out if there is a route between nodes.
'''

from collections import defaultdict

class Graph: 
    def __init__(self): # Constructor
        self.graph = defaultdict(list) # default dictionary to store graph 
  
    def addEdge(self,u,v): # function to add an edge to graph 
        self.graph[u].append(v) 
 
    def BFS(self, start, end): # find a path between the nodes
  
        visited = set() # Create a visited set

        queue = []
        queue.append(start) # Mark the source node as visited and enqueue it 
        visited.add(start)
  
        while queue: 
            curr = queue.pop(0) # pop from the queue
  
            for node in self.graph[curr]: # get all the adjacent vertices, of the current dequeued vertex 
                if node not in visited: # if the adjacent has not been visited, enqueue it
                    if  curr == end: # if it queals the end, return true
                        return True
                    queue.append(node) 
                    visited.add(node)
        return False