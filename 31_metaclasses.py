"""
Las metaclases son una característica avanzada de Python que te permite controlar el comportamiento de la creación
y estructura de las clases.
Aquí tienes un ejemplo básico de cómo se podría usar una metaclase para personalizar la creación de clases
"""

# Definición de una metaclase
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        # Modificar los atributos antes de crear la clase
        if 'x' not in attrs:
            attrs['x'] = 10
        return super().__new__(cls, name, bases, attrs)

# Usar la metaclase para definir una clase
class MyClass(metaclass=MyMeta):
    def display(self):
        print(f"x = {self.x}")

# Crear una instancia de la clase personalizada
obj = MyClass()
obj.display()  # Salida: x = 10
