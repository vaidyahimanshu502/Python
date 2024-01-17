
"""
This file only contains basics of python like
VAriable Declaration
Data Types in Python
Castings
Checking Types 
"""
if 7 > 8:
 print("7 is greater.")
else:
 print("8 is greater.");
 
A = 5;
B = 5;
print(A+B);

x = 10;
x = 20;
print(x);

x = int(10);
y = str("Name");
z = float(9);
print(x, y, z);
print(type(x), type(y), type(z));

"""
Variables names in python can only contains Alpha-Numeric with underscore.
"""
myName = "Himanshu Vaidya";
num1   = 20;
data_type = "Integer";

""" Assigning multiple values to the variables """
name1, name2, name3 = "Himanshu", "Vivek", "Raj";
print(name1, name2, name3);

""" Unpacking """
fruits = ["Apple", "BAnana", "Girl"];
a, b, boy = fruits;
print(a, b, boy);

""" Global variable with keywords """
x = 2000 # global
def myName():
    name = "Himanshu" # local 
    print(name)
  
myName()
