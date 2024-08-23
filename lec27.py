#  List iteration

# Using len() function and for loop
print("Using len() function and for loop")
l=[10,20,30,40,50]
t=len(l)
for n in range(t) :
    print(l[n])


# Using for loop without len() fn.
print("")
print("Using for loop without len() fn.")
for a in l :
    print(a)


# List iteration in reverse order
print("")
print("List iteration in reverse order")
l=[10,20,30,40,50]
t=len(l)     # 5
for n in range(t-1,-1,-1) :
    print(l[n])






