# Methods and constructors

# Method ke andar self keyword ka use karte hai
# we cannot define or access a variable without the use of self
# Constructor - defined by __init__ keyword , a method which calls automatically



class DemoClass :
    a=10

    def __init__(self):
        print("Kuch nahi")
    def showvalue(self):
        print(self.a)
        # self.c=a*a   # Error
        self.c=self.a*self.a
        print(self.c)
    def showvalue1(self,a,b):
        print(a+b)

obj=DemoClass()
obj.showvalue()
obj.showvalue1(20,30)



