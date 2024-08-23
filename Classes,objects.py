# Class/Object

# Class - Object constructor , blueprint for creating objects
# instances - actual objects
# Class attribute can be accessed through an instance as well as directly through class name

class MyClass :
    x=5   # x is an attribute of the class MyClass  (class attribute)

p1=MyClass()        # p1 is an instance
print(p1.x)
print(MyClass.x)



# __init__ function :
class person :
    def __init__(self , name , age ):
        self.name = name
        self.age = age
p1=person("Subham" , 22 )
print(p1.name)
print(p1.age)



# __str__ function :
class person :
    def __init__(self , name , age ):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} {self.age}"
p1=person("Kunal" , 69)
print(p1.name,p1.age)



# Object method
class Person :
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self) :
        print("Hello , Myself " + self.name )

p3=Person("Subham",22)
p3.myfunc()

class person :
    def __init__(self , name , age ):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} {self.age}"
p1=person("Kunal" , 69)
p1.age=30    # Updated the value of age as 30
del p1.age   # Deleted the value of age
print(p1.name,p1.age)