# assignment2

class Vehicle:
    def move(self):
        print("Vehicle is moving...")


class Car(Vehicle):
    def move(self):
        print("Car is driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Plane is flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Boat is sailing 🚤")


# Example usage (Polymorphism in action)
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
