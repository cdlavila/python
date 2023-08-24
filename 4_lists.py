print('List')
example_list = [1, 2, 3.6, 'tres', ['uno', 'dos', 'tres']]
print(example_list)
# Accessing elements of a list
print(example_list[3])
# Add a new element to the end of the list
example_list.append(4)
print(example_list)
# Remove the last element of the list
example_list.pop()
print(example_list)
# Sum or concatenate lists
print([1, 2, 3] + [4, 5, 6])  # Concatenation

list_to_reverse = [1, 2, 3, 4]
print('List to reverse:', list_to_reverse)
list_to_reverse.reverse() # Or list_to_reverse[::-1]
print('Reversed list:', list_to_reverse)

# List methods
# Create an empty list
my_list = []

# Add elements using append()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print("After append:", my_list)

# Insert an element at a specific position using insert()
my_list.insert(1, 15)
print("After insert:", my_list)

# Remove elements using remove() and pop()
my_list.remove(20)
removed_value = my_list.pop(0)
print("After remove and pop:", my_list, "Removed value:", removed_value)

# Find the index of a value using index()
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# Count occurrences using count()
count_of_10 = my_list.count(10)
print("Count of 10:", count_of_10)

# Sort and reverse the list
my_list.sort()
print("After sort:", my_list)

my_list.reverse()
print("After reverse:", my_list)

# Extend the list using extend()
another_list = [40, 50]
my_list.extend(another_list)
print("After extend:", my_list)

# Clear the list using clear()
my_list.clear()
print("After clear:", my_list)