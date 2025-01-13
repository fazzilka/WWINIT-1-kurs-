class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Vehicle make: {self.make}, Model: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        basic_info = super().get_info()
        return f"{basic_info}, Fuel Type: {self.fuel_type}"

my_car = Car("Corvete", "C5", "Petrol")

print(my_car.get_info())