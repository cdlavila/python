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
