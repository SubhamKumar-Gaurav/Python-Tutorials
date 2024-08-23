# Random module

# 1. Random randint() method - return a number between 5 and 10 (both included)
# [a,b]
import random
print(random.randint(5,10))


# 2. Random.randrange() - returns a no. btw 3 and 9
# [a,b)
import random
print(random.randrange(3,9))


# 3. Random choice method - return a random element from a list
l=["apple" , "kela" , "amrud"]
print(random.choice(l))


# 4. random() - returns a random float number between 0 and 1
import random
print(random.random())


# 5. shuffle() - Takes a sequence and returns the sequence in a random order
import random
print(random.shuffle(l))


# 6. uniform() - returns a random float number between two given parameters
import random
print(random.uniform(3,6))

