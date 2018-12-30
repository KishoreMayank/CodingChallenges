'''
Topological Sort:
    The linear ordering of vertices such that for every directed edge uv, vertex u comes before v
'''

from collections import defaultdict 
  
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) # use a defualt dict to initialize an empty list 
        self.V = vertices # No. of vertices 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def topologicalSort(self): 
        visited = [False] * self.V # initialize the verticies as not visited
        stack = [] 
  
        # Sort starting from all vertices one by one 
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i, visited, stack)

        print(stack) 

    def topologicalSortUtil(self, v, visited, stack): 
  
        visited[v] = True # make current node as visited
  
        for i in self.graph[v]: # for all of the verticies that are adjcacent 
            if visited[i] == False: 
                self.topologicalSortUtil(i, visited, stack) 

        stack.insert(0,v) # Push current vertex to stack which stores result 

g = Graph(6) 
g.addEdge(5, 2)
g.addEdge(5, 0) 
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
  
print("Following is a Topological Sort of the given graph")
g.topologicalSort() 