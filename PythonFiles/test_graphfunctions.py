import pytest 
from GraphCreation.Graph_functions import Graph_functions
from Objects.Node_Object import Node
from Objects.Edge_Object import Edge


def test_average_degree():
    node1=Node(11,51.5226,-0.1571,"Baker Street",5)
    node2=Node(3,51.5225,-0.1631,"Maryleone",2)
    node3=Node(2,51.5234,-0.1466,"Regent's Park",2)
    node4=Node(4,51.508,-0.1247,"Charing Cross",1)
    node5=Node(5,51.5074,-0.1223,"Embankment",3)
    node6=Node(263,51.5098,-0.0766,"Tower Hill",2)
    nodes=[node1,node2,node3,node4,node5,node6]
    assert Graph_functions.average_degree(nodes)== 2.5

def test_degree_list():
    node1=Node(11,51.5226,-0.1571,"Baker Street",5)
    node2=Node(3,51.5225,-0.1631,"Maryleone",2)
    node3=Node(2,51.5234,-0.1466,"Regent's Park",2)
    node4=Node(4,51.508,-0.1247,"Charing Cross",1)
    node5=Node(5,51.5074,-0.1223,"Embankment",3)
    node6=Node(8,51.5098,-0.0766,"Tower Hill",2)
    nodes=[node1,node2,node3,node4,node5,node6]
    assert Graph_functions.degree_list(nodes)==[1,3,1,0,1]

def test_max_degree():
    node1=Node(11,51.5226,-0.1571,"Baker Street",5)
    node2=Node(3,51.5225,-0.1631,"Maryleone",2)
    node3=Node(2,51.5234,-0.1466,"Regent's Park",2)
    node4=Node(4,51.508,-0.1247,"Charing Cross",1)
    node5=Node(5,51.5074,-0.1223,"Embankment",3)
    node6=Node(8,51.5098,-0.0766,"Tower Hill",2)
    nodes=[node1,node2,node3,node4,node5,node6]
    assert Graph_functions.max_degree(nodes)==5

def test_count_nodes():
    node1=Node(11,51.5226,-0.1571,"Baker Street",5)
    node2=Node(3,51.5225,-0.1631,"Maryleone",2)
    node3=Node(2,51.5234,-0.1466,"Regent's Park",2)
    node4=Node(4,51.508,-0.1247,"Charing Cross",1)
    node5=Node(5,51.5074,-0.1223,"Embankment",3)
    node6=Node(8,51.5098,-0.0766,"Tower Hill",2)
    nodes=[node1,node2,node3,node4,node5,node6]
    assert Graph_functions.count_nodes(nodes)==6

def test_max_node():
    node1=Node(11,51.5226,-0.1571,"Baker Street",5)
    node2=Node(3,51.5225,-0.1631,"Maryleone",2)
    node3=Node(2,51.5234,-0.1466,"Regent's Park",2)
    node4=Node(4,51.508,-0.1247,"Charing Cross",1)
    node5=Node(5,51.5074,-0.1223,"Embankment",3)
    node6=Node(8,51.5098,-0.0766,"Tower Hill",2)
    nodes=[node1,node2,node3,node4,node5,node6]
    assert Graph_functions.max_node(nodes)==11

def test_count_edges():
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
    edges=[edge1,edge2,edge3,edge4]
    assert Graph_functions.count_edges(edges)==4

def test_midpoint():
    x1=52
    x2=51
    y1=-0.1571
    y2=-0.1631
    assert Graph_functions.midpoint(x1,x2,y1,y2)==(51.5,-0.1601)

def test_distance():
    lat1 = 52.2296756
    lon1 = 21.0122287
    lat2 = 52.406374
    lon2 = 16.9251681
    assert Graph_functions.distance(lat1,lon1,lat2,lon2)==278.55