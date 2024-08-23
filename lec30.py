# List functions - part 2
# 1. count() - counts the no. of times the element has occured in the list
# 2. max() - finds the maximum value (integer) , for alphabets a=1 , b=2 , c=3 ....
# 3. min() - finds the minimum value (integer) , same as max() function
# 4. sort() - arranges the list elements in ascending order
# 5. reverse() - arranges the list elements in descending order
# 6. index() -  finds the index number of the element

l=[10,30,50,10,20,40]
print(l.count(10))      # 2
print(max(l))           # 50
print(min(l))           # 10
l.sort()                # 10 , 10 , 20 , 30 , 40 , 50
print(l)
l.reverse()             # 50 , 40 , 30 , 20 , 10 , 10
print(l)

m=["Hello" , "World"]
print(m.index("Hello"))    # 0
print(m.index("World"))    # 1
print(max(m))              # World
print(min(m))              # Hello
m.sort()                   # Hello World
print(m)
m.reverse()                # World Hello
print(m)




