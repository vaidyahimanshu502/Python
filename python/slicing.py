"""
Slicing Strings
"""
var = "Himanshu Vaidya"
print(var[3 :5])  #an
print(var[ : 7])  #Himansh
print(var[3 : ])  #anshu Vaidya

""" Negative Indexing """
b = "Hello, World!"
print(b[-5:-2])  #orl

""" Method to print Upper Case """
name = "Himanshu Vaidya"
print(name.upper())

""" Method to print in Lower Case """
print(name.lower())

""" Removing White spaces """
name1 = "  Vivek Kumar       Sonam"
print(name1)
print(name1.strip())

""" Replacinfg  Strings"""
print(name.replace('i' ,'e'));