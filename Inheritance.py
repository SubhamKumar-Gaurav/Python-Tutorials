# Inheritance

# Inheritance - allows us to define a class that inherits all the methods and properties from another class
# Parent class - also base class , class being inherited from
# Child class - also derived class , class that inherits from another class


class person :
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
x=person("Subham","Kumar")
x.printname()








