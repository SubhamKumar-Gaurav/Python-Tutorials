# Creating list in Python
# List - mutable datatype , declared in [ ] separated by commas
# Nested list - list ke andar list , ex :  l=[1,2,3, [34,5,6] ,9,56]
# String slicing -  str[ start : stop : step_value ]


l = [ 0 , 1 , 2 , 3 , [4,5,6] ]
print(type(l))
print( l[0::1] )
print( l[4] )      # prints the entire list
print( l[4][2] )   # to get the third element of list 4

m=[1,2,3,4,5,6,7]
print(m[0::2])    # [1,3,5,7]
print(m[-1::-1])  # [7, 6, 5, 4, 3, 2, 1]

n=[1,2,3,4,5,"Hello"]
print(type(n))
print(n[3:])
print(n[-1::-2])
print(type(n[-1]))


