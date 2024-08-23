# Python string functions - find() , index() , isalpha() , isdigit() , isalnum()


# find() function
w="Hello"
print(w.find('e'))       # returns the index number of the character
print(w.find('l' , 3))    # the number 3 indicates that we are starting our search from 3rd index
print(w.find('a'))   # returns -1 for non existing character in the string


# index() fn.  - same as find() , difference - shows error for non existing character
a="Subham"
print(a.index('S'))
# print(a.index('e'))  # shows error as 'e' is not present in the string


# isalpha() - shows true if the strings contain only alphabets
b="Gaurav"
c="2244202"
d="Gaurav11"
print(b.isalpha())     # True
print(c.isalpha())     # false
print(d.isalpha())     # false

# isdigit() - shows true if the strings contain only numbers
print(b.isdigit())     # false
print(c.isdigit())     # true
print(d.isdigit())     # false

# isalnum() - shows true if the strings contain alphabets or numbers and not characters
e="Hello Subham"
f="Hello@Gaurav"
print(b.isalnum())     # true
print(c.isalnum())     # true
print(d.isalnum())     # true
print(e.isalnum())     # false - space is neither an alphabet nor a digit
print(f.isalnum())     # false - special character
