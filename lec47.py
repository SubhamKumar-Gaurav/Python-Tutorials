# 47. What is JSON and how to create JSON files in Python :


# JSON - JavaScript Object Notation  (backend)
# It is mainly used for storing and transferring data between the browser and the server
# JSON is text , written with JavaScript Object Notation
# Python too supports JSON with a built-in package called json
## import json

# API me data ka format JSON hota hai
# Earlier xml was used to build API
# JSON works on dictionary model (key-value pair)

# JSON supports mainly 6 data types : 1.string , 2.number , 3.boolean , 4.null , 5.object , 6.array

# In python , JSON exists as a string , for example :


import json
# Example of json
p='{"name":"subham" , "lang" : ["Python" , "Java"]}'

import json
d= {
    'course' : 'Python' ,
    'fees' : 150
}

f=json.dumps(d)
print(f , type(f))






