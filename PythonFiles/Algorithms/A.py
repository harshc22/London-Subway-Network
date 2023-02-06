from queue import PriorityQueue
from GraphCreation.Graph_functions import Graph_functions
from Objects.Node_Object import Node
#Importing priority queue data sctructure and graph functions 

class State(object):
    def __init__(self,value,value_lat,value_long,parent,matrix,nodes,start=0,start_lat=0,start_long=0,goal=0,goal_lat=0,goal_long=0):
        #Base class to store the imperative stuff for A star algorithm
        #construstor gets the value of nodes and the latitude and longitude of starting and ending node
        self.children=[] #stores neighbors 
        self.parent=parent 
        self.value=value
        self.dist=0 #place holder 
        self.matrix=matrix #graph matrix 
        self.value_lat=value_lat
        self.value_long=value_long
        self.start_lat=start_lat
        self.start_long=start_long
        self.goal_lat=goal_lat
        self.goal_long=goal_long
        self.nodes=nodes #list of nodes 

        #If a parent is passed in the constructor, update the parent path and the parent node
        if parent:
            self.path= parent.path[:] #copies a list 
            self.path.append(value)
            self.start=parent.start
            self.goal=parent.goal
            self.matrix=matrix
            self.value_lat=value_lat
            self.value_long=value_long
            self.start_lat=start_lat
            self.start_long=start_long
            self.goal_lat=goal_lat
            self.goal_long=goal_long
            self.nodes=nodes
        
        #If a parent is not given 
        else:
            self.path=[value]
            self.start=start
            self.goal=goal
            self.matrix=matrix
            self.value_lat=value_lat
            self.value_long=value_long
            self.start_lat=start_lat
            self.start_long=start_long
            self.goal_lat=goal_lat
            self.goal_long=goal_long
            self.nodes=nodes

    #used for heuristic in State_matrix class   
    def heuristic(self):
        pass
    #Used to find the neighour nodes in State_matrix class 
    def adjacent(self):
        pass

class State_matrix(State):
    def __init__(self,value,value_lat,value_long,parent,matrix,nodes,start=0,start_lat=0,start_long=0,goal=0,goal_lat=0,goal_long=0):
        super(State_matrix,self).__init__(value,value_lat,value_long,parent,matrix,nodes,start,start_lat,start_long,goal,goal_lat,goal_long)
        self.dist=self.heuristic()

    def heuristic(self):
        if self.value==self.goal:
            return 0 #if the goal is reached, return zero
        #finds the distance using the graph function by sending coordinates 
        dist=Graph_functions.distance(self.value_lat,self.value_long,self.goal_lat,self.goal_long)
        return dist
    
    #generates the neighbor nodes 
    def adjacent(self):
        if not self.children: #if not is children list 
            for i in range (len(self.matrix)):
                if ((self.matrix[int(self.value)-1][i] != 0)): #not zero means there is connection to the node
                    for node in self.nodes:
                        if node.station_id==(i+1): #finds the coordinates for that neighbor node
                            lat=node.lat
                            long=node.long

                    #create a child and pass the current node as the parent 
                    child=State_matrix((i+1),lat,long,self,self.matrix,self.nodes)

                    self.children.append(child) #add that child to our list 


class AStar_Solver:
    def __init__(self,start,start_lat,start_long,goal,goal_lat,goal_long,matrix,nodes):
        self.path=[] #stores the solution
        self.visitedQueue=[] #stores the visited nodes
        self.priorityQueue= PriorityQueue()
        self.start=start
        self.start_lat=start_lat
        self.start_long=start_long
        self.goal=goal
        self.goal_lat=goal_lat
        self.goal_long=goal_long
        self.matrix=matrix
        self.nodes=nodes

    def Solve(self):
        #creates a start state with no parent 
        startState=State_matrix(self.start,self.start_lat,self.start_long,0,self.matrix,self.nodes,self.start,self.start_lat,self.start_long,self.goal,self.goal_lat,self.goal_long)
        count=0

        #adds a tuple of 0 count and startstate
        self.priorityQueue.put((0,count,startState))
        
        #while the path is empty and priority queue has a size
        while (not self.path and self.priorityQueue.qsize()):
            closestChild = self.priorityQueue.get()[2] #gets the state
            closestChild.adjacent() #gets neighbors 
            self.visitedQueue.append(closestChild.value) #updates the visited queue

            for child in closestChild.children: #go through all children
                if child.value not in self.visitedQueue: #if the children is not visited
                    count+=1
                    
                    if not child.dist: #if the child distance is not zero
                        self.path=child.path
                        break
                    self.priorityQueue.put(((child.dist),count,child))
        if not self.path: #if a path is not found
            print ("Not possible")
        print (self.path)
        return self.path #returns the path 




                



        




    



