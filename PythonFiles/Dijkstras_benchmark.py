'''
input: metric obejct 
output: 
'''
#Import Objects
from Objects.Line_Object import Line
from Objects.Edge_Object import Edge 
from Objects.Node_Object import Node
from Objects.Metric_Object import Metric

#Import Creators 
from GraphCreation.NodeCreator import NodeCreator
from GraphCreation.LineCreator import LineCreator
from GraphCreation.EdgeCreator import EdgeCreator

from Algorithms.Dijkstras import DijkstrasAlgo
from GraphCreation.Graph import Graph

import time
import random 

class Tester():
    def __init__(self, nodes, lines, edges) -> None:
        self.nodes = nodes
        self.lines = lines
        self.edges = edges

    def create(self, source):  
        

        #Create Creator objects 
        self.nodes = NodeCreator(self.nodes)
        self.nodes.node_creator() #no input as default is 0

        #print(self.nodes.nodes)
        
        self.lines = LineCreator(self.lines)
        self.lines.line_creator() #no input as default is 0 

        #metric object -> connections.csv, line object -> dictionary, node object -> dictionary 
        self.edges = EdgeCreator(self.edges,self.lines,self.nodes)
        self.edges.edge_creator()

        #print(self.edges.edges)

        #Create grpah
        graph=Graph(self.nodes.nodes,self.edges.edges)
    

        start = time.process_time()
        #Run DijkstrasAlgo
        g = DijkstrasAlgo(len(graph.matrix)) #input: #of nodes (len of matrix ie. 5x5 -> 5) 
        g.graph = graph.matrix #getting matrix 
        g.dijkstra(source)  #input: source node 0 <= input <= nodes.len
        
        time.sleep(3)


        end = time.process_time()

        return end - start

