# tuples.py

# Tuples are like lists, but immutable (can't be changed later)
# Because they can't be mutated, they are slightly more space/time efficient

import sys, platform, time

mytuple = (5,) * 10
print(mytuple)
print(f"Address:{hex(id(mytuple))}")
mytuple = mytuple + (1, 2, 3)
print(mytuple)
print(f"Address:{hex(id(mytuple))}")
