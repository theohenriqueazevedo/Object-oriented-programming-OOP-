# polymorphism.py

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the area method.")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

def main():
    shapes = [
        Rectangle(4, 5),
        Circle(3)
    ]
    
    for shape in shapes:
        print(f"Area: {shape.area()}")

if __name__ == "__main__":
    main()
