# Truck class used to create truck objects
class Truck:
    def __init__(self, packages, street, mileage, time, truck_number):
        self.packages = packages
        self.street = street
        self.mileage = mileage
        self.time = time
        self.truck_number = truck_number

    # transform Truck objects to string for readability
    def __str__(self):
        return "%s, %s, %s, %s" % (self.packages, self.street, self.mileage, self.time)