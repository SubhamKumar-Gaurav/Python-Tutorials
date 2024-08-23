# Conditional statements in PYTHON
# if statement , if else statement , if elif else statement
# proper spacing needs to be take care


# if statement syntax
#     if (condition) :
#         (statement to be executed)

a = int(input("Enter a : "))
if a%2==0 :
    print(a , "is even number")


# if else statement syntax
#     if (condition) :
#        (statement to be executed)
#     else:
#        (alternate statement to be executed)

b = int(input("Enter b : "))
if b%2==0 :
    print(b , "is even number")
else:
    print(b , " is odd number")


#  if elif else statement syntax
#      if (condition 1) :
#                [statement 1]
#      elif (condition 2) :
#                [statement 2]
#      elif (condition 3)  :
#                [statement 3]
#      else:
#         [statement when if and elif(s) are false]

c = int(input("Enter your percentage : "))
if c>=80 :
    print("First division ")
elif c>=60 :
    print("Second division ")
elif c>=40 :
    print("Third division ")
else :
    print("You are fail")