"""
Write a python script to multiple 2 or 3 or 4 numbers 
with a single multiply method in a class using method overloading.
"""

class Calculater:

    def multiple(self, a, b = None, c = None, d = None):
        if d != None:
            print(a * b * c * d)
        elif c != None:
            print(a * b * c)
        elif b != None:
            print(a * b)
        else:
            print(a)


c1 = Calculater()
c1.multiple(10, 5, 3, 4)
