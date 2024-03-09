class Engine:
    def __init__(self, power, type):
        self.power = power
        self.type = type

    def __str__(self):
        return f"Engine: {self.type}, power {self.power} HP."

class Body:
    def __init__(self, type, color):
        self.type = type
        self.color = color

    def __str__(self):
        return f"Body: {self.type}, color {self.color}"

class Wheels:
    def __init__(self, size, type):
        self.size = size
        self.type = type

    def __str__(self):
        return f"Wheels: {self.type}, size {self.size} inches"

class Car:
    def __init__(self, make, model, engine, body, wheels):
        self.make = make
        self.model = model
        self.engine = engine
        self.body = body
        self.wheels = wheels

    def detailed_description(self):
        return f"{self.make} {self.model}\n{self.engine}\n{self.body}\n{self.wheels}"

# Example usage:
engine = Engine(150, "petrol")
body = Body("sedan", "red")
wheels = Wheels(17, "alloy")
car = Car("Toyota", "Camry", engine, body, wheels)

print(car.detailed_description())

