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

def main():
    '''
    print("Hello1")
    #Connections metric object
    connections = Metric("_dataset\london.connections.csv")

    print("Hello2")

    #Make line files and metric object of line files 
    linesfile = Metric("_dataset\london.lines.csv")
    lines = LineCreator(linesfile)

    print("Hello2")

    #Make node creator 
    nodefile = Metric("_dataset\london.stations.csv")
    nodes = NodeCreator(nodefile)

    print("Hello4")

    #make edgecreator 
    edges = EdgeCreator(connections, lines, nodes)

    edges.edge_creator()

    print(edges.edges)
    '''
    #added zone to node creation, reflected change here 
    node1=Node(1,51.5226,-0.1571,"Baker Street",5,1)
    node2=Node(3,51.5225,-0.1631,"Maryleone",2,1)
    node3=Node(2,51.5234,-0.1466,"Regent's Park",2,1)
    node4=Node(4,51.508,-0.1247,"Charing Cross",1,1)
    node5=Node(5,51.5074,-0.1223,"Embankment",3,1)
    node6=Node(6,51.6736,-0.607,"Amersham",1,1)
    node7=Node(7,51.5322,-0.1058,"Angel",1,1)
    node8=Node(8,51.5653,-0.1353,"Archway",1,2.5)
    node9=Node(9,51.6164,-0.1331,"Arnos Grove",1,4)
    node10=Node(10,51.5586,-0.1059,"Arsenal",1,2)
    node11=Node(11,51.5226,-0.1571,"Baker Street",5,1)
    node12=Node(12,51.4431,-0.1525,"Balham",1,3)
    node13=Node(13,51.5133,-0.0886,"Bank",4,1)
    node14=Node(14,51.5204,-0.0979,"Barbican",3,1)
    node15=Node(15,51.5396,0.081,"Barking",2,4)

    edge1=Edge(node1,node2,1,1)
    edge2=Edge(node1,node3,2,2)
    edge3=Edge(node4,node5,7,1)
    edge4 = Edge(node2, node4, 5, 12)
    edge5 = Edge(node6,node1,4,1)
    edge6 = Edge(node7,node6,3,3)
    edge7 = Edge(node8,node1,6,6)
    edge8 = Edge(node9,node3,4,1)
    edge9 = Edge(node10,node1,1,2)
    edge10 = Edge(node11,node1,9,7)
    edge11 = Edge(node12,node3,2,1)
    edge12 = Edge(node13,node8,6,3)
    edge13 = Edge(node14,node11,7,8)
    edge14 = Edge(node15,node14,2,4)

    nodes = [node1,node2,node3,node4,node5,node6,node7,node8,node9,node10,node11,node12,node13,node14,node15]
    edges = [edge1,edge2,edge3,edge4,edge5,edge6,edge7,edge8,edge9,edge10,edge11,edge12,edge13,edge14]

    graph=Graph(nodes,edges)
    
    #Running DijkstrasAlgo
    g = DijkstrasAlgo(len(nodes)) #input: #of verts 
    g.graph = graph.matrix #getting matrix 
    g.dijkstra(1)  #4 is source node



main()