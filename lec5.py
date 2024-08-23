# Variables in python
# In other languages variable address is stored , but here the value of variable is stored
# the function id() is used to find the address

a = 10
b = 20
c = 10
print( id(a) )  #address of a and c will be same
print( id(b) )
print( id(c) )  #address of a and c will be same
print( id(10))

s="Hello"

for i in range(len(s)) :
    print(s[i]) 