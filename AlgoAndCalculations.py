
from Packages import *

# Open the Distances file and use a comma as a delimiter to properly cut the data
with open("Distances.csv") as distanceDataFile:
    distance_scanCSV = csv.reader(distanceDataFile, delimiter=",")
    # Create a distance list
    distance_list = list(distance_scanCSV)

# Open the Distances file and use a comma as a delimiter to properly cut the data
with open("Location Names.csv") as locationNameDataFile:
    location_names_scanCSV = csv.reader(locationNameDataFile, delimiter=",")
    # Create a location names list
    location_list = list(location_names_scanCSV)

    # Function that will take two addresses, and then determine the distance from the current one to the next.
    # Big O = O(n)
    def distance_between_two(current_address, next_address):
        # Create indexes to locate the accurate data in the distance_list created earlier
        index_next_address = 0
        index_current_address = 0
        # Run a for loop to iterate through the locations in the location list
        for i in location_list:
            # Use if statements to check if the current address is in the location_list at index i
            if current_address in i:
                # If it is, set the index for the current address as the index of the current_address in the location_list
                index_current_address = location_list.index(i)
            # Otherwise, if next address is in the location_list at index i:
            if next_address in i:
                # Set the index for the next address as the index of the next_address in the location_list
                index_next_address = location_list.index(i)
        # This if statement will make sure that the next_address has a lower index value than the current_address because if not, it would not pull the correct data
        if float(index_next_address) < float(index_current_address):
            # Swap the values of the indexes if the if statement passes
            index_next_address, index_current_address = index_current_address, index_next_address
        # Plug in the indexes into the distance list to determine the distance
        distance = distance_list[index_next_address][index_current_address]
        # Return the distance as a float
        return float(distance)

    # Determines the next closest address on the truck provided based on the last location visited
    # Big O = O(n^2)
    def shortest_distance(last_location, truck):
        # Initialize the variables, returned_package and shortest_distance
        returned_package = ""
        shortest_distance = ""
        # For each package in the truck run the distance_between_two function
        for package in truck:
            # First time through the for loop
            if shortest_distance == "":
                shortest_distance = distance_between_two(package[1] + " (" + package[4] + ")", last_location)
                returned_package = package
            # Every time after the first time through the for loop, check to see if the previous distance is shorter than the shortest distance.
            elif distance_between_two(package[1] + " (" + package[4] + ")", last_location) < shortest_distance:
                # If it is, the new shortest distance becomes the distance between the current package in the loop and the last_location
                shortest_distance = distance_between_two(package[1] + " (" + package[4] + ")", last_location)
                # Set the package to be returned to the current package in the loop
                returned_package = package
        return returned_package

    # Algorithm I will be using is the NEAREST NEIGHBOR ALGORITHM. This algorithm looks for the closest location to the current location and takes that route.
    # Big O = O(n^3)
    def nearest_neighbor():
        # Create copys of the trucks to work with the data without altering the original
        first_truck_copy = first_truck.copy()
        second_truck_copy = second_truck.copy()
        third_truck_copy = third_truck.copy()
        # Create new "Optimized" truck lists to store the route created by the algorithm for each truck
        optimized_first_truck = []
        optimized_second_truck = []
        optimized_third_truck = []
        # Initialize the last locations for each truck
        last_first_truck_location = ""
        last_second_truck_location = ""
        last_third_truck_location = ""
        # Iterate through first truck
        for package in first_truck:
            # Check if its the first iteration
            if last_first_truck_location == "":
                # If first iteration, then the initial location is WGUPS, so we will set it to that
                last_first_truck_location = location_list[0][2]
            # Run the shortest_distance method, and pass in the last_first_truck_location and the copy of the first_truck list
            returned_package = shortest_distance(last_first_truck_location, first_truck_copy)
            # Now that we have the next closest distance, we will add the package returned to the optimized first truck
            optimized_first_truck.append(returned_package)
            # Now the last location for the first truck will be set to the location of the package returned in the shortest distance method
            last_first_truck_location = returned_package[1] + " (" + returned_package[4] + ")"
            # Remove the returned package from the copy of the first truck so it does not continue to go back and forth
            first_truck_copy.pop(first_truck_copy.index(returned_package))

        # Repeat process for second truck
        for package in second_truck:
            if last_second_truck_location == "":
                last_second_truck_location = location_list[0][2]
            returned_package = shortest_distance(last_second_truck_location, second_truck_copy)
            optimized_second_truck.append(returned_package)
            last_second_truck_location = returned_package[1] + " (" + returned_package[4] + ")"
            second_truck_copy.pop(second_truck_copy.index(returned_package))

        # Repeat process for third truck
        for package in third_truck:
            if last_third_truck_location == "":
                last_third_truck_location = location_list[0][2]
            returned_package = shortest_distance(last_third_truck_location, third_truck_copy)
            optimized_third_truck.append(returned_package)
            last_third_truck_location = returned_package[1] + " (" + returned_package[4] + ")"
            third_truck_copy.pop(third_truck_copy.index(returned_package))

        # Return all three optimized trucks with packages stored in the order they will be delivered.
        return optimized_first_truck, optimized_second_truck, optimized_third_truck


    # Calculate the total distance traveled by a truck
    # Big O = O(n^2)
    def total_distance(truck):
        # Initialize the index of the current and next address to determine distance from distance_list later on
        index_current_address = 0
        index_next_address = 0
        # Set the starting address at WGUPS
        starting_address = location_list[0][2]
        # Initialize the total_distance and previous package variables
        total_distance = 0
        prev_package = ""
        # Iterate through each package in truck given
        for package in truck:
            # Check if first iteration
            if prev_package == "":
                # If first iteration, set the previous time to the departure time of package
                old_time = package[9]
                # Run nested for loop to iterate through location list
                for i in location_list:
                    # Check if WGUPS is in location list
                    if starting_address in i:
                        # Set the index of the current address as the index of WGUPS in location_list
                        index_current_address = location_list.index(i)
                    # Check if package currently on is in item of location list
                    if package[1] + " (" + package[4] + ")" in i:
                        # Set the index of the next address as the index of the location in location_list
                        index_next_address = location_list.index(i)
                # Check to see if indexes need to be swapped to yield correct data
                if float(index_next_address) < float(index_current_address):
                    index_next_address, index_current_address = index_current_address, index_next_address
                # Determine current distance by using the indexes and checking csv_file list
                current_distance = distance_list[index_next_address][index_current_address]
                # Now add the float of the current distance to the total_distance variable created earlier
                total_distance += float(current_distance)
                # Calculate the amount of time it took for the current package by multiplying current distance by 60 and dividing by drivers mph (18)
                time_change = timedelta(minutes=(float(current_distance) * 60 / 18))
                # Update the time of when the package was delivered
                new_time = datetime.combine(date.today(), old_time) + time_change
                # Set delivery time of package to the time calculated
                package[10] = new_time.time()
                # Now the new time becomes the old time for the next package
                old_time = new_time.time()
                prev_package = package
            else:
                # Same as first iteration, with the exception that instead of starting address, we will use the previous package
                for l in location_list:
                    if prev_package[1] + " (" + prev_package[4] + ")" in l:
                        index_current_address = location_list.index(l)
                    if package[1] + " (" + package[4] + ")" in l:
                        index_next_address = location_list.index(l)
                if float(index_next_address) < float(index_current_address):
                    index_next_address, index_current_address = index_current_address, index_next_address
                prev_package = package
                current_distance = distance_list[index_next_address][index_current_address]
                total_distance += float(current_distance)
                time_change = timedelta(minutes=(float(current_distance) * 60 / 18))
                new_time = datetime.combine(date.today(), old_time) + time_change
                package[10] = new_time.time()
                old_time = new_time.time()
                # We will check to see if the time has passed 10:20, and if it has, we can now update the package with ID: 9 so that it has the proper address
                if new_time.time() > time(10, 20):
                    third_truck[5][1] = "410 S State St"
                    third_truck[5][2] = "Salt Lake City"
                    third_truck[5][3] = "UT"
                    third_truck[5][4] = "84111"

        # Return the total distance
        return total_distance

    # Method to take distance and divide by 18 to determine total hours driven
    # Big O = O(1)
    def time_traveled(distance):
        return distance / 18

    # Set the status of a package based on a given time of day
    # Big O = O(n)
    def set_status(given_time):
        # If time given is past 10:20, then package with ID 9 can be updated to the correct address
        if given_time > time(10, 20):
            third_truck[5][1] = "410 S State St"
            third_truck[5][2] = "Salt Lake City"
            third_truck[5][3] = "UT"
            third_truck[5][4] = "84111"
        # Otherwise, make sure the package with ID 9 has its initial incorrect address
        else:
            third_truck[5][1] = "300 State St"
            third_truck[5][2] = "Salt Lake City"
            third_truck[5][3] = "UT"
            third_truck[5][4] = "84103"
        # Iterate through packages in first truck
        for package in first_truck:
            #Check if delivery time is lower than the given time
            if package[10] < given_time:
                # If it is, the new status will be the string below where we take the delivery time from the package and tell the user that it was delivered at the time stored in delivery time
                package[8] = "Delivered at " + package[10].strftime("%H:%M")
            elif (package[10] > given_time) and (given_time > package[9]):
                # Otherwise, if the delivery time has not passed yet, but the time given is still greater than its depature time, we know that the package is en route
                # So we will set the status as en route and then the given time
                package[8] = "En Route at " + given_time.strftime("%H:%M")
            else:
                # Lastly, if neither of the previous criteria were met, we know that the package is still at the hub at the given time
                package[8] = "At Hub at " + given_time.strftime("%H:%M")
        # Repeat for second truck
        for package in second_truck:
            if package[10] < given_time:
                package[8] = "Delivered at " + package[10].strftime("%H:%M")
            elif (package[10] > given_time) and (given_time > package[9]):
                package[8] = "En Route at " + given_time.strftime("%H:%M")
            else:
                package[8] = "At Hub at " + given_time.strftime("%H:%M")
        # Repeat for third truck
        for package in third_truck:
            if package[10] < given_time:
                package[8] = "Delivered at " + package[10].strftime("%H:%M")
            elif (package[10] > given_time) and (given_time > package[9]):
                package[8] = "En Route at " + given_time.strftime("%H:%M")
            else:
                package[8] = "At Hub at " + given_time.strftime("%H:%M")



