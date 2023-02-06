'''
Description:
#Takes information form 'london.lines.csv' to create a Line object
#Stores line number, line name, line colour, and stripe within the object 
'''

class Line:
    def __init__(self, line, name, colour, stripe) -> None:
        self.line = line
        self.name = name
        self.colour = colour 
        #Stripe appears "NULL in the london.lines.cvs file in some spots
        if stripe != "NULL":
            self.stripe = stripe
        else:
            self.stripe = None

    #add a property to the Line Object key-value pair -> attr-value pair 
    def add_proeprty(self, attr, value):
        setattr(self, attr, value)

    #return properties of the Line oject 
    def get_properties(self):
        return __dict__
    
    
