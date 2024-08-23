# Implement  a stack and queue using a list data type

# Stack - linear data structure , stores items in a LIFO or FILO manner
# LIFO - Last in First out
# FILO - First in Last out

# Stack operations :
#     push - inserting an element
#     pop - deletion of an element (Last element)
#     peek - display the last element
#     display - display list
print("Stack operation")
l=[10,2]
while True :
    c=int(input('''
    1. Push operation
    2. Pop operation 
    3. Peek operation 
    4. Display operation 
    5. Exit 
    '''))
    if c==1 :
        n=int(input("Enter the value : "))
        l.append(n)
        print(l)
    elif c==2 :
        if len(l)==0 :
            print("Empty stack")
        else :
            t=l.pop()
            print(l)
    elif c==3 :
        if len(l)==0 :
            print("Empty stack")
        else :
            print("The last element is " , l[-1])
    elif c==4 :
        print(l)
    elif c==5 :
        break ;
    else :
        print("Invalid operation ")



# Queue - linear data structure , stores items in FIFO manner
# Queue operations :
#     Enqueue - Adds an item to the queue
#     Dequeue - Removes an item from the queue
#     Front - Get the front item from queue
#     Rear - Get the last item from queue
#
print("Queue operation")
m=[]
while True :
    c=int(input('''
    1. Push element
    2. Pop first element
    3. Front element
    4. Last element
    5. Display queue
    6. Exit 
    '''))
    if c==1 :
        a=input("Enter the value : ")
        m.append(a)
        print(m)
    elif c==2 :
        if len(m)==0 :
            print("Empty Queue")
        else :
            m.pop(0)
            print(m)
    elif c==3 :
        if len(m)==0 :
            print("Empty Queue")
        else :
            print(m[0])
    elif c==4 :
        if len(m)==0 :
            print("Empty Queue")
        else :
            print(m[-1])
    elif c==5 :
        print(m)
    elif c==6 :
        break ;
    else :
        print("Invalid operation")
