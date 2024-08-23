# zip function and iterating 2+ lists at same time

l1=[1,2,3,4,5]
l2=[10,20,30,40,50]
l3=[2,4,6,8,10]

# Using zip() function :
print("List iteration using zip() function")
for a,b,c in zip(l1,l2,l3) :
    print(a,b,c)

# Without using zip() function :
print("List iteration without using zip() function")
t=len(l2)
for m in range(t) :
    print(l1[m] , l2[m])


