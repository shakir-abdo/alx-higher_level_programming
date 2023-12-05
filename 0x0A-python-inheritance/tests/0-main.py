#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class FirstClass(object):
    pass

class SecondClass(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(FirstClass))
print(lookup(SecondClass))
print(lookup(int))
