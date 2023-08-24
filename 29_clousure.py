# 1
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)  # Crear un closure con x = 10

result = closure(5)  # Llamada al closure, x = 10, y = 5
print(result)  # Salida: 15


# 2
def create_adder(x):
    def adder(y):
        return x + y
    return adder

# Creamos un closure para sumar 5 a cualquier número
add5 = create_adder(5)

# Creamos un closure para sumar 10 a cualquier número
add10 = create_adder(10)

# Utilizamos los closures creados
result1 = add5(3)   # 5 + 3
result2 = add10(7)  # 10 + 7

print(result1)  # Salida: 8
print(result2)  # Salida: 17


# 3
def custom_sum(a, b=None):
    if b is None:
        # Caso de suma con closure
        def adder(x):
            return a + x
        return adder
    else:
        # Caso de suma normal
        return a + b

# Suma normal
result1 = custom_sum(5, 3)  # 5 + 3
print(result1)  # Salida: 8

# Suma con closure
add7 = custom_sum(7)
result2 = add7(4)  # 7 + 4
print(result2)  # Salida: 11

