#  List - Functions

# Function for deleting element from list - del() , pop() , remove() , clear()
#  1. del l[i] - enter the index number and it will remove that element
#  2. l.pop(i) - same as del() , difference is it can also print the deleted element
#  3. l.remove(value) - enter the value from the list and it will remove it
#  4. l.clear() - clears the entire list
print("To delete the elements from the list ")
l=[10,20,30,40,50,60]
del l[3]
print(l)

l.pop(0)
print(l)
print(l.pop(0))  # 20

l.remove(50)
print(l)

l.clear()
print(l)



# Function for updating element in the list - insert() , append() , extends()
# 1. l.insert(index_number , value) - replaces the i'th element in the list
# 2. l.append() - adds element to the end of the list
# 3. l.extend() - same as append() , diff. - adds the data instead of datatype as in append()
print("To update the elements from the list ")
m=[1,2,3,4]
m.insert(0,10)
print(m)

a=[69,96]
m.append("Hello")   # [10, 1, 2, 3, 4, 'Hello']
print(m)
m.append(a)         # [10, 1, 2, 3, 4, 'Hello', [69, 96]]
print(m)

m.extend(a)  # [10, 1, 2, 3, 4, 'Hello', [69, 96], 69, 96]
print(m)



      