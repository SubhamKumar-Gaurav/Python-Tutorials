# Nested dictionary - collection of dictionaries  into one single dictionary
# Nesting dictionary means putting a dictionary inside another dictionary

course={
    'php' : {'duration' : '3Months' , 'fees' :100} ,
    'java' : {'duration' : '2Months' , 'fees' :200} ,
    'python' : {'duration' : '1Month' , 'fees' :300}
}

print(course)
print(course['php']['fees'])
print(course['java']['fees'])
print(course['python']['fees'])

print("Using items() fn. and iterating with for loop")
for a,b in course.items() :
    print(a,b['duration'],b['fees'])

# Updating a value :
course['php']['fees'] = 150
print(course['php'])


