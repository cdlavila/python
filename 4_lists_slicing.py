"""
In Python, the concept of "slicing" lists and sequences is well-known and follows a consistent syntax.
The syntax for slicing is as follows:

list[start:stop:step]

Where:

start: The index to start the slice (inclusive).
stop: The index to end the slice (exclusive).
step: The step size between elements in the slice (optional, defaults to 1).
"""

# Define a list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original list:", my_list) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using List[:n]
first_three = my_list[:2]
print("First three elements:", first_three)  # Output: [0, 1]

# Using List[n:]
from_four_onwards = my_list[5:]
print("Elements from index 5 onwards:", from_four_onwards)  # Output: [5, 6, 7, 8, 9]

# Using List[n:m]
between_three_and_six = my_list[2:5]
print("Elements between index 2 and 5:", between_three_and_six)  # Output: [2, 3, 4]

# Using List[start:stop:step]
sliced_list = my_list[1:8:2]
print("Sliced list with step 2:", sliced_list)  # Output: [1, 3, 5, 7]

# Using List[::step]
stepped_list = my_list[::2]
print("List with step 2:", stepped_list)  # Output: [0, 2, 4, 6, 8]