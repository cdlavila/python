class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"


person = Person("Alice", 30)

print(str(person))  # Salida: Person(name='Alice', age=30)
print(repr(person))  # Salida: Person('Alice', 30)
print(person)  # Salida: Person(name='Alice', age=30)

# En la consola
# person  # Salida: Person('Alice', 30)
