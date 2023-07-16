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

list_to_reverse = [1, 2, 3, 4]
print('List to reverse:', list_to_reverse)
list_to_reverse.reverse() # Or list_to_reverse[::-1]
print('Reversed list:', list_to_reverse)
