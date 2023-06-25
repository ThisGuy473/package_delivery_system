import csv
from hash_table import HashMap

with open('./data/input_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    third_truck = []
    second_truck = []
    first_truck = []
    insert_hashmap = HashMap()

    #Inserts all rows from csv into hash table -> O(n)
    for row in csv_reader:
        package_id = row[0]
        package_address = row[1]
        package_city = row[2]
        package_state =  row[3]
        package_zip = row[4]
        package_delivery = row[5]
        package_weight = row[6]
        package_note = row[7]
        package_delivery_start_time = ''
        package_delivery_status = 'HUB'
        package_delivery_timestamp = ''

        new_value = [package_id, package_address, package_city, package_state, package_zip, package_delivery, package_weight, package_note, package_delivery_start_time, package_delivery_status, package_delivery_timestamp]
        
        if row[0] == '1':
            first_truck.append(new_value)
        if row[0] == '2':
            third_truck.append(new_value)
        if row[0] == '3':
            second_truck.append(new_value)
        if row[0] == '4':
            third_truck.append(new_value)
        if row[0] == '5':
            third_truck.append(new_value)
        if row[0] == '6':
            second_truck.append(new_value)
        if row[0] == '7':
            third_truck.append(new_value)
        if row[0] == '8':
            first_truck.append(new_value)
        if row[0] == '9':
            new_value[1] = "410 S State St"
            third_truck.append(new_value)
        if row[0] == '10':
            first_truck.append(new_value)
        if row[0] == '11':
            third_truck.append(new_value)
        if row[0] == '12':
            third_truck.append(new_value)
        if row[0] == '13':
            first_truck.append(new_value)
        if row[0] == '14':
            first_truck.append(new_value)
        if row[0] == '15':
            first_truck.append(new_value)
        if row[0] == '16':
            first_truck.append(new_value)
        if row[0] == '17':
            first_truck.append(new_value)
        if row[0] == '18':
            second_truck.append(new_value)
        if row[0] == '19':
            first_truck.append(new_value)
        if row[0] == '20':
            first_truck.append(new_value)
        if row[0] == '21':
            third_truck.append(new_value)
        if row[0] == '22':
            third_truck.append(new_value)
        if row[0] == '23':
            third_truck.append(new_value)
        if row[0] == '24':
            third_truck.append(new_value)
        if row[0] == '25':
            second_truck.append(new_value)
        if row[0] == '26':
            second_truck.append(new_value)
        if row[0] == '27':
            second_truck.append(new_value)
        if row[0] == '28':
            second_truck.append(new_value)
        if row[0] == '29':
            first_truck.append(new_value)
        if row[0] == '30':
            first_truck.append(new_value)
        if row[0] == '31':
            first_truck.append(new_value)
        if row[0] == '32':
            second_truck.append(new_value)
        if row[0] == '33':
            third_truck.append(new_value)
        if row[0] == '34':
            first_truck.append(new_value)
        if row[0] == '35':
            third_truck.append(new_value)
        if row[0] == '36':
            second_truck.append(new_value)
        if row[0] == '37':
            first_truck.append(new_value)
        if row[0] == '38':
            second_truck.append(new_value)
        if row[0] == '39':
            second_truck.append(new_value)
        if row[0] == '40':
            first_truck.append(new_value)
            
        insert_hashmap.insert(package_id, new_value)

    #returns hashmap object
    def get_hash_map():
        return insert_hashmap
    #returns all packages for first truck second load
    def third_truck_packages():
        return third_truck
    #returns all packages for second truck first load
    def second_truck_packages():
        return second_truck
    #returns all packages for first truck first load
    def first_truck_packages():
        return first_truck

    