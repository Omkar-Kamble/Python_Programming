# there are 3 types of functions in python 
# 1) inbuilt = int, str, bool, etc.
# 2) module = import math, string, random etc.
# 3) user-defined = syntax : def function_name(parameters):
#                            //do something  

# module function
# 1)
import math
print(dir(math)) # you can get all functions from math module
print(math.pi) # you can get value of PI
print()

# 2)
from math import sqrt
print(sqrt(16))
print()

# OR

from math import *
print(sqrt(8))
print()

# user-defined function
# 1)
def greet():
    print("Good Morning, Omkar")
greet()
greet()
greet()
print()

# 2) 
def print_sum(first, second): # here def means definition
    print(first + second)
print_sum(5,8)
print()

# OR

def print_sum(first, second=5):
    print(first + second)
print_sum(5)