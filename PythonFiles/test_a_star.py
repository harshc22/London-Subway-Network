import pytest
from Objects.Node_Object import Node
from Objects.Edge_Object import Edge
from GraphCreation.Graph import Graph
from Algorithms.A import AStar_Solver
def test_a_star():
    node1=Node(11,51.5226,-0.1571,"Baker Street",5)
    node2=Node(3,51.5225,-0.1631,"Maryleone",2)
    node3=Node(2,51.5234,-0.1466,"Regent's Park",2)
    node4=Node(4,51.508,-0.1247,"Charing Cross",1)
    node5=Node(5,51.5074,-0.1223,"Embankment",3)
    node6=Node(8,51.5098,-0.0766,"Tower Hill",2)

    edge1=Edge(node1,node2,1,1)
    edge2=Edge(node1,node3,2,2)
    edge3=Edge(node4,node5,7,1)
    edge4=Edge(node3,node6,2,2)

    nodes=[node1,node2,node3,node4,node5,node6]
    edges=[edge1,edge2,edge3,edge4]

    graph=Graph(nodes,edges)
    a=AStar_Solver(node2.station_id,node2.lat,node2.long,node6.station_id,node6.lat,node6.long,graph.getMatrix(),nodes)
    assert a.Solve()==[3, 11, 2, 8]