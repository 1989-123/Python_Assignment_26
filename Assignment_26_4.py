"""
Write a python script to create two Threads. First thread will print 
all Even numbers and Second thread will print all 
Odd numbers till 100. 
"""

from threading import *
from time import sleep

class evenNumbers(Thread):

    def printEven(self):
        for i in range(2, 10, 2):
            print(i, end=" ")
            sleep(1)

    
class oddNumbers(Thread):

    def printOdd(self):
        for i in range(1, 100, 2):
            print(i, end=" ")
            sleep(1)

obj1 = evenNumbers()
obj2 = oddNumbers()

obj1.printEven()
obj2.printOdd()
