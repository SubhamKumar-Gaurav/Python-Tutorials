# Inheritance

# Single inheritance - inheriting one class from another class
# Multi-level inheritance - inheriting one class from another and the another from other class
# Multiple inheritance - inheriting two class in one class


# Single inheritance :
# class A :
#     def displayA(self):
#         print("Hey , guys ")
#
# class B(A) :
#     def displayB(self):
#         print("Welcome to my ")

# multi level inheritance :
class A :
    def displayA(self):
        print("Hey , guys ")

class B :
    def displayB(self):
        print("Welcome to my ")

class C(B) :
    def displayC(self):
        print("Youtube channel ")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC()



