"""
Write a python script to create a to print the above 
user account object using operator overloading (hint __str__ method).
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

    def __str__(self):
        return str(self.user_id) +  " : " + str(self.balance)

u1 = User(10, 100)
u2 = User(20, 200)
u3 = User(30, 300)
u4 = User(40, 400)

s3 = u1 + u2 + u3 + u4
print()
print(s3)
print()
