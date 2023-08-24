# Arrays in Python
# Arrays are used to store multiple values in one single variable
# The syntax of array is: arrayName = array(typecode, [Initializers])
# All the elements in an array must be of the same type

from array import *

int_array = array('i', [1, 2, 3, 4, 5])
print(int_array)
print(int_array[1])
int_array.append(6) # you can use the same methods as lists
print(int_array)

"""
int_array = array('i', [1, 2, 3, 4, '5'])
print(int_array)

ERROR
Traceback (most recent call last):
  File "/Users/Carlos/Documents/Projects/python/5_arrays.py", line 15, in <module>
    int_array = array('i', [1, 2, 3, 4, '5'])
TypeError: 'str' object cannot be interpreted as an integer
"""


