from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Accessing enum members
print(Color.RED) # Color.red
print(Color(1)) # Color.red
print(Color['RED']) # Color.red

# Accessing enum values
print('\n')
print(Color.RED.value) # 1
print(Color(1).value) # 1
print(Color['RED'].value) # 1

# Accessing enum names
print('\n')
print(Color.RED.name) # RED
print(Color(1).name) # RED
print(Color['RED'].name) # RED

# Iterating over enum members
print('\n')
for color in Color:
    print(color)
    print(color.name)
    print(color.value)