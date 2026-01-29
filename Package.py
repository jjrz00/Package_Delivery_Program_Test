from datetime import timedelta

#create Package class
class Package:

    #create Package constructor
    def __init__(self, package_id=0, package_address="", package_city="", package_state="", package_zip="", package_deadline="",
                 package_weight=0.0, package_notes="", package_delivery_time="", package_loading_time=""):
        self.package_id = int(package_id)
        self.package_address = package_address
        self.package_city = package_city
        self.package_state = package_state
        self.package_zip = package_zip
        self.package_deadline = package_deadline
        self.package_weight = float(package_weight)
        self.package_notes = package_notes
        self.package_delivery_time = package_delivery_time
        self.package_loading_time = package_loading_time
        self.truck_id = None
        self.status = "At the hub"

    #create method for when object is turned into string
    def __str__(self):
        return (f"{self.package_id}" 
                f",{self.package_address}"
                f",{self.package_city}"
                f",{self.package_state}"
                f",{self.package_zip}"
                f",{self.package_deadline}"
                f",{self.package_weight}"
                f",{self.package_notes}"
                f",{self.package_loading_time}"
                f",{self.package_delivery_time}"
                f",{self.status}"
                f",{self.truck_id}"
                )

    #create method to get the status of a pkg at a specified time.
    def time_status (self, time_entered):
        t_status = "at the hub."
        t_delivery_time = ""
        t_address = self.package_address
        t_zip = self.package_zip

        #ensure delayed packages are accounted for in status if time entered is before package loading time
        if time_entered < self.package_loading_time:
            if self.package_id in [6, 25, 28, 32, ]:
                if time_entered < timedelta(hours=9, minutes=5):
                    t_status = "delayed."
        #if time entered is greater than package delivery time, set status to delivered
        elif time_entered > self.package_delivery_time:
            t_status = "delivered."
            t_delivery_time = self.package_delivery_time
        #default status to enroute
        else:
            t_status = "enroute"

        #account for package 9 address before it's changed
        if self.package_id == 9:
            if time_entered < timedelta(hours=10, minutes=20):
                t_address = "300 State St"
                t_zip = "84103"

        #return string representation for time status method
        return (f"{self.package_id}" 
                f"|{t_address}"
                f"|{self.package_city}"
                f",{self.package_state}"
                f"|{t_zip}"
                f"|deadline-{self.package_deadline}"
                f"|weight-{self.package_weight}"
                f"|{self.package_notes}"
                f"|loadtime-{self.package_loading_time}"
                f"|deliverytime-{t_delivery_time}"
                f"|status-{t_status}"
                f"|truck {self.truck_id}"
                )

    #create string representation for Package instances
    def __repr__(self):
        return (f"Package_ID:{self.package_id}" 
                f"Package_Address:{self.package_address}"
                f"Package_City:{self.package_city}"
                f"Package_State:{self.package_state}"
                f"Package_Zip:{self.package_zip}"
                f"Package_Deadline:{self.package_deadline}"
                f"Package_Weight:{self.package_weight}"
                f"Package_Notes:{self.package_notes}"
                f"Package_Delivery_Time:{self.package_delivery_time}"
                f"Package_Loading_Time:{self.package_loading_time}"
                )

