# INSERT Query

# Syntax :
# create a variable , variable_name=''' insert into table_name (variables) VALUES (table_values)  '''

import sqlite3
conn=sqlite3.connect("sqlite.db")
ins='''
      insert into student (st_name,st_class,st_email) VALUES
         ('Alok','12th' , "bheduchand@gmail.com") 
'''
conn.execute(ins)
conn.commit()
conn.close()

