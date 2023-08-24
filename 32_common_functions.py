from functools import reduce

numbers = [4, 2, 7, 1, 9, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Salida: [1, 2, 3, 4, 7, 9]


numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # Salida: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Salida: 15 (1 + 2 + 3 + 4 + 5)
