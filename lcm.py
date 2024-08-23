# To find LCM
import math
print(2*5 // math.gcd(2,5))


def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        print("False")
    elif year % 4 == 0 and year % 100 == 0:
        print("True")


year = int(input())
print(is_leap(year))