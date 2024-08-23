#   Writing and Reading JSON file

import json
file=open("posts.json","r")
x=file.read()
finaldata=json.loads(x)

print(finaldata)

for i in finaldata :
    print(i)







