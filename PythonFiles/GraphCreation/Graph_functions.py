'''
Description: 
#A class of functions that act on the Graph class 
#Each function has self-explanatory nodes
'''

import matplotlib.pylab as plt 
import matplotlib.pyplot as plt 
import pprint
from math import sin, cos, sqrt, atan2,radians
R = 6373.0 #constant used for calculating distance
class Graph_functions:
    
    #visualizer for the graph connections 
    def Graph_builder(connections):
        for edge in connections: #plots every edge with node id and line number
            x=([edge.node1.long,edge.node2.long])
            y=([edge.node1.lat,edge.node2.lat])
            midx,midy=Graph_functions.midpoint(edge.node1.long,edge.node2.long,edge.node1.lat,edge.node2.lat)
            plt.plot(x,y,'-o',  c='black', mfc='blue', mec='k')
            #plt.text(edge.node1.long,edge.node1.lat,edge.node1.station_id,verticalalignment='bottom', horizontalalignment='center')
            #plt.text(edge.node2.long,edge.node2.lat,edge.node2.station_id,verticalalignment='bottom', horizontalalignment='center')
            #plt.text(midx,midy,edge.line,verticalalignment='bottom', horizontalalignment='center',color='red')

        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.show()
    
    #calculates the average degree
    def average_degree(nodes):
        total=0
        for node in nodes: #degree of all nodes
            total+=node.degree
        return (total/len(nodes))
    def add_labels(x,y):
        for i in range(len(x)):
            plt.text((i+1),y[i],y[i])
    def node_graph(nodes): #graphs the distribution of node vs degree
        degree=Graph_functions.degree_list(nodes) #gets the degree data
        x= [*range(1,(len(degree)+1),1)]

        plt.bar(x,degree)
        Graph_functions.add_labels(x,degree)
        plt.title ('Distribution of Nodes degree')
        plt.xlabel ('degree')
        plt.ylabel ('number of nodes')
        plt.show()
        
    def degree_list(nodes):
        max=Graph_functions.max_degree(nodes) #max degree
        degree=[0]*max #makes array big enough for all degree
        for i in range (max):
            for node in nodes: 
                if (node.degree == (i+1)): #checks all degrees and adds one to corresponding index
                    degree[i]+=1
        return degree
        

    def max_degree(nodes): #finds the max degree
        max=0
        for node in nodes:
            if node.degree>max:
                max=node.degree
        return int(max)

    def midpoint(x1,x2,y1,y2): #calculates mid point of two coordinates
        midx=(x1+x2)/2
        midy=(y1+y2)/2
        return (midx,midy)

    def count_nodes(nodes): #returns node count
        return len(nodes)

    def count_edges(edges): #returns edge count 
        return len(edges)
    
    def max_node(nodes): #returns the node with maximum station_id
        max=0
        for node in nodes:
            if (node.station_id>max):
                max=node.station_id
        return int(max)
    
    def distance(start_lat,start_long,end_lat,end_long): #calculates the distance of two coordinates
        dlon = radians(end_long) - radians(start_long)
        dlat = radians(end_lat) - radians(start_lat)
        a = (sin(dlat/2))**2 + cos(radians(start_lat)) * cos(radians(end_lat)) * (sin(dlon/2))**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = R * c
        return round(distance,2)

        