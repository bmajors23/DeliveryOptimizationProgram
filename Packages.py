import csv

from HashTable import HashMap
from datetime import *

# Open the csv file and use a comma delimiter to properly strip the data
with open("Package File.csv") as packageDataFile:
    scanCSV = csv.reader(packageDataFile, delimiter=",")

    # Create hashmap for storing package data
    hashmap = HashMap()

    # Create instances of the three trucks lists to fill with packages.
    first_truck = []
    second_truck = []
    third_truck = []

    # Run a for loop to scan through the csv file and create package variables
    # Big O = O(n)
    for i in scanCSV:
        dep_time = 0
        status = "at facility"
        del_time = 0
        iD = i[0]
        address = i[1]
        city = i[2]
        state = i[3]
        zipcode = i[4]
        deadline = i[5]
        weight = i[6]
        special_notes = i[7]

        # Create a package
        package = [iD, address, city, state, zipcode, deadline, weight, special_notes, status, dep_time, del_time]

        # Run if statements to filter so that each truck receives the correct packages based on deadline times and special exceptions.
        if len(first_truck) < 16 and package[5] != "EOD" and "Delayed" not in package[7]:
            package[9] = time(8, 0)
            first_truck.append(package)

        if len(second_truck) < 16 and "truck 2" in package[7] or "Delayed" in package[7]:
            package[9] = time(9, 5)
            second_truck.append(package)

        if len(third_truck) < 16 and package[0] == '9':
            package[9] = time(10, 24)
            third_truck.append(package)

        # Run if statements if the package did not fit any of the criteria in the other if statements above to make sure no package goes unassigned.
        if package not in first_truck and package not in second_truck and package not in third_truck:
            if len(third_truck) < 16:
                package[9] = time(10, 24)
                third_truck.append(package)
            elif len(second_truck) < 16:
                package[9] = time(9, 5)
                second_truck.append(package)
            elif len(first_truck) < 16:
                package[9] = time(8, 0)
                first_truck.append(package)

        # Add package to the hashmap
        hashmap.insert(iD, package)







