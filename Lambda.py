# Single arguments
x = lambda a : a + 10
print(x(5))

# Multiple arguments :
x = lambda a,b : a*b + 10
print(x(5,2))

y = lambda a,b,c : a*b*c
print(y(2,3,4))

# Usage of lambda function :
def myfunc(n):
  return lambda a : a * n

a = myfunc(2)
b = myfunc(3)
print(a(11))
print(b(11))


