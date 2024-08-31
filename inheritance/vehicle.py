class Vehicle:
    # Define father class attributes
    def __init__(self, color, plate, wheel_number):
        self.color = color
        self.plate = plate
        self.wheel_number = wheel_number

    # Method example
    def start_engine(self):
        print("Starting engine")

    # To string method
    def __str__(self):
        # Filter every attribute and print
        return f"{self.__class__.__name__}: {', '.join([f"{key}={value}" for key, value in self.__dict__.items()])}"
    
class Bike(Vehicle):
    pass

class Car(Vehicle):
    pass

class Truck(Vehicle):
    # Define attributes
    def __init__(self, loaded, **kw):
        # Pass father class attributes
        super().__init__(**kw)

        # Pass current class attributes
        self.loaded = loaded


    def is_loaded(self):
        print(f"Loaded? {'True' if self.is_loaded else 'False'}")