# Module - (i) pre existing module  (ii) user defined
# can be a collection of functions , variables , classes
# we need to import module (means module is an external file)

# Calling a module :
# Method 1 :
# import module_name
# module_name.function_name()

# Method 2 :
# from module_name import  function_name

# We can also make alias of a module
# import module as m
# print(m.sum(arguments))

# from module_name import *   (imports all the functions of


# Method 1 :
import module1
print(module1.sum(10,20))
print(module1.sq(15))


from module1 import sum
print(sum(10,40))
from module1 import sq
print(sq(4))

from module1 import *
print(sum(9,60))
print(sq(23))






