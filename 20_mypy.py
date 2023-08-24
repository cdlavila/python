# Without using mypy, it will not show any error until running it.
def add_numbers(a, b):
    return a + b

# Trying to add a string to an int, it will FAIL when running it.
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
result = add_numbers(5, "10")
print(result)


# NOTE: run mypy file_name.py to check for errors.

# Using mypy, it will show the error before running it if you run: mypy 20_mypy.py
def add_numbers_v2(a: int, b: int) -> int:
    return a + b

# Trying to add a string to an int, it will FAIL when running it.
# If you run: mypy 20_mypy.py, it will show the error before running it.
# 20_mypy.py:19: error: Argument 2 to "add_numbers_v2" has incompatible type "str"; expected "int"  [arg-type]
# Found 1 error in 1 file (checked 1 source file
result = add_numbers_v2(5, 10)
print(result)

# NOTE: mypy only works if you have type annotations in your cod, otherwise it will not work.
# For example, -> int, -> str, etc.