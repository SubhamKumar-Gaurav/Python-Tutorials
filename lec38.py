# Sets :
#  unordered , unindex , defined within {} or set()
# no duplicate elements , can give random values

# set() functions :
# set() - converts into set
# add() - adds the element at random position
# pop() - removes the random element
# remove() - removes the element that we want to remove
# Note : if the item to be removed does not exist , then remove() will raise an error
# clear() - clears the entire set and gives output as set()
# discard() - same as remove() , but won't raise an error { Refer note of remove() }
# update() - updates the set

l=[10,20,30,10]
print(l)
s=set(l)
print(s)
s.add(50)
print(s)
s.pop()
print(s.pop())
s.clear()
print(s)
s.add(79)
s.add(69)
s.add(99)
print(s)
s.remove(69)
print(s)
s.discard(79)
print(s)
s.clear() 
print(s)


