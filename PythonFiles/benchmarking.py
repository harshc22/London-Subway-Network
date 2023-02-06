from Objects.Line_Object import Line
from Objects.Edge_Object import Edge 
from Objects.Node_Object import Node
from Objects.Metric_Object import Metric
from GraphCreation.Graph import Graph
import matplotlib.pyplot as plt 
from GraphCreation.Graph_functions import Graph_functions
from GraphCreation.NodeCreator import NodeCreator
from GraphCreation.LineCreator import LineCreator
from GraphCreation.EdgeCreator import EdgeCreator
from Algorithms.Dijkstras import DijkstrasAlgo
from Dijkstras_benchmark import Tester
from Astar_benchmark import A_Tester


def main():

    
    # #make metric objects
    nodes = Metric("_dataset\london.stations.csv")
    lines = Metric("_dataset\london.lines.csv")
    edges = Metric("_dataset\london.connections.csv")  

    
    n = NodeCreator(nodes)
    n.node_creator()

    l = LineCreator(lines)
    l.line_creator()

    e = EdgeCreator(edges,l,n)
    e.edge_creator()
    #print(e.edges)

    test = Tester(nodes, lines, edges)
    
    print(test.create(0))
    print("Dijkstra Time")

    test2=A_Tester(nodes,lines,edges)
    
    print(test2.create())
    print("A star Time")
    
    # source = 0
    # print(test.create(source))




    pass
    
main()


