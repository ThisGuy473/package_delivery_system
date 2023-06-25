import csv
from datetime import datetime, timedelta
from operator import itemgetter

truck1_route = []    
truck2_route = []
truck3_route = []

with open('./data/distance_data.csv') as csv_file:
    csv_reader1 = csv.reader(csv_file, delimiter=',')
    distance_list = list(csv_reader1)

with open('./data/distance_name_data.csv') as csv_file:
    csv_reader2 = csv.reader(csv_file, delimiter=',')
    distance_name_list = list(csv_reader2) 

#Creates an adjacency list                   
distance_data_adj_list = {}
data_node_list = []

#Adds a node to adjacency list -> O(n)
def add_node(node):
  if node not in data_node_list:
    data_node_list.append(node)
  else:
    print("Node ",node," already exists!")

#Adds edge using two nodes and the weight -> O(n)
def add_edge(node1, node2, weight):
  temp = []
  if node1 in data_node_list and node2 in data_node_list:
    if node1 not in distance_data_adj_list:
      temp.append([node2,weight])
      distance_data_adj_list[node1] = temp
   
    elif node1 in distance_data_adj_list:
      temp.extend(distance_data_adj_list[node1])
      temp.append([node2,weight])
      distance_data_adj_list[node1] = temp
       
  else:
    print("node1: ", node1, "node2: ", node2, "weight: ", weight, "Nodes don't exist!")
    
#Creates an adjacency list for the distance data from csv -> O(n^2)
def create_distance_data_adj_list(): 
    #Adding nodes
    for i in range(0, 27):
        add_node(i)
    #Adding edges
    for i in range(len(data_node_list)):
        for j in range(0,27):
            add_edge(i,j,distance_list[i][j])
            
    return distance_data_adj_list

#Calculates the time of the trucks and converts to a datetime timestamp based on the distance -> O(n)
def get_time(routelist, initial_time):
    for item in routelist:
        item[5] = 'en route'
    route_start_time = datetime.strptime(initial_time, "%H:%M")
    current_time = initial_time
    first_time = True
    for item in routelist:
        if first_time:
            date_time = datetime.strptime(initial_time, "%H:%M")
            item[4] = str(route_start_time)
            delivery_time = (item[3] / 18) * 60
            final_time = date_time + timedelta(minutes=delivery_time)
            item[6] = str(final_time)
            first_time = False
            current_time = final_time
            item[5] = 'DELIVERED'
        else:
            item[4] = str(route_start_time)
            delivery_time = (item[3] / 18) * 60
            final_time = current_time + timedelta(minutes=delivery_time)
            current_time = final_time
            item[6] = str(final_time)
            item[5] = 'DELIVERED'
        
#Returns the sum of the trucks distances traveled -> O(n)
def get_total_distance(truck1, truck2, truck3):
    truck1_distance = get_truck_distance(truck1)
    truck2_distance = get_truck_distance(truck2)
    truck3_distance = get_truck_distance(truck3)
    return truck1_distance + truck2_distance + truck3_distance

#Returns the sum of distances traveled for given truck -> O(n)
def get_truck_distance(truck):
    return sum([pair[3] for pair in truck])

#Finds value in list of lists -> O(n)
def find_in_list_of_list(query):

    mylist = distance_name_list
    
    for sub_list in mylist:
        if query in sub_list:
            return (mylist.index(sub_list))
    raise ValueError(query, 'not found in list. Check spelling.')

#Returns a list of packages with necessary info to calculate shortest route -> O(n)
def get_route_info(routelist1, 
                   adj_list, 
                   startlocation):
    routeinfo = []
    for item in routelist1:

        route_index = routelist1.index(item)
        item_index = find_in_list_of_list(item[1])
        packageid = item[0]
        delivery_location_address = item[1]
        dead_line = item[5]
        distance_float = float(adj_list[item_index][startlocation][1])
        start_time = ''
        status = item[9]
        delivered_timestamp = ''
        weight = item[6]
        city = item[2]
        package_zip = item[4]
        
        routeinfo.append([packageid, delivery_location_address, dead_line, distance_float, start_time, status, delivered_timestamp, route_index, item_index, weight, city, package_zip])
        
    return routeinfo

#Gets the min value in a list of lists -> O(1)
def get_min(route_info):
    minvalue = min(route_info,key=itemgetter(3))
    return minvalue

"""
The following is a 'Greedy Algorithm'. It uses a recursive technique to determine 
the best location to visit next.

This algorithm takes 4 parameters.
1. List of packages
2. Adjancency list of distances
3. Start location
4. Truck number

First a list takes all necessary info from the routelist and get rid of any un-needed info. 
Routeinfo also calculates the distances of the startlocation and all packages destinations.
Then an if statement is used to check truck number. based on the truck number the algorithm 
proceeds to that section of the code. Then the length of the routlist is check to create a 
end condition for the recursive algorithm. Then the get min is called on routelist to find 
the min distance between the route and startlocaiton. The package with the smallest distance
to the startlocation is then appended to the truck_route list. Then the package with the 
shortest distance to the startlocation is removed from the original routelist. Then the 
startlocation is updated with the shortest package that was just found. The shortest_route_recurision
is called again on the same list only this time its one shorter because a value was removed. This 
is repeated until the original routelist is at 0. Then one more value is appended to the truck_route
list which is the distance to return back to the HUB. The the truck_route list is then returned.

Space-Time Complexity -> O(n^2)
"""            
def shortest_route_recursion(routelist2, 
                             adjacency_list, 
                             startlocation,
                             truck_number):
    
    routeinfo = get_route_info(routelist2, 
                               adjacency_list, 
                               startlocation)
    if truck_number == 1:
        index = len(routeinfo)
        if index > 0:
            index - 1
            minval = get_min(routeinfo)
            truck1_route.append(minval)
            routelist2.remove(routelist2[minval[7]])
            start_location = minval[8]
            return shortest_route_recursion(routelist2, adjacency_list, start_location, truck_number)
        else:
            end_location = 0
            start_location = truck1_route[-1][8]
            distance_float = float(adjacency_list[end_location][start_location][1])
            delivery_location = distance_name_list[0][2]
            delivered_timestamp = ''
            packageid = 'Returning to hub'
            dead_line = ''
            start_time = ''
            status = ''
            route_index = 0
            item_index = 0
            weight = 0
            city = 0
            package_zip = 0
            
            #Return to HUB
            truck1_route.append([packageid, delivery_location, dead_line, distance_float, start_time, status, delivered_timestamp, route_index, item_index, weight, city, package_zip])
            return truck1_route

    elif truck_number == 2:
        index = len(routeinfo)
        if index > 0:
            index - 1
            minval = get_min(routeinfo)
            truck2_route.append(minval)
            routelist2.remove(routelist2[minval[7]])
            start_location = minval[8]
            return shortest_route_recursion(routelist2, adjacency_list, start_location, truck_number)
        else:

            end_location = 0
            start_location = truck2_route[-1][8]
            distance_float = float(adjacency_list[end_location][start_location][1])
            delivery_location = distance_name_list[0][2]
            delivered_timestamp = ''
            packageid = 'Returning to hub'
            dead_line = ''
            start_time = ''
            status = ''
            route_index = 0
            item_index = 0
            weight = 0
            city = 0
            package_zip = 0
            
            #Return to HUB
            truck2_route.append([packageid, delivery_location, dead_line, distance_float, start_time, status, delivered_timestamp, route_index, item_index, weight, city, package_zip])
            return truck2_route
    
    elif truck_number == 3:
        index = len(routeinfo)
        if index > 0:
            index - 1
            minval = get_min(routeinfo)
            truck3_route.append(minval)
            routelist2.remove(routelist2[minval[7]])
            start_location = minval[8]
            return shortest_route_recursion(routelist2, adjacency_list, start_location, truck_number)
        else:

            end_location = 0
            start_location = truck3_route[-1][8]
            distance_float = float(adjacency_list[end_location][start_location][1])
            delivery_location = distance_name_list[0][2]
            delivered_timestamp = ''
            packageid = 'Returning to hub'
            dead_line = ''
            start_time = ''
            status = ''
            route_index = 0
            item_index = 0
            weight = 0
            city = 0
            package_zip = 0
            
            #Return to HUB
            truck3_route.append([packageid, delivery_location, dead_line, distance_float, start_time, status, delivered_timestamp, route_index, item_index, weight, city, package_zip])
            return truck3_route
    
    else:
        print("Invalid truck number")