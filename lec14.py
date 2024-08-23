# Data types in python
# 1) Numeric - integers , float , complex numbers
# 2) Sequence types - string , list , tuple
# 3) Dictionaries
# 4) List

# Datatypes - mutable ( changes can be made ) and immutable (no changes can be made)
# Mutable - list , dictionary , byte array
# Immutable - int , float , complex , string , tuple , set


# NUMBERS :
a = 5
print(a,type(a))
a = 5.5
print(a,type(a))
a = 5+7j
print(a,type(a))


# STRINGS - written within ' ' or " " or ''' '''
# ''' ''' - print as it is written within the quotation
s = ''' 
Hi 
Hello 
Good bye 
'''
print(s,type(s))

b = 10
print(b,type(b))
c = '10'
print(c,type(c))
print(id(b) , id(c))


# LIST - ordered sequence of items , most used datatype in Python , very flexible , mutable
l = [10 , 'Subham' , 11]
l[2] = 20
print(l, type(l))


# TUPLE - ordered sequence of items same as list , defined within paranthesis() , immutable , faster than list
t = ( 10 , 20 , 30 )
print(t,type(t))
u = (20.0)
print(u,type(u))


# DICTIONARY / DIRECTORY - unordered collection of key-value pairs , defined within curly braces{ } with each item being a pair in the form key:value
d={
    'name' : 'Subham' ,
    'Reg_no' : '2244202'
}
print(d,type(d))


# SET - unordered collection of items
#  Every set element is unique (no duplicates) and must be immutable , declared within { }
my_set= { 10 , 20 , 30 , 20 }
print(my_set, type(my_set))

