#!python3
# Explain what this code does

import random
x = []
for i in range(40):
    if random.randint(0,1):
        x.append(random.randint(1,10))
    else:
        x.append(random.randint(1,10) + random.randint(1,10)/10)

print(x)

"""This code starts by creating a list. It then creates a random integer of either 1 or 0, if it is 1 it will be 
considered true, causing the program to add a random integer between 1 and 10 on to the list. If the integer is 0, it
be considered false and the program will add a random number between 1 and 10 that goes to a single decimal place. 
This program will create a list of random numbers between 1 and 10, around half of which will be integers, while the other
~half are numbers with 1 decimal place.

"""


