'''
Input: metric object (london.stations.csv)
Output: Node dictionary (accesses via <NodeCreatorObject>.nodedic)
'''
from Objects.Node_Object import Node
from Objects.Metric_Object import Metric


class NodeCreator:
    def __init__(self, metric) -> list:
        self.metric = metric
        self.nodedic = {}
        self.nodes = []
        

    #input: takes in station_id given by user, return None
    #Access dictionary with <NodeCreatorObject>.nodedic
    def node_creator(self, id=0):
        
        data = self.metric.data        

        #start a 1 b/c data[0] is a list of headers 
        for i in range(1,len((data))):
            n = Node(data[i][0], data[i][1], data[i][2], data[i][3],data[i][6], int(data[i][5]))
            self.nodes.append(n)
            #at a particular index specified by user, the node is added
            #this index is the id of the station
            self.nodedic[data[i][id]] = n

        

    