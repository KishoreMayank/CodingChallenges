'''
Graph Coloring:
    Given an undirected graph with maximum degree D, find a graph coloring using at most D+1 colors.
'''

class GraphNode: # the definition of the graph node
    
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


def color_graph(graph, colors):

    for node in graph:
        illegal = [] # create an illegal list of colors based on the neighbors 
        for n in node.neighbors:
            if n == node:
                raise Exception()
            if n.color:
                illegal.append(n.color)
                
        for color in colors:
            if color not in illegal: # find a color that is not illegal and set the node's color to that
                node.color = color
                break

    return graph