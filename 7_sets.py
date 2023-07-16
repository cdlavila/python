# Sets are unordered collections of unique elements
my_set = {1, 2, 3, 3, 3, 3, 3}
print(my_set)

# Remove duplicates from a list
my_list = [1, 2, 3, 3, 3, 3, 3]
print(list(set(my_list)))

# Intersection
my_set = {1, 2, 3}
your_set = {2, 3, 4, 5}
print(my_set.intersection(your_set))

# Difference
my_set = {1, 2, 3}
your_set = {2, 3, 4, 5}
print(my_set.difference(your_set))

# Union
my_set = {1, 2, 3}
your_set = {2, 3, 4, 5}
print(my_set.union(your_set))
