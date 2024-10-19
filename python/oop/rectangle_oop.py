class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height


# Приклад використання
rectangle = Rectangle(5, 10)
print(f"Периметр: {rectangle.calculate_perimeter()}")  # Периметр: 30
print(f"Площа: {rectangle.calculate_area()}")  # Площа: 50
