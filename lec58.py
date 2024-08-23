# Python errors and built-in exceptions

# These errors can be broadly classifies into two classes :
# 1) Syntax errors (We cannot handle these types of errors)
# 2)Logical errors (Exceptions) - We can handle this type of error

# Syntax error :
a=10
b=20
if a==b
    print("yes")
else
    print("No")


# Python Logical errors (Exceptions)
print(1/0)  # ZeroDivisionError: division by zero
l=[10,20,30,40,50]
print(l[8])   # IndexError: list index out of range