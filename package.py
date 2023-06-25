from datetime import datetime

#Prints all packages and their current status to console-> O(n)
def snapshot(time, routelist):
    input_time = datetime.strptime(time, "%H:%M")
    
    for item in routelist:
        datetime_start = datetime.strptime(item[4], '%Y-%m-%d %H:%M:%S')
        datetime_delivery = datetime.strptime(item[6], '%Y-%m-%d %H:%M:%S')
        
        if 9 == item[0]:
            item[1] = wrong_address(time, "300 State St", "410 S State St")
            
        item[5] = get_status(input_time, datetime_start, datetime_delivery, item[5])
        
        dash = '-' * 112
        delivery_time = is_delivered(item[6], input_time)
        
        if item[0] == 1:
            print(dash)
            print('{:<4}{:<40s}{:<10s}{:<17s}{:<8s}{:<7s}{:<11s}{:<16s}'.format("id","delivery_address","deadline","city","zipcode","weight","status", "delivery_time"))
            print(dash)
            print('{:<4}{:<40s}{:<10s}{:<17s}{:<8s}{:<7s}{:<16s}{:<16s}'.format(item[0],item[1],item[2],item[10], item[11], item[9], font_color(item[5]), delivery_time))
        else:
            print('{:<4}{:<40s}{:<10s}{:<17s}{:<8s}{:<7s}{:<16s}{:<16s}'.format(item[0],item[1],item[2],item[10], item[11], item[9], font_color(item[5]), delivery_time))
 
#Get package by id and check status by time->O(n)           
def get_package(packageid, time, routelist):
    input_time = datetime.strptime(time, "%H:%M")
    isfound = False
    
    for item in routelist:
        if 9 == item[0]:
            item[1] = wrong_address(time, "300 State St", "410 S State St")
            
        if int(packageid) == item[0]:
            
            print("\nPackage located!!")
            isfound = True
            datetime_start = datetime.strptime(item[4], '%Y-%m-%d %H:%M:%S')
            datetime_delivery = datetime.strptime(item[6], '%Y-%m-%d %H:%M:%S')
            
            item[5] = get_status(input_time, datetime_start, datetime_delivery, item[5])
            
            dash = '-' * 112
            delivery_time = is_delivered(item[6], input_time)
            print(dash)
            print('{:<4}{:<40s}{:<10s}{:<17s}{:<8s}{:<7s}{:<11s}{:<16s}'.format("id","delivery_address","deadline","city","zipcode","weight","status", "delivery_time"))
            print(dash)
            print('{:<4}{:<40s}{:<10s}{:<17s}{:<8s}{:<7s}{:<16s}{:<16s}'.format(item[0],item[1],item[2],item[10], item[11], item[9], font_color(item[5]), delivery_time))
            print("\n")
    if isfound == False:
        print(f"Package '{packageid}' not found please check package id")

#Return colored text to console based on given string->O(1)
def font_color(string):
    
    if string == 'At HUB':#red
        value = "\033[0;31m"
        
    elif string == 'DELIVERED->':#green
        value = "\033[0;32m"
        
    elif string == 'En ROUTE':#yellow
        value = "\033[0;33m"
        
    elif string == '!!Attention!!':
        value = "\033[0;33m"
        
    else:
        value = "\033[0;36m"#cyan
        
    close = '\033[00m'
    
    return value + string + close

#Checks if package was delivered or not -> O(1)
def is_delivered(delivery_time, current_time):
    delivery_time = datetime.strptime(delivery_time, '%Y-%m-%d %H:%M:%S')
    if delivery_time < current_time:
        return str(delivery_time)[-8:]
    else:
        return ''

#Checks and sets status of package based on time of delivery and time searched for -> O(1)
def get_status(input_time1, datetime_start1, datetime_delivery1, item1):
    item1 = item1
    if input_time1 >= datetime_start1 and input_time1 < datetime_delivery1:
        item1 = 'En ROUTE'
        
    elif input_time1 < datetime_start1:
        item1 = 'At HUB'
        
    elif input_time1 >= datetime_delivery1:
        item1 = 'DELIVERED->'
    
    return item1

#Checks if package with wrong address has updated address -> O(1)
def wrong_address(input_time, old_address, new_address):
    type(old_address)
    current_time = datetime.strptime(input_time, "%H:%M")
    address_change_time = datetime.strptime("10:20", "%H:%M")
    
    attention_message = font_color("!!Attention!!")
    
    if current_time < address_change_time:
        return old_address
    else:
        print(f"\n{ attention_message }Package '9' address was updated at '10:20'")
        return new_address