# Converting JSON to Python objects

# If you have a JSON string , you can parse it by using json.loads() method

import json

d='{"cname":"Python","fees":150,"duration":"2 Months"}'
x=json.loads(d)
print(x , type(x))


for i in x :
    print(i , x[i])
