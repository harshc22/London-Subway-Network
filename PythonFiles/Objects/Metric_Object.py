import csv


class Metric:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.data = self.read_file()


    #Update filename
    def set_filename(self,filename):
        self.filename = filename


    #Read csv file given file name
    def read_file(self):
        
        #Open london.connections.csv file
        connections_file = open(self.filename)
        csvreader = csv.reader(connections_file)


        #Extract interger data as string, convert to int or float later    
        self.data = []
        for row in csvreader:
            self.data.append(row)
            for i in range(len(row)):
                try: 
                    row[i] = float(row[i])
                except:
                    pass
 

        #print(self.data)
        connections_file.close()

        return self.data


    #if changes are made to data, a new file with same filename  
    def update_data(self):
        self.data = self.read_file(self.filename)

    
    #Return the first row of data (ie. Headers) 
    def get_headers(self):
        return self.data[0]


    #sort data based on given index if that is requried, index is the index of the list that is used to sort the data
    def sort_index(self, index:int):
        #sort form 1 to n-1
        #given and index, sort list based on index 
        #insertion sort, Source: GeekforGeeks, adpated

        #Range: start at 1, 1st element in data is list of headers
        for i in range(1,len(self.data)):

            key = self.data[i][index]

            j = i-1
            while j >=1 and key < self.data[j][index]:
                self.data[j+1][index] = self.data[j][index]
                j-=1

            self.data[j+1][index] = key 

