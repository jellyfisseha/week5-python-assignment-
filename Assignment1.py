# assignment1

# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.__battery = battery  # encapsulated (private attribute)

    def call(self, contact):
        print(f"{self.brand} {self.model} is calling {contact}...")

    def charge(self, amount):
        self.__battery += amount
        if self.__battery > 100:
            self.__battery = 100
        print(f"{self.brand} {self.model} charged. Battery: {self.__battery}%")

    def get_battery(self):  # encapsulation (getter method)
        return self.__battery


# Derived class (Inheritance + Polymorphism)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    # Overriding method (Polymorphism)
    def call(self, contact):
        print(f"{self.brand} {self.model} (Gaming Edition) is calling {contact} with HD Voice 🎮")


# Example usage
phone1 = Smartphone("Iphone", "v-14", "256GB", 98)
phone1.call("Fish")
phone1.charge(20)
print("Battery level:", phone1.get_battery())

gaming_phone = GamingSmartphone("Realme", "Smart Phone", "256GB", 50, "Liquid Cooling")
gaming_phone.call("Bob")
