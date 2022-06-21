# Nicholas Majors

from AlgoAndCalculations import *

# Run Algorithm to optimize each trucks route, and then call the total distance function to determine time delivered for each package in truck one
optimized_first_truck, optimized_second_truck, optimized_third_truck = nearest_neighbor()
total_distance(optimized_first_truck)

# Run Algorithm again to optimize each trucks route, and then call the total distance function to determine time delivered for each package in truck two
optimized_first_truck, optimized_second_truck, optimized_third_truck = nearest_neighbor()
total_distance(optimized_second_truck)

# Run Algorithm one last time to optimize each trucks route (Specifically the third truck which has an updated address), and then call the total distance function to determine time delivered for each package in truck two
optimized_first_truck, optimized_second_truck, optimized_third_truck = nearest_neighbor()
total_distance(optimized_third_truck)

active = True

# Run a while function for interface so it doesn't exit program until user exits voluntarily. Big 0 = O(n)
while active:
    # Receive input from user to determine what the user wants to do in the program.
    print("\nPress 1 to view the status of all packages, Press 2 to view the status of a specific package by ID, Press 3 to view the total distance traveled by all trucks in miles, Press 4 to quit.")
    choice = input()
    if choice == "1":
        keep_going = True
        # Run a nested while loop in the case that the user enters invalid input.
        while keep_going:
            # Use a try/except statement to catch any errors that would occur in input
            try:
                print("Please enter a time to view all package status: ")
                time_choice = input()
                # Gather user input for time, and then turn the string entered into a datetime.time value so it can be passed into the set_status funciton properly
                time_stripped = datetime.strptime(time_choice, "%H:%M")
                set_status(time_stripped.time())
                # Print info for the given time, and set keep_going to false to exit the nested while loop
                print(hashmap.lookup())
                keep_going = False
            except:
                print("Please enter a valid time (HH:MM)")
    elif choice == "2":
        keep_going = True
        # Run a nested while loop in the case that the user enters invalid input.
        while keep_going:
            try:
                # Gather two user inputs. Package ID and a valid time.
                print("Please enter a package ID: ")
                ID_choice = input()
                print("Please enter a valid time: ")
                time_choice = input()
                # Same as previously, translate string into datetime.time item and pass it into set_status function.
                time_stripped = datetime.strptime(time_choice, "%H:%M")
                set_status(time_stripped.time())
                # For a nice look at the specified package's details, this for loop will display all the packages information cleanly.
                # Big O = O(9)
                for i in range(9):
                    if i == 0:
                        print("Package ID: " + hashmap.get(ID_choice)[i])
                    if i == 1:
                        print("Address: " + hashmap.get(ID_choice)[i])
                    if i == 2:
                        print("City: " + hashmap.get(ID_choice)[i])
                    if i == 3:
                        print("State: " + hashmap.get(ID_choice)[i])
                    if i == 4:
                        print("Zip Code: " + hashmap.get(ID_choice)[i])
                    if i == 5:
                        print("Delivery Deadline: " + hashmap.get(ID_choice)[i])
                    if i == 6:
                        print("Weight (Kilo): " + hashmap.get(ID_choice)[i])
                    if i == 7:
                        print("Special Notes: " + hashmap.get(ID_choice)[i])
                    if i == 8:
                        print("Delivery Status: " + hashmap.get(ID_choice)[i])
                # Exit nested while loop by setting keep_going to false
                keep_going = False
            except:
                print("Please enter a valid time (HH:MM) or Package ID")
    elif choice == "3":
        # Return the total distance traveled by all three trucks which is under 140 by a large margin
        print("Total distance traveled by all three trucks: ")
        print(total_distance(optimized_first_truck) + total_distance(optimized_second_truck) + total_distance(optimized_third_truck))
    elif choice == "4":
        # Exit program
        active = False
    else:
        print("Please enter a valid number")




