from abc import ABC, abstractmethod

class Shape(ABC):  # Clase abstracta (ABC): Abstract Base Class
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):  # Clase derivada
    def __init__(self, radius):
        self.radius = radius

    # If you don't implement this method, you will get an error
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):  # Clase derivada
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# No se puede instanciar directamente una clase abstracta
# shape = Shape()  # Esto generaría un error

circle = Circle(5)
print("Circle area:", circle.area())  # Output: Circle area: 78.5

rectangle = Rectangle(4, 6)
print("Rectangle area:", rectangle.area())  # Output: Rectangle area: 24
