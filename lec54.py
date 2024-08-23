# Encapsulation

# An object variable should not always be directly accessible
# The methods can ensure the correct values are set. If an incorrect value is set , the method can return an error

# __ - to make private variable


class Student :
    __name="Hello"  # private variable
    def __init__(self):
        print(self.__name)
    def __displayinfo(self):
        print("Welcome back! ")


obj=Student()
print(obj.__name) # We cannot use this as its a private variable
obj.__displayinfo() # We cannot use this as well (private function)










