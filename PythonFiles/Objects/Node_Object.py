#Node oject will contain station information read from londom.stations.csv
#station: station id, degree: number of node connections
#Might make the non-relavent information in a Object Class to make Node construction easier 
#Assume station_id will never be set to None/NULL

class Node:
    def __init__(self, station_id, lat, long, station_name, degree, zone=0): 
        self.station_id = station_id
        self.lat = lat
        self.long = long
        self.station_name = station_name
        self.degree = degree
        self.zone = zone
        
    #add property to node if needed
    def add_proeprty(self, attr, value):
        setattr(self, attr, value)

    #add a property to the Line Object key-value pair -> attr-value pair 
    def get_properties(self):
        return __dict__
    
