
from Objects.Line_Object import Line
from Objects.Edge_Object import Edge 
from Objects.Node_Object import Node
from Objects.Metric_Object import Metric
from GraphCreation.Graph import Graph
import matplotlib.pyplot as plt 
from GraphCreation.Graph_functions import Graph_functions
from GraphCreation.NodeCreator import NodeCreator
from Algorithms.A import AStar_Solver
from GraphCreation.LineCreator import LineCreator
from Algorithms.Subway import travelling_salesman_function
from Algorithms.Urban import UrbanPlanner
from GraphCreation.EdgeCreator import EdgeCreator
def main():
    '''
    node1=Node(11,51.5226,-0.1571,"Baker Street",5)
    node2=Node(3,51.5225,-0.1631,"Maryleone",2)
    node3=Node(2,51.5234,-0.1466,"Regent's Park",2)
    node4=Node(4,51.508,-0.1247,"Charing Cross",1)
    node5=Node(5,51.5074,-0.1223,"Embankment",3)

    edge1=Edge(node1,node2,1,1)
    edge2=Edge(node1,node3,2,2)
    edge3=Edge(node4,node5,7,1)

    connections=[edge1,edge2,edge3]
    nodes=[node1,node2,node3,node4,node5]
    edges=[edge1,edge2,edge3]

    print (Graph_functions.count_edges(edges))
    print (Graph_functions.count_nodes(nodes))
    graph=Graph(nodes,edges)
    print(Graph_functions.average_degree(nodes))
    Graph_functions.Graph_builder(connections)
    Graph_functions.node_graph(nodes)
    a=heuristic(nodes,node2)
    '''
    '''
    #Create Metric object 
    data = Metric("_dataset\london.stations.csv")
    # for i in data.data:
    #     print("row:", i)
    #print(data.data)
from queue import PriorityQueue

from Algorithms.A import AStar_Solver
def main():
    data = Metric("_dataset/london.stations.csv")

    #print(data.get_headers())

    #sorted list works, issue is that some id's may be missing
    data.sort_index(0)
    print(len(data.data))

    c = 0
    for i in range(len(data.data)):
        print("row: ",c,"\t",data.data[i])
         
        if c==189: c+=1
        if c!=data.data[i][0]: print("False")
        c+=1
    
    nodes = NodeCreator(data)
    nodes = nodes.node_creator()
    
    for i in nodes:
        print(i.get_properties())

    print(nodes)
    '''


    nodes = Metric("_dataset/london.stations.csv")
    lines = Metric("_dataset/london.lines.csv")
    edges = Metric("_dataset/london.connections.csv")


    n = NodeCreator(nodes)
    n.node_creator()

    l = LineCreator(lines)
    l.line_creator()

    e = EdgeCreator(edges,l,n)
    e.edge_creator()

    nodeset=set()
    for edge in e.edges:
        nodeset.add(edge.node1)
        nodeset.add(edge.node2)
    print("amount")
    check=list(range(304))
    print(len(nodeset))
    # nodes.node_creator(0)

    #print(nodes.nodedic.items())

    #print(nodes.node_creator())
    '''priorityQueue=PriorityQueue()
    priorityQueue.put((1,2,3))
    child = priorityQueue.get()[2]    
    print (child)
    node1=Node(0,51.5226,-0.1571,"Baker Street",5,1)
    node2=Node(1,51.5225,-0.1631,"Maryleone",2,1)
    node3=Node(2,51.5234,-0.1466,"Regent's Park",2,1)
    node4=Node(3,51.508,-0.1247,"Charing Cross",1,1)
    node5=Node(4,51.5074,-0.1223,"Embankment",3,2)
    node6=Node(5,51.5098,-0.0766,"Tower Hill",2,2)

    edge1=Edge(node1,node2,1,1)
    edge2=Edge(node3,node4,2,2)
    edge3=Edge(node5,node6,7,1)
    edge4=Edge(node3,node6,2,2)
    edge5=Edge(node2,node3,3,4)

    nodes=[node1,node2,node3,node4,node5,node6]
    edges=[edge1,edge2,edge3]
    UrbanPlanner(nodes,edges)'''

    #print (Graph_functions.count_edges(edges))
    #print (Graph_functions.count_nodes(nodes))
    graph=Graph(nodes,edges)
    #print (graph.getMatrix())
    #graph = [[0,15,1,11,1,0],[15,0,1,10,0,0],[1,1,0,1,0,4],[11,10,1,0,3,0],[1,0,0,3,0,0],[0,0,4,0,0,0]]
    '''subset=[node1,node2,node3,node4]
    s = 1
    res = travelling_salesman_function(graph.getMatrix(),subset,s)
    print(res)'''
    print("The number of nodes in the graph:")
    print(Graph_functions.count_nodes(n.nodes))
    print("The average degree of nodes is: ")
    print(Graph_functions.average_degree(n.nodes))
    print ("The number of Edges:")
    print(Graph_functions.count_edges(e.edges))

    Graph_functions.Graph_builder(e.edges)
    Graph_functions.node_graph(n.nodes)
    #a=heuristic(nodes,node2)

    #a=AStar_Solver(node2.station_id,node2.lat,node2.long,node6.station_id,node6.lat,node6.long,graph.getMatrix(),nodes)
    #a.Solve()
    
    #Create Metric object 
    #print(nodes)

    
if __name__ == "__main__":
    main()