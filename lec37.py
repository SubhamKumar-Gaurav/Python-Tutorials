# Tuple :
# ordered datatype
# always contain more than one element
# defined in () separated by comma
# immutable
# iterating through tuple is faster than with list

# tuple functions : min() , max() , count() , index() , sum()

t=(10,20,30,40,50,60,70,80,90,10)
print(t[1])
l=len(t)

# for a in range(l) :
#      print(t[a])

print(min(t))
print(max(t))
print(t.count(10))
print(t.index(50))
print(sum(t))
print(sum(t,100))

