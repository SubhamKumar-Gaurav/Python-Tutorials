# String iteration - using for loop
# Method 1 : taking length of the string and then iterating the string using for loop
# Method 2 : Directly iterating the string using for loop

w="Hello Subham Kumar"
t=len(w)
print(t)  #18
for a in range(t) :
    print(w[a])


print("")
# reverse iteration
w="Hello Subham Kumar"
t=len(w)
for a in range(t-1,-1,-1) :
    print(w[a])


w="Hello Subham Kumar"
for a in w :
    print(a)






