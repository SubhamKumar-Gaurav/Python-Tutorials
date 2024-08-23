# Functions in Python :
# (i)   simple function
# (ii)  function with argument
# (iii) return type

# Syntax of a function :
#   def function_name()
         # code to be executed
         # code to be executed
# function_calling()


# Defining a function :
def simplefn() :
    print("Hi Hello GoodBye! ")
# Calling a function :
simplefn()


# Function with argument :
def sumdata(a,b) :
    print(a+b)

a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
# Calling function
sumdata(a,b)


# Function with default argument :
def subham(a,b=5) :
    print(a+b)
subham(int(input("Enter a : ")),10)



# Function with return type :
def skg(a,b) :
    c=a+b
    return c
h=skg(20,20)
print(h)





