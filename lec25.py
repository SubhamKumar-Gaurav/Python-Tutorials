# Python string format() method - we can add anything inbetween the string in runtime

# The format() method formats the specified values and insert them inside the strings placeholder
# The placeholder is defined using curly braces {}

# 1st example :
txt1="Welcome to my  {fname}    {lname}".format(fname="Youtube" , lname="channel")
print(txt1)  # jitna space string me denge wo output me bhi ayega

# 2nd example :
txt2="Welcome to my  {0}  {1}".format("Youtube" , "channel")
print(txt2)

# 3rd example
txt3="Welcome to my {} {}".format("Youtube" , "channel")
print(txt3)

# 4th example
txt4="Welcome to my {a} {b}".format( a="Youtube" , b="channel" )
print(txt4)


# We can even shift the placeholders to right , left or middle
# use the operator : before < , > and ^
# Center align
txt5="Welcome to my {a:^10} {b:^10} ok !".format( a="Youtube" , b="channel" )
print(txt5)

# Left align
txt6="Welcome to my {a:<10} {b:<10} ok !".format( a="Youtube" , b="channel" )
print(txt6)

# Right align
txt7="Welcome to my {a:>10} {b:>10} ok !".format( a="Youtube" , b="channel" )
print(txt7)








