# String indexing and slicing
# String - sequence of characters
# can be created by enclosing characters inside a single quote or double quotes
# triple quotes can be used represent multiline strings

# string indexing
#    -5 -4 -3 -2 -1    String indexing from right to left
#     H  E  L  L  O    String
#     0  1  2  3  4    String indexing from left to right

a = "Subham Kumar"
print(a[0])          # String indexing
print(a[-5])         # String indexing

print(a[0:8])        # String slicing from 0 to 8
print(a[0::2])       # String slicing from 0 to last element with step value of 2

print(a[-1::-4])     # negative string slicing


