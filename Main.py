#Jojo Rodriguez 011987446

import csv
from HashTable import HashTable
from DistanceList import DistanceList
from datetime import timedelta
from Package import Package
from Truck import Truck

#create empty lists to hold package instances and distance list instances
packages = []
distance_list = []

#open distance table csv and append to distance_list
with open("Distance Table.csv", mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
    distance_list.append(lines)

#open and clean packages csv and append to packages
with open("packages.csv", "r") as file:
    lines = file.readlines()

    #loop through lines in packages csv and clean (remove quotes)
    for line in lines:
        clean_line = line.strip().replace('"', '')

        if not clean_line:
            continue

        #split lines at comma
        values = clean_line.split(",")

        #create Package instance and append to packages list
        pkg = Package(*values)
        packages.append(pkg)

#create HashTable instance with packages
package_hash_table = HashTable()
for pkg in packages:
    package_hash_table.insert(pkg)

#create DistanceList function instance to use in nearest neighbor algorithm
distance_list_functions = DistanceList(distance_list)

#start_address = packages[6].package_address
#end_address = packages[4].package_address

#mile = (distance_list_functions.get_distance(start_address, end_address))
#print(mile)

#create deliver packages function, initialize/print time and location variables
def deliver_packages(truck):
    current_time = truck.departure_time
    current_location = distance_list[0][0]

    #print(current_location)
    #print(current_time)

#begin nearest neighbor algorithm, while there are packages in truck instance
    while truck.truck_packages:
        next_pkg = None
        shortest_address_distance = float("inf")

        #loop through packages, get nearest package address and assign shortest address and next package variables
        for pkg_id in truck.truck_packages:
            pkg_id = int(pkg_id)
            pkg = package_hash_table.lookup(pkg_id)
            distance_between = distance_list_functions.get_distance(current_location, pkg.package_address)
            if distance_between < shortest_address_distance:
                shortest_address_distance = distance_between
                next_pkg = pkg

        #print package delivery
        print(f"package {next_pkg.package_id} delivered to {next_pkg.package_address} ^-^")

        #adjust current time, location and truck + next package attributes and remove package after delivery.
        current_location = next_pkg.package_address
        current_time = current_time + timedelta(hours=shortest_address_distance / 18)
        truck.truck_mileage += shortest_address_distance

        next_pkg.package_delivery_time = current_time
        next_pkg.truck_id = truck.truck_num
        next_pkg.package_loading_time = truck.departure_time
        next_pkg.status = "delivered"

        truck.truck_packages.remove(next_pkg.package_id)

#create package id lists for trucks 1-3
t1 = [1, 4, 10, 11, 12, 13, 14, 15, 16, 20, 24, 29, 30, 34, 37]
t2 = [3, 6, 18, 25, 31, 32, 36, 38, 40]
t3 = [2, 7, 5, 8, 9, 17, 19, 21, 22, 23, 26, 27, 28, 33, 35, 39]

#create Truck instances, and insert package id lists
truck1 = Truck(1, t1, timedelta(hours=8, minutes=0))

truck2 = Truck(2, t2, timedelta(hours=9, minutes=5))

truck3 = Truck(3, t3, timedelta(hours=10, minutes=20))

#execute package delivery for all trucks and update package 9 address
deliver_packages(truck1)
deliver_packages(truck2)
p9 = package_hash_table.lookup(9)
p9.package_address = "410 S State St."
p9.package_zip = "84111"
deliver_packages(truck3)

#create user interface while program runs and await user input
while True:
    print("-" * 60)
    print("total_mileage- ", (truck1.truck_mileage + truck2.truck_mileage + truck3.truck_mileage),
          "truck 1 mileage- ", (truck1.truck_mileage), "truck 2 mileage- ", (truck2.truck_mileage),
          "truck 3 mileage- ", (truck3.truck_mileage))
    print("-" * 60)
    print("1.  List status of all packages")
    print("2. List status of all packages at specified time")
    print("3. List single package at specified time")
    print("4,  exit")
    choice = int(input("Enter choice: "))

    #print status of all packages in hashtable if user enters 1
    if choice == 1:
        for i in range (1, 41):
            print (package_hash_table.lookup(i))

    #prompt user, convert resulting string to timedelta. Print time status routine for each package if user enters 2
    elif choice == 2:
        time_entered = input("Enter time  (hh:mm): ")
        input_hours, input_minutes = map(int, time_entered.split(':'))
        time_entered = timedelta(hours=input_hours, minutes=input_minutes)
        for pkg_id in range(1, 41):
            pkg = package_hash_table.lookup(pkg_id)
            print(pkg.time_status(time_entered))

    #prompt user, convert resulting string to timedelta and print time status routine if user enters 3
    elif choice == 3:
        time_entered = input("Enter time  (hh:mm): ")
        input_hours, input_minutes = map(int, time_entered.split(':'))
        time_entered = timedelta(hours=input_hours, minutes=input_minutes)
        package_id = int(input("Enter package id: "))
        pkg = package_hash_table.lookup(package_id)
        print(pkg.time_status(time_entered))
    #end program if choice = 4
    elif choice == 4:
        break


#test for 10am, 9am, and 11pm

print(truck1)
print(truck2)
print(truck3)