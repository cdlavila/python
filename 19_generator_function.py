def counter(top):
    n = 0
    while n < top:
        yield n
        n += 1

# Using the generator function
counter_gen = counter(5)

print(counter_gen)  # <generator object counter at 0x7f8b1c1b5f20>
print(type(counter_gen))  # <class 'generator'>
print(next(counter_gen))  # 0
print(next(counter_gen))  # 1

for num in counter_gen:
    print(num) # 2, 3, 4
