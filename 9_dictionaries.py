print('Dictionary')  # Key-value pairs
example_dict = {
  'name': 'Carlos',
  'age': 21,
  'partners': ['Juan Esteban', 'Santiago', 'Juan Camilo']
}
print(example_dict)
# Getting the value of a key in a dictionary
print(example_dict['name'])
# Getting all keys of a dictionary
print(list(example_dict.keys()))
# Getting all values of a dictionary
print(list(example_dict.values()))

# Dictionary methods
# Creating a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Getting keys using keys()
keys = my_dict.keys()
print("Keys:", keys)

# Getting values using values()
values = my_dict.values()
print("Values:", values)

# Getting items using items()
items = my_dict.items()
print("Items:", items)

# Getting values with get()
age = my_dict.get("age")
print("Age:", age)

# Removing a key-value pair using pop()
city = my_dict.pop("city")
print("City:", city)
print("Dictionary after pop:", my_dict)

# Updating the dictionary using update()
new_data = {"age": 31, "gender": "female"}
my_dict.update(new_data) # Updates the dictionary merging the new data
print("Updated dictionary:", my_dict)

# Clearing the dictionary using clear()
my_dict.clear()
print("Dictionary after clear:", my_dict)

# Checking existence using "in"
if "name" in my_dict:
    print("Name exists in the dictionary.")
else:
    print("Name does not exist in the dictionary.")
