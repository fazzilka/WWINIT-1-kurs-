class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

circle = Circle(812)
print("Исходный радиус равен:", circle.get_radius())

circle.set_radius(52)
print("Новый радиус равен:", circle.get_radius())