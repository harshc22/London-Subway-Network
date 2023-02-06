'''
Description:
#Edge object takes in two nodes, the line connecting them, and time corresponding
#Node1, Node2 - Node Objects, Line - Line Object, time - float/int input 

'''
class Edge:
    def __init__(self, node1, node2, line, time):
        self.node1 = node1
        self.node2 = node2
        self.line = line
        self.time = time

    #add a property to the Edge Object key-value pair -> attr-value pair 
    def add_proeprty(self, attr, value):
        setattr(self, attr, value)

    #return properties of the Line oject 
    def get_properties(self):
        return __dict__