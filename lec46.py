#  Pickle in Python

#  to serialize(save) and deserialize(load) the data

# The pickle module implements a fundamental , but powerful algorithm
# for serializing and deserializing a Python object structure

# We can pickle objects with the following data types :
# Booleans , Integers , Floats , Complex numbers , (normal and unicode) strings
# Tuples , lists , sets and dictionaries

# To start pickle , start by importing pickle module
# Pickle has two main methods :
# The first one is dump , which dumps an object to a file object
# and the second one is load , which loads an object from a file object

# dump() - to serialize an object hierarchy
# load() - to de-serialize a data stream

# Pickling with dump() - Pickling data is done via the dump() function ,
# The dump() function then serializes the data and writes it to the file
# Syntax : dump(obj,file)
# obj - Object to be pickled
# file - File object where pickled data will be written
# wb - data write karna
# rb - data load karna

import pickle
l=[10,20,30,40]
file=open("data.txt" , "wb")    # wb - write binary
pickle.dump(l,file)
file.close()

import pickle
file=open("data.txt" , "rb")
l=pickle.load(file)
print(l)















