"""
Author:         Samuel Diaz #001361588

Title:          WGUPS Routing Project

Description:    Program determines an efficient route and delivery distribution option for packages distributed by
                WGUPS, a parcel distributor.

Course:         C950 - Data Structures and Algorithms II

Sources:        Zybooks textbook - Data Structures and Algorithms II
"""

import csv
import datetime
from HashMap import HashMap
from Truck import Truck
from Package import Package

global dist_array


########################################################################################################################
#                                                   NN Algorithm                                                       #
########################################################################################################################

# Nested for loops to compare package at current delivery address against future delivery
# Chooses an optimal package to after each run
# runtime - O(N²) Quadratic
def algorithm(truck):
    print("Truck", truck.truck_number, "left the hub at", truck.time)

    # go through every single package within the truck
    for p in truck.packages:
        optimal_distance = float('inf')
        optimal_package = None

        # go through every single package ID within the truck
        for p_id in truck.packages:
            # if the time is over 10:20... update package 9 address information
            if truck.time > datetime.timedelta(hours=10, minutes=20):
                package9.street = "410 S State St"

            # get package contents
            curr_package = hashMap.lookup(p_id)

            # 2D array displaying truck's current address and distance to next potential address
            dist_to_next_package = dist_array[address_dict[truck.street]][address_dict[curr_package.street]]

            # Algorithm - NN (Nearest Neighbor)
            # if distance to next package is shorter than optimal distance and package is undelivered...
            # next package distance becomes optimal distance
            if curr_package.time_delivered is None and dist_to_next_package < optimal_distance:
                optimal_package = curr_package
                optimal_distance = dist_to_next_package

        # next package to deliver is an optimal package with the shortest miles to travel to
        if optimal_package is not None:
            # 2D array displaying truck's current address and distance to optimal potential
            dist_to_next_package = dist_array[address_dict[truck.street]][address_dict[optimal_package.street]]
            # record miles driven to travel to the next pacakge
            truck.mileage += dist_to_next_package
            # record time taken to travel to the next pacakge
            truck.time += datetime.timedelta(minutes=(dist_to_next_package / (18 * (1 / 60))))  # trucks travel at 18mph

            truck.street = optimal_package.street
            optimal_package.time_delivered = truck.time
            optimal_package.delivery_status = True
            optimal_package.truck_number = truck.truck_number

    # record miles driven from last package delivered back to the HUB
    dist_to_next_package = dist_array[address_dict[truck.street]][address_dict["4001 South 700 East"]]
    truck.mileage += dist_to_next_package
    # record time taken from last package delivered back to the HUB
    truck.time += datetime.timedelta(minutes=(dist_to_next_package / (18 * (1/60))))  # trucks travel at 18mph
    print("Truck", truck.truck_number, "returned to the hub at", truck.time)
    print()


########################################################################################################################
#                                                     Main                                                             #
########################################################################################################################


# create package objects
# runtime - O(N²)
# def load_package_data(csv_file):
#     my_list = []
#     row_list = []
#     with open(csv_file, 'r', encoding='utf-8-sig') as data:
#         csv_reader = csv.reader(data, delimiter=',')
#         for row in csv_reader:
#             row_list = []
#             for cell in row:
#                 try:
#                     cell = int(cell)
#                 except:
#                     pass
#                 row_list.append(cell)
#             my_list.append(row_list)
#         return my_list
#
#
# packages_array= load_package_data('CSV/wgups_package_file.csv')
# for row in packages_array:
#     print(row)

# create Package objects obtained from information in the spreadsheet
package1 = Package(1, '195 W Oakland Ave', 'Salt Lake City', 'UT', 84115, '10:30 AM', 21, '')
package2 = Package(2, '2530 S 500 E', 'Salt Lake City', 'UT', 84106, 'EOD', 44, '')
package3 = Package(3, '233 Canyon Rd', 'Salt Lake City', 'UT', 84103, 'EOD', 2, 'Can only be on truck 2')
package4 = Package(4, '380 W 2880 S', 'Salt Lake City', 'UT', 84115, 'EOD', 4, '')
package5 = Package(5, '410 S State St', 'Salt Lake City', 'UT', 84111, 'EOD', 5, '')
package6 = Package(6, '3060 Lester St', 'West Valley City', 'UT', 84119, '10:30 AM', 88,
                   'Delayed on flight---will not arrive to depot until 9:05 am')
package7 = Package(7, '1330 2100 S', 'Salt Lake City', 'UT', 84106, 'EOD', 8, '')
package8 = Package(8, '300 State St', 'Salt Lake City', 'UT', 84103, 'EOD', 9, '')
package9 = Package(9, '300 State St', 'Salt Lake City', 'UT', 84103, 'EOD', 2, 'Wrong address listed')
package10 = Package(10, '600 E 900 South', 'Salt Lake City', 'UT', 84105, 'EOD', 1, '')
package11 = Package(11, '2600 Taylorsville Blvd', 'Salt Lake City', 'UT', 84118, 'EOD', 1, '')
package12 = Package(12, '3575 W Valley Central Station bus Loop', 'West Valley City', 'UT', 84119, 'EOD', 1, '')
package13 = Package(13, '2010 W 500 S', 'Salt Lake City', 'UT', 84104, '10:30 AM', 2, '')
package14 = Package(14, '4300 S 1300 E', 'Millcreek', 'UT', 84117, '10:30 AM', 88, 'Must be delivered with 15, 19')
package15 = Package(15, '4580 S 2300 E', 'Holladay', 'UT', 84117, '9:00 AM', 4, '')
package16 = Package(16, '4580 S 2300 E', 'Holladay', 'UT', 84117, '10:30 AM', 88, 'Must be delivered with 13, 19')
package17 = Package(17, '3148 S 1100 W', 'Salt Lake City', 'UT', 84119, 'EOD', 2, '')
package18 = Package(18, '1488 4800 S', 'Salt Lake City', 'UT', 84123, 'EOD', 6, 'Can only be on truck 2')
package19 = Package(19, '177 W Price Ave', 'Salt Lake City', 'UT', 84115, 'EOD', 37, '')
package20 = Package(20, '3595 Main St', 'Salt Lake City', 'UT', 84115, '10:30 AM', 37, 'Must be delivered with 13, 15')
package21 = Package(21, '3595 Main St', 'Salt Lake City', 'UT', 84115, 'EOD', 3, '')
package22 = Package(22, '6351 South 900 East', 'Murray', 'UT', 84121, 'EOD', 2, '')
package23 = Package(23, '5100 South 2700 West', 'Salt Lake City', 'UT', 84118, 'EOD', 5, '')
package24 = Package(24, '5025 State St', 'Murray', 'UT', 84107, 'EOD', 7, '')
package25 = Package(25, '5383 S 900 East #104', 'Salt Lake City', 'UT', 84117, '10:30 AM', 7,
                    'Delayed on flight---will not arrive to depot until 9:05 am')
package26 = Package(26, '5383 S 900 East #104', 'Salt Lake City', 'UT', 84117, 'EOD', 25, '')
package27 = Package(27, '1060 Dalton Ave S', 'Salt Lake City', 'UT', 84104, 'EOD', 5, '')
package28 = Package(28, '2835 Main St', 'Salt Lake City', 'UT', 84115, 'EOD', 7,
                    'Delayed on flight---will not arrive to depot until 9:05 am')
package29 = Package(29, '1330 2100 S', 'Salt Lake City', 'UT', 84106, '10:30 AM', 2, '')
package30 = Package(30, '300 State St', 'Salt Lake City', 'UT', 84103, '10:30 AM', 1, '')
package31 = Package(31, '3365 S 900 W', 'Salt Lake City', 'UT', 84119, '10:30 AM', 1, '')
package32 = Package(32, '3365 S 900 W', 'Salt Lake City', 'UT', 84119, 'EOD', 1,
                    'Delayed on flight---will not arrive to depot until 9:05 am')
package33 = Package(33, '2530 S 500 E', 'Salt Lake City', 'UT', 84106, 'EOD', 1, '')
package34 = Package(34, '4580 S 2300 E', 'Holladay', 'UT', 84117, '10:30 AM', 2, '')
package35 = Package(35, '1060 Dalton Ave S', 'Salt Lake City', 'UT', 84104, 'EOD', 88, '')
package36 = Package(36, '2300 Parkway Blvd', 'West Valley City', 'UT', 84119, 'EOD', 88, 'Can only be on truck 2')
package37 = Package(37, '410 S State St', 'Salt Lake City', 'UT', 84111, '10:30 AM', 2, '')
package38 = Package(38, '410 S State St', 'Salt Lake City', 'UT', 84111, 'EOD', 9, 'Can only be on truck 2')
package39 = Package(39, '2010 W 500 S', 'Salt Lake City', 'UT', 84104, 'EOD', 9, '')
package40 = Package(40, '380 W 2880 S', 'Salt Lake City', 'UT', 84115, '10:30 AM', 45, '')

# create a list containing all package objects to iterate and insert into the hashMap
all_packages_array = [package1, package2, package3, package4, package5, package6, package7, package8, package9,
                      package10, package11, package12, package13, package14, package15, package16, package17, package18,
                      package19, package20, package21, package22, package23, package24, package25, package26, package27,
                      package28, package29, package30, package31, package32, package33, package34, package35, package36,
                      package37, package38, package39, package40]

# create hash table instance
hashMap = HashMap()

# insert package objects into hash table
# runtime - O(N)
n = 1
for package_object in all_packages_array:
    hashMap.insert(n, package_object)
    n += 1

# Table of the distance between address locations
# runtime - O(N²) Quadratic
with open('CSV/wgups_dist_file.csv', 'r', encoding='utf-8-sig') as data:
    dist_array = []
    csv_reader = csv.reader(data, delimiter=',')
    for row in csv_reader:
        row_list = []
        for cell in row:
            cell = float(cell)
            row_list.append(cell)
        dist_array.append(row_list)

# create dictionary with addresses as indices
# runtime - O(1) Constant
address_dict = {"4001 South 700 East": 0,
                "1060 Dalton Ave S": 1,
                "1330 2100 S": 2,
                "1488 4800 S": 3,
                "177 W Price Ave": 4,
                "195 W Oakland Ave": 5,
                "2010 W 500 S": 6,
                "2300 Parkway Blvd": 7,
                "233 Canyon Rd": 8,
                "2530 S 500 E": 9,
                "2600 Taylorsville Blvd": 10,
                "2835 Main St": 11,
                "300 State St": 12,
                "3060 Lester St": 13,
                "3148 S 1100 W": 14,
                "3365 S 900 W": 15,
                "3575 W Valley Central Station bus Loop": 16,
                "3595 Main St": 17,
                "380 W 2880 S": 18,
                "410 S State St": 19,
                "4300 S 1300 E": 20,
                "4580 S 2300 E": 21,
                "5025 State St": 22,
                "5100 South 2700 West": 23,
                "5383 S 900 East #104": 24,
                "600 E 900 South": 25,
                "6351 South 900 East": 26}


# load all three Truck objects
# general limitations...
# at most 16 packages per truck
# Package limitations...
# Package 3 - can only be in truck 2
# Package 6 - will not arrive at the depot until 9:05 am
# Package 9 - wrong address listed
# Package 14 - must be delivered with 15, 19
# Package 16 - must be delivered with 13, 19
# Package 18 - can only be on truck 2
# Package 20 - must be delivered with 13, 15
# Package 25 - will not arrive to depot until 9:05 am
# Package 28 - will not arrive to depot until 9:05 am
# Package 32 - will not arrive to depot until 9:05 am
# Package 36 - can only be on truck 2
# Package 38 - can only be on truck 2
# Deliver these packages by 10:30 a.m.: 1, 6, 13, 14, 16, 20, 25, 29, 30, 31, 34, 37, 40
# Deliver these packages by 9:00 a.m.: 15

# load the following packages to truck 1 given restrictions: 1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 39, 40
truck1_packages_id = [package1.id, package13.id, package14.id, package15.id, package16.id, package19.id, package20.id,
                      package29.id, package30.id, package31.id, package34.id, package37.id, package39.id, package40.id]
# Depart at 08:00
truck1_time = datetime.timedelta(hours=8, minutes=0)
# function initializes Truck 1 at the hub and 0 mileage incurred
truck_1 = Truck(truck1_packages_id, "4001 South 700 East", 0, truck1_time, 1)

# load the following packages to truck 2 given restrictions: 3, 6, 18, 23, 24, 25, 26, 27, 28, 32, 33, 35, 36, 38
# Packages 6, 25, 28, 32 arrive at the depot at 9:05
truck2_packages_id = [package3.id, package6.id, package18.id, package23.id, package24.id, package25.id, package26.id,
                      package27.id, package28.id, package32.id, package33.id, package35.id, package36.id, package38.id]
# Departs at 9:05
truck2_time = datetime.timedelta(hours=9, minutes=5)
# function initializes Truck 2 at the hub and 0 mileage incurred
truck_2 = Truck(truck2_packages_id, "4001 South 700 East", 0, truck2_time, 2)

# load the following packages to truck 3 given restrictions: 2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 19, 21, 22
truck3_packages_id = [package2.id, package4.id, package5.id, package7.id, package8.id, package9.id, package10.id,
                      package11.id, package12.id, package17.id, package19.id, package21.id, package22.id]
# Depart at 10:00
# Note: 1st driver switches to truck 3 after truck 1 finishes delivering
truck3_time = datetime.timedelta(hours=10, minutes=0)
# function initializes Truck 3 at the hub and 0 mileage incurred
truck_3 = Truck(truck3_packages_id, "4001 South 700 East", 0, truck3_time, 3)

# run NN algorithm on all tracks and their corresponding packages
algorithm(truck_1)
algorithm(truck_2)
algorithm(truck_3)


# array of all packages by their ID
# function loops through all packages to display status at a specified time
# runtime - O(N) linear
def all_packages_at_specified_time(hr, mins):
    specified_time = datetime.timedelta(hours=hr, minutes=mins)
    print("\nDelivery status for all packages at", specified_time)
    for p in all_packages_array:
        # get package ID
        p_id = p.id
        # lookup package on hashmap and obtain information
        package = hashMap.lookup(p_id)
        delivery_stats = ""

        if package.truck_number == 1:
            if specified_time <= truck1_time:
                delivery_stats = "at the hub"
            elif truck1_time < specified_time < package.time_delivered:
                delivery_stats = "en route"
            elif specified_time >= package.time_delivered:
                delivery_stats = "delivered"
        if package.truck_number == 2:
            if specified_time <= truck2_time:
                delivery_stats = "at the hub"
            elif truck2_time < specified_time < package.time_delivered:
                delivery_stats = "en route"
            elif specified_time >= package.time_delivered:
                delivery_stats = "delivered"
        if package.truck_number == 3:
            if specified_time <= truck3_time:
                delivery_stats = "at the hub"
            elif truck3_time < specified_time < package.time_delivered:
                delivery_stats = "en route"
            elif specified_time >= package.time_delivered:
                delivery_stats = "delivered"
        print("Package", package.id, "|", delivery_stats)


# checks status of all packages at 09:00
print("---------------------------------------------------------------------------------------------")
all_packages_at_specified_time(9, 20)
# checks status of all packages at 10:00
print("---------------------------------------------------------------------------------------------")
all_packages_at_specified_time(10, 20)
# checks status of all packages at this 12:30
print("---------------------------------------------------------------------------------------------")
all_packages_at_specified_time(13, 00)

# user input menu
# (1) retrieves the delivery status of a package at a specified time
# (2) Displays miles traveled by all trucks combined
# (3) Quits the program
# runtime - O(1) constant
while True:
    user_choice = int(input('\n-----------------------------------------------------------------------------------'
                            '\nRetrieve Package Status (1) | Display Total Mileage (2) | Quit (3)'
                            '\nMenu choice: '))

    # option 1: check status of an individual package at a given time
    if user_choice == 1:
        # gets the requested input to check for specific package id at a specified time
        input_p_id = int(input('\n\nInput package ID (1-40): '))
        input_hrs = int(input('\nHour(1-24): '))
        input_mins = int(input('\nMinutes(1-60): '))

        # convert user's input to objects
        input_time = datetime.timedelta(hours=input_hrs, minutes=input_mins)
        input_package = hashMap.lookup(input_p_id)
        status_message = ""

        # sets the status message based on the user's input package and time
        if input_package.truck_number == 1:
            if input_time <= truck1_time:
                status_message = "at the hub"
            elif truck1_time < input_time < input_package.time_delivered:
                status_message = "en route"
            elif input_time >= input_package.time_delivered:
                status_message = "delivered"
        elif input_package.truck_number == 2:
            if input_time <= truck2_time:
                status_message = "at the hub"
            elif truck2_time < input_time < input_package.time_delivered:
                status_message = "en route"
            elif input_time >= input_package.time_delivered:
                status_message = "delivered"
        elif input_package.truck_number == 3:
            if input_time <= truck3_time:
                status_message = "at the hub"
            elif truck3_time < input_time < input_package.time_delivered:
                status_message = "en route"
            elif input_time >= input_package.time_delivered:
                status_message = "delivered"

        print(input_package)
        print("\n\nPackage ID:", input_package.id, "| Requested time:", input_time,
              "\n---------------------------------------------------------------"
              "\n  Status:", status_message,
              "\n  Time delivered", input_package.time_delivered,
              "\n  Deadline:", input_package.deadline,
              "\n  Address: ", input_package.street, input_package.city, input_package.state, input_package.zip,
              "\n  Weight:", input_package.weight, "lbs",
              "\n  Special notes:", input_package.special_notes,
              "\n  Truck number:", input_package.truck_number)

    # option 2: displays total mileage traveled by each truck
    if user_choice == 2:
        combined_miles = (truck_1.mileage + truck_2.mileage + truck_3.mileage)
        print("\n\nAll trucks combined drove a total of", round(combined_miles, 2), "miles.")

    # option 3: user exits the program
    if user_choice == 3:
        break
