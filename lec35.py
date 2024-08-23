# Dictionary functions - get() , keys() , values() , items()
#   get() - gives the value of the key entered as argument , case sensitive , returns none for non-existing key
#   keys() - to get the key                [compatible in for loop]
#   values() - to get the value            [compatible in for loop]
#   items() - to get both keys and values  [compatible in for loop]
#
#

d = {
    'name' : 'Python' ,
    'fees' : '150' ,
    'duration' : '2Months'
}

print(d.get('name'))
print(d['fees'])
print(d.get('Duration'))   # Returns None

print("")
print(d.keys())
print(d.values())

print("")
print("Iterating keys() fn. via for loop ")
for a in d.keys() :
    print(a)

print("")
print("Iterating values() fn. via for loop ")
for b in d.values() :
    print(b)

print("")
print(d.items())  # appears as ordered pair like (key,value)

print("")
print("Iterating items() fn. via for loop")
for m,n in d.items() :
    print(m,n)


# Functions to delete - del() , pop()
print("")
print("del() and pop() ")
a=d.pop('name')
print(a)
print(d)


# Some other functions - dict() , update() , clear()
#   dict() - to create a dictionary
#   update() - to update the value of any key
#   clear() - clears the dictionary

s=dict(naam='Subham',Roll_no= 2244202,trade='GIN')
print(s)

s.update({'trade':'GEC'})
print(s)


# To add a new key:value pair in dictionary
s['book']="Subconscious mind"
print(s)

# Another way to update a key in dictionary
s['naam']="Gaurav"
print(s)

# To clear the entire dictionary 
s.clear()
print(s)