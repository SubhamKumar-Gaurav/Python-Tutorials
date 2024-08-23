# Object Oriented Programming in Python _ OOPs in Python

# Class - blueprint for the object , a template for a lot of functions
# we can define functions and variables into it
# Class ke andar kabhi object nahi banta
# Whenever you create a fn. inside a class , always pass an argument , it will act as an object


class DemoClass :
    a=10
    b=20
    c=30
    def sumvalue(self) :
        print(20+30)


demoobject=DemoClass()   #variable name , class defining - now it became object
print(demoobject.a)
print(demoobject.b)
print(demoobject.c)
demoobject.sumvalue() 


