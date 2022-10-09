"""
Write a python script to create a clock where 1st thread will 
print the current time every second and 2nd will print 
“1 Minute Completed” after every 1 minute.
"""

from datetime import datetime
from time import sleep, strftime
from threading import *
from time import time

def first_t():
    while True:
        dt = strftime("%H:%M:%S")
        print(dt)
        sleep(1)

def second_t():
    while True:
        dt = print("1 Minute Completed")
        print(dt)
        sleep(1)

first_t()
second_t()
