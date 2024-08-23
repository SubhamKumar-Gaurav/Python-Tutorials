# Bitwise operators - converts integer into binary , performs operations in binary , gives final output in integer
# & - logical AND
# | - logical OR
# ^ - logical XOR  ( false when all the inputs are same )
# bin() - function to find binary

x = 10
y = 9
print(bin(x))   # 1010
print(bin(y))   # 1001
print(x&y , bin(x&y))  # 1010 & 1001 = 1000
print(x|y , bin(x|y))  # 1010 | 1001 = 1011
print(x^y , bin(x^y))  # 1010 ^ 1001 = 0011

