# Program to convert string to a list

# Using split() function :
print("Using split() function ")
n=input("Enter the value : ")
print("l =" , n.split())

# Using logic :
m=[]
for a in range(1,5) :
    n=input("Enter the value " +str(a)+ " : ")
    m.append(n)
print("m = " , m)


