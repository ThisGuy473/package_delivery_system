##### WGUPS #######################
##### Jeffrey Day #################
##### C950 Data Strucs & Algos II #
##### 1/21/2022 ###################
import csv_reader
import distance
from hash_table import HashMap
import package
import itertools
from operator import itemgetter

def main():
    
    h = HashMap()
    csv_reader.get_hash_map()

    #truck start times
    truck1_start_time = '8:00'
    truck2_start_time = '9:05'
    truck3_start_time = '10:30'
    route_start = 0

    #Read data from csv and sort into truck load lists
    truck1_list = csv_reader.first_truck_packages()
    truck2_list = csv_reader.second_truck_packages() 
    truck3_list = csv_reader.third_truck_packages()
    distance_adj_list = distance.create_distance_data_adj_list()

    #Greedy algorithm used on trucklists to determine shortest route
    truck1_route = distance.shortest_route_recursion(truck1_list, distance_adj_list, route_start, truck_number=1)
    truck2_route = distance.shortest_route_recursion(truck2_list, distance_adj_list, route_start, truck_number=2)
    truck3_route = distance.shortest_route_recursion(truck3_list, distance_adj_list, route_start, truck_number=3)

    #Truck Distances are added up 
    truck1_distance = distance.get_truck_distance(truck1_route)
    truck2_distance = distance.get_truck_distance(truck2_route)
    truck3_distance = distance.get_truck_distance(truck3_route)
    total_distance = distance.get_total_distance(truck1_route, truck2_route, truck3_route)

    #Time for trucks is calculated
    distance.get_time(truck1_route, truck1_start_time)
    distance.get_time(truck2_route, truck2_start_time)
    distance.get_time(truck3_route, truck3_start_time)
    del truck1_route[-1]
    del truck2_route[-1]
    del truck3_route[-1]

    #User interface
    def ui_menu():
        userresponse = input("Please select and option below or type 'exit' at any time to exit.\n 1. Get package status for all packages at specific time.\n 2. Get package status on a specific package.\n 3. Get all route distance info.\n-->")
        #Get info for all packages->O(n)
        if userresponse == '1':
            userinput = input("Please enter a time between 08:00 to 13:30 to view status of all packages 'HH:MM': ")
            combined_truck_list = list(itertools.chain(truck1_route,truck2_route, truck3_route))
            for item in combined_truck_list:
                item[0] = int(item[0])
            combined_truck_list = sorted(combined_truck_list, key=itemgetter(0))
            package.snapshot(userinput, combined_truck_list)
            exit_options()
        
        #Get info for a specific package->O(n)
        elif userresponse == '2':
            package_input = input("Please enter a package id: ")
            time_input = input("Please input time to get package status: ")
            combined_truck_list = list(itertools.chain(truck1_route,truck2_route, truck3_route))
            for item in combined_truck_list:
                item[0] = int(item[0])
            combined_truck_list = sorted(combined_truck_list, key=itemgetter(0))
            package.get_package(package_input, time_input, combined_truck_list)
            exit_options()
                
        #Get total distances for truck routes->O(1)
        elif userresponse == '3':
            
            print("truck1 total distance:", truck1_distance+ truck3_distance, "miles")
            print("truck2 total distance:", truck2_distance, "miles")
            print("Route completed in ", total_distance, "miles\n")
            exit_options()
        
        #Complexity->O(1)
        elif userresponse == 'exit':
            exit()
        
        #Complexity->O(1)
        else:
            print(f"'{userresponse}' is not a valid input")
            ui_menu()
    
    #User exit options->O(1)  
    def exit_options():
        #user input from console
        userinput2 = input("type 'menu' to return to menu or 'exit' to exit: ")
        
        #Returns user to main menu
        if userinput2 == 'menu':
            ui_menu()
        
        #Exits the program
        elif userinput2 == 'exit':
            exit()
        
        #If input is invalid menu starts over again
        else:
            print(f"'{userinput2}' is not a valid input")
            exit_options()
            
    print("-----------------------------------------------------------")
    print("-------------------WGUPS ROUTING PROGRAM-------------------")
    print("----------------------by. Jeffrey Day----------------------\n")
    print("Route completed in ", total_distance, "miles\nAll packages delivered on time.\n")
    ui_menu()
    exit()
