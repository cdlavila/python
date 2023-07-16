# Loops
print('\nNormal for loop')
for i in range(5):
    print(i)

print('\nWhile loop')
j = 5
while j > 0:
    print(j)
    j -= 1

# Loops in lists
print('\nFor in lists')
roles = ['admin', 'user', 'guest']
for role in roles:
    print(role)

# Loops in dictionaries
print('\nFor in dictionaries')
professor = {
    'name': 'Cesar Jaramillo',
    'age': 40,
    'degree': 'PhD'
}
for key, value in professor.items():
    print(f'{key}: {value}')