'''
Input: metric object (london.lines.csv)
Output: Line dictionary (accesses via <LineCreatorObject>.linedic)
'''
from Objects.Line_Object import Line
from Objects.Metric_Object import Metric

class LineCreator:
    def __init__(self, metric) -> None:
        self.metric = metric
        self.linedic = {}
        


    def line_creator(self, line_num=0):
        #line_num is the column in metric data that contains the line number
        #gives flexibility to user to decide how they want to access dictionary
        #default is 0 

        data = self.metric.data

        #start a 1 b/c data[0] is a list of headers 
        for i in range(1,len((data))):
            
            n = Line(data[i][0], data[i][1], data[i][2], data[i][3])

            self.linedic[data[i][line_num]] = n
        