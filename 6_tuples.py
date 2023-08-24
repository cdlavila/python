# Remember that tuples are immutable, so you can't add, modify or remove items from them.

# Tuples
print('\nTuples')
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1:3])
print(my_tuple[2:])

# Tuples are immutable
# my_tuple[0] = 10  # This will throw an error
# print(my_tuple)

# Tuple Methods
# Creating tuples
my_tuple = (10, 20, 30, 20, 40)
another_tuple = (50, 60, 70)

# Count occurrences using count()
count_of_20 = my_tuple.count(20)
print("Count of 20:", count_of_20)

# Find the index of a value using index()
index_of_30 = my_tuple.index(30)
print("Index of 30:", index_of_30)

# Concatenate tuples
concatenated_tuple = my_tuple + another_tuple
print("Concatenated tuple:", concatenated_tuple)

# Repeat tuples
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)
