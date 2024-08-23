# Method overloading and overriding

# Method overloading : one concept of polymorphism
# comes under th elements of OOPs
# It is worked in the same method names and different arguments
# Arguments different will be based on a number of arguments and types of arguments

# Method overriding :
# child overrides parent's function , implemented with inheritance also
# Mostly used for memory reducing processes



# Method overloading
print("Method overloading :")
class area :
    def find_area(self,a=None,b=None):
        if a!=None and b!=None :
            print("Area of Rectangle : " , (a*b))
        elif a!=None :
            print("Area of Square : " , (a*a))
        else :
            print("Nothing to find ")
obj=area()
obj.find_area()
obj.find_area(10)
obj.find_area(10,20)
print(" ")


# Method overriding
print("Method overriding : ")
class A :
    def ShowData(self):
        print("I am in A class ")
class B(A) :
    def ShowData(self):
        print("I am in B class ")
obj1=B()
obj1.ShowData()






