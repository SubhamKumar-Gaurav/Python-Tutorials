# SELECT Query and limit keyword
# row -->> tuple
# limit x,y  # x- where to start (at what index should start)
#            # y- how many data we need to show (no. of data to be shown)

# syntax
# data=conn.execute("SELECT * FROM table_name")
# for n in data :
#     print(n)


import sqlite3
conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT * FROM student limit 0,8 ")
print("STUDENT ID" , "STUDENT NAME" , "STUDENT CLASS" , "STUDENT EMAIL")
for n in data :
    print(n[0],"          ",n[1],"        ",n[2],"   ",n[3])









