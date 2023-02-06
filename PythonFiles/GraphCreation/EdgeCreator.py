'''
Input: metric object (london.connections.csv)
Output: Lines list (access via <EdgeCreatorObject>.edges)
'''

from Objects.Metric_Object import Metric
from Objects.Node_Object import Node 
from Objects.Edge_Object import Edge
from GraphCreation.NodeCreator import NodeCreator

#Takes 3 Objects, creates a node and edge objects 
#returns a list of edge & node objects 
#Edge input: node1, node2, line, time
#Take dictionary of edges, take Metric object -> connections, forms edges 
class EdgeCreator:
    def __init__(self, metric, lines, nodes) -> list:
        self.metric = metric
        self.nodes = nodes
        self.lines = lines
        self.edges = [] 


    def edge_creator(self):
        if self.edges != []:
            return self.edges

        for i in range(1,len(self.metric.data)):
            #access the dictionaries and create edges 
            edge = Edge(
                self.nodes.nodedic.get(self.metric.data[i][0]),
                self.nodes.nodedic.get(self.metric.data[i][1]),
                self.lines.linedic.get(self.metric.data[i][2]),
                self.metric.data[i][3]
                )
                
            self.edges.append(edge)

            

            