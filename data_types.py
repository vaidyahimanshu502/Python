""" Data Types in Python """
import random

# type() - By using this we can know the type of data.
a = 1 + 5j 
print(type(a));
print(a)

a = float(100)
print(type(a));
print(a)

b = complex(3)
print(b);

"""
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
"""
print(random.randrange(1, 100)) # prints random numbers between 1 and 100
# List
x = ["name", "age", "Qualification"] # List
print(x)
print(type(x))

y = ("name", "age", "Qualification") # Tuple
print(y)
print(type(y))

z = {"name" : "Himanshu", "age" : 27, "qualification" : "BCA"} #Dict (Dictionary)
print(z)
print(type(z))

w = {"Apple", "Banana", "Apple"} # Set - Only accept unique elements
print(w)
print(type(w))



