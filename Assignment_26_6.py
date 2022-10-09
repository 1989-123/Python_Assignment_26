"""
Write a python script to create 5 threads to fill a list 
with random numbers till 100. 
"""

from threading import *
from time import sleep
import random

class first_t(Thread):

    def add(self):
        l1 = []
        l = random.randint(1, 100)
        l1.append(l)
        return l

class second_t(Thread):

    def add(self):
        l1 = []
        l = random.randint(1, 100)
        l1.append(l)
        return l

class third_t(Thread):

    def add(self):
        l1 = []
        l = random.randint(1, 100)
        l1.append(l)
        return l

class fourth_t(Thread):

    def add(self):
        l1 = []
        l = random.randint(1, 100)
        l1.append(l)
        return l

class fifth_t(Thread):

    def add(self):
        l1 = []
        l = random.randint(1, 100)
        l1.append(l)
        return l

f1 = first_t()
f2 = second_t()
f3 = third_t()
f4 = fourth_t()
f5 = fifth_t()
a, b, c, d, e = f1.add(), f2.add(), f3.add(), f4.add(), f5.add()
l2 = [a, b, c, d, e]
print()
print(l2)
print()
