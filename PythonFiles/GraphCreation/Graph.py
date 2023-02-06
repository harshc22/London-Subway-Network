'''
Description:
#Graph class creates the adjacency matrix
#input in a list of nodes and edges when constructing the class
'''

import matplotlib.pylab as plt 
from GraphCreation.Graph_functions import Graph_functions

class Graph:
    #creates a graph matrix 
    def __init__(self,nodes,edges):
        matrix=[]
        max=Graph_functions.max_node(nodes)
        for i in range (max): #creates the matrix big enough to store all data
            row=[]
            for j in range (max):
                row.append(0)
            matrix.append(row)
        
        for edge in edges: #for all edges
            rows=int(edge.node1.station_id)   #ADDED INT
            col=int(edge.node2.station_id)    #ADDED INT
            matrix [rows-1][col-1]=edge.time #weighted matrix 
            matrix [col-1][rows-1]=edge.time
        
        self.matrix=matrix

    def getMatrix(self):
        return self.matrix
