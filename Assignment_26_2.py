"""
Write a python script to create a user account class 
with 2 instance variables (userid and balance). 
Create 3 user objects and add all the users using operator
overloading.
"""

class User:

    def __init__(self, user_id, balance):
        self.user_id = user_id
        self.balance = balance

    def __add__(self, other):
        total_u = self.user_id + other.user_id
        total_b = self.balance + other.balance
        s3 = User(total_u, total_b)
        return s3


u1 = User(10, 100)
u2 = User(20, 200)
u3 = User(30, 300)
u4 = User(40, 400)

s3 = u1 + u2 + u3 + u4
print(s3.user_id)
print(s3.balance)
