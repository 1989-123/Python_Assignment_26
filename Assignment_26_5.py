"""
Write a python script to create 2 threads to add 
all the values from 1 to 100. 
"""

from threading import *
from time import sleep

class add(Thread):

    def Sum(self):
        s, i = 0, 1
        while i <= 50:
            s = s + i
            i += 1
        return s

class add_1(Thread):

    def Sum(self):
        s, i = 0, 51
        while i <= 100:
            s = s + i
            i += 1
        return s
        
o1 = add()
o2 = add_1()
x = o1.Sum()
y = o2.Sum()
z = x + y
print()
print(z)
print()
