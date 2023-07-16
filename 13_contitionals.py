# Conditional
print('\nConditional')
example_number = 2021
if example_number == 2022:  # True sentences
    print('We are in 2022')
else:  # False sentences
    print('We are not in 2022')

# Elif (Python does not have a direct switch statement, so we use if-elif-else)
print('\nElif statement')
if example_number == 2021:
    print('We are in 2021')
elif example_number == 2022:
    print('We are in 2022')
else:
    print('We are not in 2021 or 2022')

# Ternary operator
print('\nTernary operator')
print('We are in 2022' if example_number == 2022 else 'We are not in 2022')