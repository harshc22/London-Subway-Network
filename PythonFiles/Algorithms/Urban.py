from Algorithms.Components import Components
from Objects.Edge_Object import Edge
from Objects.Node_Object import Node 

def UrbanPlanner(nodes,edges):
    size=maxZone(nodes)
    zone_vertices=[0]*size

    #stores the number of vertices of each zone 
    for node in nodes:
        zone_vertices[node.zone-1]+=1
    for i in range(size):
        zone_edges=[]
        zone_connected=[]
        for edge in edges:
            one=edge.node1
            two=edge.node2
            if one.zone==two.zone and one.zone==(i+1):
                zone_edges.append([one.station_id,two.station_id])
            else:
                zone_connected.append(two.station_id)
        print(zone_vertices[i])
        print(zone_edges)
        count=Components.countComponents(len(nodes),zone_edges)
        print (count)
        print (zone_connected)

def maxZone(nodes):
    max=0
    for node in nodes:
        if node.zone>max:
            max=node.zone
    return max 
