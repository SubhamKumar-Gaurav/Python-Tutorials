# For loop with Range() function
# hw - print multiplication table
# range( start , stop , step_value )

range(5)
# start  = 0 , condition < 5 , increment 1 (default)
# 0 1 2 3 4

range(1,6)
# start = 1 , condition < 6 , increment 1 (default)
# 1 2 3 4 5

range(1,6,2)
# start = 1 , condition < 6 , increment 2 (default)
# 1 3 5

range(10,0,-1)     # range() function running in reverse
# start = 10 , condition < 0 , decrement -1
# 10 9 8 7 6 5 4 3 2 1

for n in range(1,5,2) :
    print(n)

for n in range(10,0,-1) :
    print(n)







