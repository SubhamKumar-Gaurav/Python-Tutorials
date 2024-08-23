# Checking String
a="hey i am subham"
if "Subham" in a :
    print("True")
else :
    print("False")


# Functions with arguments :
def func(fname) :
    print("Hello " + fname)

func("Subham")


# Arbitrary arguments : (If we dont know how many arguments to be passed)
def myfn(*name) :
    print("Uska naam hai " + name[2] )

myfn( "Subham" , "Harish" , "Binod" )


# Keyword arguments :
def myfunction(child1 , child2 , child3 ) :
    print("The younger one is " + child3)

myfunction("subham" , "Deepak" , "Harish")


# Arbitrary Keyword Arguments
def fnc(**kids) :
    print("His name is " + kids["f"])

fnc(a="Subham" , b="Harish" , f="Roshan")


# Default parameter value :
def mf(country = "Norway") :
    print("My country is " + country )
mf()
mf("India")

def MYFUNCTION(a) :
    for i in a :
        print(i)
b=["baigan" , "aalu" , "bhindi"]
MYFUNCTION(b)

# Return type
def ret(x) :
    return 5*x
print(ret(5))



