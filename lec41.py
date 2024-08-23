# Math module

# 1. math.ceil() - returns the ceiling of x
#   the smallest integer greater than or equal to x
# if x is not a float , delegates to x.__ceil__() , which should return an integral value

import math
x=10.0
print(math.ceil(x))


# 2. math.fabs() - returns the absolute value of x
x=-19
print(math.fabs(x))


# 3. math.factorial() - returns x factorial as an integer , Raises value error if x is not integral or is negative
print(math.factorial(5))


# 4. math.floor() - returns the floor of x , the largest integer less than or equal to x
#  If x is not a float , delegates to x.__floor__() , which should return an integral value
print(math.floor(10.5))


# 5. math.fsum(iterable) - returns an accurate floating point sum of values in the iterable
l=[10.1 , 18.0 , 40.9]
print(math.fsum(l))

# 6. math.sqrt() - returns the square root of x
print(math.sqrt(16))
print(math.sqrt(11))
# print(math.sqrt(-10)) - throws error

# 7. math.gcd(a,b) -  Return the greatest common divisor of the integers a and b.
# If either a or b is nonzero, then the value of gcd(a, b) is the largest positive integer that divides both a and b.
# gcd(0, 0) returns 0.
print(math.gcd(8,2))







