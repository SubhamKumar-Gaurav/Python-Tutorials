# List comprehension - elegant way to define and create lists based on existing lists
#   - generally more compact and faster than normal functions and loops for creating list
# Syntax for list comprehension : [expression for item in list]


# Using .append() fn.
l=[]
for a in range(1,11) :
    l.append(a)
print(l)


# Using list comprehension
n=[m for m in range(1,11) if m%2==0]
#  m for m - these variables should be same , we can also add some condition in this with which the list filters the element
print(n)


# strings
s="Hello"
d=[a for a in s]
print(d)







