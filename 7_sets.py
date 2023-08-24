# Sets are unordered collections of unique elements
example_set = {1, 2, 3, 3, 3, 3, 3}
print(example_set)

# Example list
my_list = [1, 2, 3, 3, 3, 3, 3]
print("Original list:", my_list)

# Convert list to set and back to list to remove duplicates
unique_list = list(set(my_list))
print("List after removing duplicates:", unique_list)

# Intersection
my_set = {1, 2, 3}
your_set = {2, 3, 4, 5}
intersection_result = my_set.intersection(your_set)
print("Intersection:", intersection_result)

# Difference
my_set = {1, 2, 3}
your_set = {2, 3, 4, 5}
difference_result = my_set.difference(your_set)
print("Difference:", difference_result)

# Union
my_set = {1, 2, 3}
your_set = {2, 3, 4, 5}
union_result = my_set.union(your_set)
print("Union:", union_result)

# Adding elements using add()
my_set.add(6)
print("Set after adding 6:", my_set)

# Removing elements using remove()
my_set.remove(3)
print("Set after removing 3:", my_set)

# Removing elements using discard()
my_set.discard(2)
print("Set after discarding 2:", my_set)

# Removing and returning an element using pop()
popped_element = my_set.pop()
print("Popped element:", popped_element)
print("Set after pop:", my_set)

# Clearing the set using clear()
my_set.clear()
print("Set after clear:", my_set)

# Checking existence using "in"
if 4 in your_set:
    print("4 exists in the set.")
else:
    print("4 does not exist in the set.")

# Getting the length of the set using len()
set_length = len(your_set)
print("Length of your_set:", set_length)
