# Polymorphism - overloading and overriding

# Polymorphism means same function name (but different signatures) being used for different types
# Function overloading - same function name but different parameters
# Fn. overriding - 

l=[10,20,30,40,50]
print(len(l))
s="Subham "
print(len(s))

class ws :
    def display(self,name=''):
        print("Welcome to WS Cubetech"+name)

class IIP(ws) :
    def display(self):
        super().display()
        print("Nikal ja yahan se")

obj=ws()
obj.display()
obj.display(" Python")

a=IIP()
a.display()










