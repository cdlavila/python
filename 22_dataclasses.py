from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

# Create instances of the Point class
p1 = Point(1, 2)
p2 = Point(3, 4)

# Access attributes
print(f"p1: x={p1.x}, y={p1.y}")
print(f"p2: x={p2.x}, y={p2.y}")

# Compare instances
print("p1 == p2:", p1 == p2)  # False

# Automatically generated __repr__ method
print("p1:", p1)  # Output: Point(x=1, y=2)

# Casting
previous_point = (10, 20)
point_instance = Point(*previous_point)
print("point_instance:", point_instance)  # Output: Point(x=10, y=20)
