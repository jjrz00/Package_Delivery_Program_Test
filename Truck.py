#create Truck class
class Truck:

    #create Truck constructor
    def __init__(self, truck_num, truck_packages, departure_time):

        self.truck_num = truck_num
        self.truck_packages = truck_packages
        self.departure_time = departure_time
        self.current_location = "HUB"
        self.truck_mileage = 0

    #create string representation method for Truck instances
    def __str__(self):
        return f"{self.truck_num}, {self.truck_mileage}"


