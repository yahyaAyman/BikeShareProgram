'''CSC108 Assignment 2 Starter code'''

from typing import List, TextIO
# A type to represent cleaned (see clean_data()) for multiple stations
SystemData = List[List[object]]
# A type to represent cleaned data for one station
StationData = List[object]
# A type to represent a list of stations
StationList = List[int]
import math


####### CONSTANTS ##################################

# A set of constants representing a list index for particular
# station information.
ID = 0
NAME = 1
LATITUDE = 2
LONGITUDE = 3
CAPACITY = 4
BIKES_AVAILABLE = 5
DOCKS_AVAILABLE = 6
IS_RENTING = 7
IS_RETURNING = 8


####### BEGIN HELPER FUNCTIONS ####################

def is_number(value: str) -> bool:
    '''Return True iff value represents a decimal number.

    >>> is_number('csc108')
    False
    >>> is_number('  108 ')
    True
    >>> is_number('+3.14159')
    True
    '''

    return value.strip().lstrip('+-').replace('.', '', 1).isnumeric()


# It isn't necessary to call this function to implement your bikes.py
# functions, but you can use it to create larger lists for testing.
# See the main block below for an example of how to do that.
def csv_to_list(csv_file: TextIO) -> List[List[str]]:
    '''Return the contents of the open CSV file csv_file as a list of lists,
    where each inner list contains the values from one line of csv_file.

    Docstring examples not provided since results depend on a data file.
    '''

    # Read and discard the header
    csv_file.readline()

    data = []
    for line in csv_file:
        data.append(line.strip().split(','))
    return data


### SAMPLE DATA TO USE IN DOCSTRING EXAMPLES ####
# You will wish to add additional examples, but when you do, either
# create new constants or update the results that use these examples.

SAMPLE_STATIONS = [
    [7087, 'Danforth/Aldridge', 43.684371, -79.316756, 23, 9, 14, True, True],
    [7088, 'Danforth/Coxwell', 43.683378, -79.322961, 15, 13, 2, False, False]]

HANDOUT_STATIONS = [
    [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 20, 11, True, True],
    [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907,
     15, 5, 10, True, True]]


####### FUNCTIONS TO WRITE ########################

def clean_data(data: List[List[str]]) -> None:
    '''Modify the list data by converting each string in data to:
        . an int iff if it represents a whole number
        . a float iff it represents a number that is not a whole number
        . True or False iff the string is 'True' or 'False', respectively
        . None iff the string is 'null' or the empty string
    and leaving the string as it is otherwise.

    >>> d = [['abc', '123', '45.6', 'True', 'False']]
    >>> clean_data(d)
    >>> d
    [['abc', 123, 45.6, True, False]]
    >>> d = [['ab2'], ['-123'], ['False', '3.2']]
    >>> clean_data(d)
    >>> d
    [['ab2'], [-123], [False, 3.2]]


    >>> d = [['abc', '-123', '-45.6', 'False', 'False']]
    >>> clean_data(d)
    >>> d
    [['abc', -123, -45.6, False, False]]
    >>> d = [['abc', '-123', '-45.6', 'True'], [], ['']]
    >>> clean_data(d)
    >>> d
    [['abc', -123, -45.6, True], [], [None]]
    >>> d = [['abc2', '123', '-45.6', ''], [], ['0.35', ''], ['-105', 'True']]
    >>> clean_data(d)
    >>> d
    [['abc2', 123, -45.6, None], [], [0.35, None], [-105, True]]
    >>> d = [['1289a', '0', '12.5', '***'], [''], ['0.35', 'True'], ['', 'False']]
    >>> clean_data(d)
    >>> d
    [['1289a', 0, 12.5, '***'], [None], [0.35, True], [None, False]]
    '''

    for index1 in range (len(data)):
        for index2 in range (len(data[index1])):

            #converting the str 'True' to the boolean True
            if data[index1][index2] == 'True':
                data[index1][index2] = True
                
            #converting the str 'False' to the boolean False
            elif data[index1][index2] == 'False':
                data[index1][index2] = False

            #converting the str 'int' to just int                
            elif data[index1][index2].replace('-', '').isdigit():
                data[index1][index2]= int(data[index1][index2])

             #converting the str 'float' to just float                                
            elif is_number(data[index1][index2].replace('-','')):
                 data[index1][index2]= float(data[index1][index2])                

            #converting the empty string to just None                
            elif data[index1][index2] == '' or data[index1][index2] == ['']:
                data[index1][index2] = None
                
            
def get_station_info(station_id: int, stations: SystemData) -> StationData:
    '''Return a list containing the following information from stations
    about the station with id number station_id:
        . station name
        . number of bikes available
        . number of docks available
    (in this order)

    Precondition: station_id will appear in stations.

    >>> get_station_info(7087, SAMPLE_STATIONS)
    ['Danforth/Aldridge', 9, 14]
    >>> get_station_info(7088, SAMPLE_STATIONS)
    ['Danforth/Coxwell', 13, 2]


    >>> get_station_info(7031, bike_stations)
    ['Jarvis St / Isabella St', 3, 20]
    >>> get_station_info(7216, bike_stations)
    ['Wellington Dog Park', 14, 9]  
    >>> get_station_info(7170, bike_stations)
    ['Spadina / Willcocks', 2, 13]
    >>> get_station_info(7120, bike_stations)
    ['Gerrard/River', 9, 2]
    '''
    
    stations_list = []

    for index in range (len(stations)):
        if stations[index][ID] == station_id:
            stations_list.append(stations [index][NAME])
            stations_list.append(stations [index][BIKES_AVAILABLE])
            stations_list.append(stations[index][DOCKS_AVAILABLE])
    
    return stations_list

def get_total(index: int, stations: SystemData) -> int:
    '''Return the sum of the column in stations given by index.

    Precondition: the items in stations at the position
                  that index refers to are ints.

    >>> get_total(BIKES_AVAILABLE, SAMPLE_STATIONS)
    22
    >>> get_total(DOCKS_AVAILABLE, SAMPLE_STATIONS)
    16

    >>> get_total(CAPACITY, SAMPLE_STATIONS)
    38
    >>> get_total(BIKES_AVAILABLE, HANDOUT_STATIONS)
    25
    >>> get_total(CAPACITY, SAMPLE_STATIONS)
    46
    >>> get_total(BIKES_AVAILABLE, bike_stations)
    1384
    '''
    total = 0
    
    for station in range (len(stations)):
        total += stations[station][index]

    return total

    


def get_station_with_max_bikes(stations: SystemData) -> int:
    '''Return the station ID of the station that has the most bikes available.
    If there is a tie for the most available, return the station ID that appears
    first in stations.

    Precondition: len(stations) > 0

    >>> get_station_with_max_bikes(SAMPLE_STATIONS)
    7088


    >>> get_station_with_max_bikes(HANDOUT_STATIONS)
    7000
    >>> get_station_with_max_bikes(bike_stations)
    7075
    >>> mix_stations = [[7087, 'Danforth/Aldridge', 43.684371, -79.316756, 23, 9, 14, True, True],
    [7088, 'Danforth/Coxwell', 43.683378, -79.322961, 15, 13, 2, False, False],
    [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 20, 11, True, True],
    [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907, 15, 5, 10, True, True]]
    >>> get_station_with_max_bikes(mix_stations)
    7000
    '''

    highest_value = stations[0][BIKES_AVAILABLE]
    place_value_id = stations[0][ID]

    
    for index in range (len(stations)):
        if stations[index][BIKES_AVAILABLE] > highest_value:
            place_value_id = stations[index][ID]

    return place_value_id               


def get_stations_with_n_docks(n: int, stations: SystemData) -> StationList:
    '''Return a list containing the station IDs for the stations in stations
    that have at least n docks available, in the same order as they appear
    in stations.

    Precondition: n >= 0

    >>> get_stations_with_n_docks(2, SAMPLE_STATIONS)
    [7087, 7088]
    >>> get_stations_with_n_docks(5, SAMPLE_STATIONS)
    [7087]

    >>> get_stations_with_n_docks(0, HANDOUT_STATIONS)
    [7000, 7001]
    >>> get_stations_with_n_docks(11, HANDOUT_STATIONS)
    [7000]
    >>> get_stations_with_n_docks(18, HANDOUT_STATIONS)
    []
    >>> get_stations_with_n_docks(25, bike_stations)
    [7019, 7020, 7021, 7022, 7028, 7048, 7052, 7057]
    '''

    station_list = []

    for index in range (len(stations)):
        if stations[index][DOCKS_AVAILABLE] >= n:
            station_list.append(stations[index][ID])

    return station_list
        


def get_direction(start_id: int, end_id: int, stations: SystemData) -> str:
    '''Return a string that contains the direction to travel to get from
    station start_id to station end_id according to data in stations.

    Precondition: start_id and end_id will appear in stations.
    theta = atan2(delta_y, delta_x)

    >>> get_direction(7087, 7088, SAMPLE_STATIONS)
    'WEST'

    >>> get_direction(7136, 7000, bike_stations)
    'EAST'
    >>> get_direction(7174, 7216, bike_stations)
    'SOUTHEAST'
    >> get_direction(7031, 7017, bike_stations)
    'SOUTH'
    >>> get_direction(7033, 7019, bike_stations)
    'NORTH'
    >>> get_direction(7090, 7128, bike_stations)
    'WEST'
    >>> get_direction(7101, 7009, bike_stations)
    'NORTHWEST'
    '''

    for index in range (len(stations)):
        if stations[index][ID] == start_id:
            latitude_x1 = math.radians(stations[index][LATITUDE])
            longitude_y1 = math.radians(stations[index][LONGITUDE])
            
        if stations[index][ID] == end_id:
            latitude_x2 = math.radians(stations[index][LATITUDE])
            longitude_y2 = math.radians(stations[index][LONGITUDE])


    y_component = math.cos(latitude_x2) * math.sin(longitude_y2 - longitude_y1)
    x_component = math.sin(latitude_x2) * math.cos(latitude_x1) - (math.cos(longitude_y2 - longitude_y1) * math.sin(latitude_x1) * math.cos(latitude_x2))

    angle_alpha = math.degrees(math.atan2(y_component , x_component))

    if  angle_alpha < 0:
        angle_alpha = angle_alpha + 360
        
    if angle_alpha >= 247.5 and  angle_alpha < 292.5:
        return 'WEST'
    if angle_alpha >= 202.5 and angle_alpha < 247.5:
        return 'SOUTHWEST'
    if angle_alpha >= 157.5 and angle_alpha < 202.5:
        return 'SOUTH'
    if angle_alpha >= 112.5 and angle_alpha < 157.5:
        return 'SOUTHEAST'
    if angle_alpha >= 67.5 and angle_alpha < 112.5:
        return 'EAST'
    if angle_alpha >= 22.5 and angle_alpha < 67.5: 
        return 'NORTHEAST'
    if angle_alpha >= 292.5 and angle_alpha < 337.5:
        return 'NORTHWEST'
    if angle_alpha >= 337.5 and angle_alpha <= 360:
        return 'NORTH'
    if angle_alpha >= 0 and angle_alpha < 22.5:
        return 'NORTH'
 
    
def rent_bike(station_id: int, stations: SystemData) -> bool:
    '''Update the specified available bike count and the docks available
    count in stations, if possible. Return True iff the rental from
    station_id was successful.

    Precondition: station_id will appear in stations.

    >>> station_id = SAMPLE_STATIONS[0][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    >>> rent_bike(station_id, SAMPLE_STATIONS)
    True
    >>> original_bikes_available - 1 == SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    True
    >>> original_docks_available + 1 == SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    True
    >>> station_id = SAMPLE_STATIONS[1][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    >>> rent_bike(station_id, SAMPLE_STATIONS)
    False
    >>> original_bikes_available == SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    True
    >>> original_docks_available == SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    True

    >>> station_id = HANDOUT_STATIONS[0][ID]
    >>> original_bikes_available = HANDOUT_STATIONS[0][BIKES_AVAILABLE]
    >>> original_docks_available = HANDOUT_STATIONS[0][DOCKS_AVAILABLE]
    >>> rent_bike(station_id, HANDOUT_STATIONS)
    True
    >>> example_stations = [[7087, 'Danforth/Aldridge', 43.684371, -79.316756, 23, 9, 14, True, True],
    [7088, 'Danforth/Coxwell', 43.683378, -79.322961, 15, 13, 2, False, False],
    [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 20, 11, False, True]]
    >>> station_id = example_stations[2][ID]
    >>> original_bikes_available = example_stations[0][BIKES_AVAILABLE]
    >>> original_docks_available = example_stations[0][DOCKS_AVAILABLE]
    >>> rent_bike(station_id, example_stations)
    False
    >>> sample = [[7087, 'Danforth/Aldridge', 43.684371, -79.316756, 23, 9, 14, True, True],
    [7088, 'Danforth/Coxwell', 43.683378, -79.322961, 15, 13, 2, False, False],
    [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 20, 11, False, True],
    [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907,15, 5, 10, True, True]]
    >>> station_id = sample[3][ID]
    >>> original_bikes_available = sample[0][BIKES_AVAILABLE]
    >>> original_docks_available = sample[0][DOCKS_AVAILABLE]
    >>> rent_bike(station_id, sample)
    True
    '''

    for index in range (len(stations)):
        if stations[index][ID] == station_id:
            if stations[index][IS_RENTING] and stations[index][BIKES_AVAILABLE] >= 1:
                stations[index][BIKES_AVAILABLE] -= 1
                stations[index][DOCKS_AVAILABLE] += 1
                return True
            return False
        return False

def return_bike(station_id: int, stations: SystemData) -> bool:
    '''Update stations by incrementing the appropriate available bike
    count and decrementing the docks available count, if possible.
    Return True iff a bike is successfully returned to station_id.

    Precondition: station_id will appear in stations.

    >>> station_id = SAMPLE_STATIONS[0][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    >>> return_bike(station_id, SAMPLE_STATIONS)
    True
    >>> original_bikes_available + 1 == SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    True
    >>> original_docks_available - 1 == SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    True
    >>> station_id = SAMPLE_STATIONS[1][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    >>> return_bike(station_id, SAMPLE_STATIONS)
    False
    >>> original_bikes_available == SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    True
    >>> original_docks_available == SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    True


    >>> station_id = HANDOUT_STATIONS[0][ID]
    >>> original_bikes_available = HANDOUT_STATIONS[0][BIKES_AVAILABLE]
    >>> original_docks_available = HANDOUT_STATIONS[0][DOCKS_AVAILABLE]
    >>> return_bike(station_id, HANDOUT_STATIONS)
    True
    >>> sample1 = [[7087, 'Danforth/Aldridge', 43.684371, -79.316756, 23, 9, 14, True, True],
    [7088, 'Danforth/Coxwell', 43.683378, -79.322961, 15, 13, 2, False, False],
    [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 20, 11, True, False]]
    >>> station_id = sample1[2][ID]
    >>> original_bikes_available = sample1[0][BIKES_AVAILABLE]
    >>> original_docks_available = sample1[0][DOCKS_AVAILABLE]
    >>> return_bike(station_id, sample1)
    False
    >>> sample2 = [[7087, 'Danforth/Aldridge', 43.684371, -79.316756, 23, 9, 14, True, True],
    [7005, 'University Ave / King ST W', 43.64809, -79.3847, 19, 0, 18, True, True],
    [7047, 'University Ave / Gerrard ST W', 43.65776, -79.3892, 11, 2, 9, True, False]]
    >>> station_id = sample2[1][ID]
    >>> original_bikes_available = sample2[1][BIKES_AVAILABLE]
    >>> original_docks_available = sample2[1][DOCKS_AVAILABLE]
    >>> return_bike(station_id, sample2)
    True
    '''
    for index in range (len(stations)):
        if stations[index][ID] == station_id:
            if stations[index][IS_RETURNING] and stations[index][DOCKS_AVAILABLE] >= 1:
                stations[index][BIKES_AVAILABLE] +=  1
                stations[index][DOCKS_AVAILABLE] -=  1
                return True
            return False
        return False


def calculate_variance(stations: SystemData ) -> float:


    mean = get_total(BIKES_AVAILABLE, stations) / get_total(CAPACITY, stations)*100
    variance = 0
    for station in stations:
        if station[IS_RETURNING] or station[IS_RENTING]:
            variance += (-(station[BIKES_AVAILABLE] / station[CAPACITY])*100 +mean)**2

    return (variance / len(stations))

##def calculate_variance(stations: SystemData ) -> float:
##    available_bikes_total = 0
##    total_docks_capacity = 0
##    individual_percentage = []
##    variance =0
## #GET THE TOTAL PERCENTAGE 
##    for index in range (len(stations)):
##        available_bikes_total += stations[index][BIKES_AVAILABLE]
##        total_docks_capacity += stations[index][CAPACITY]
##    
##    percentage_available = (available_bikes_total / total_docks_capacity)
##
##        
##    #GET INDIVIDUAL PERCENTAGE
##    for index2 in range(len(stations)):
##        individual_percentage.append((stations[index2][BIKES_AVAILABLE]/stations[index2][CAPACITY]))
##
##
##
##    for index3 in range(len(individual_percentage)):
##        variance += ((individual_percentage[index3]- percentage_available) ** 2)/ len(individual_percentage)
##
##    return variance
##        bikes_total = stations[BIKES_AVAILABLE] + station2[BIKES_AVAILABLE]

def balance_all_bikes(stations: SystemData) -> None:
    '''Update stations by redistributing bikes so that, as closely as
    possible, all bike stations has the same percentage of bikes available.

    >>> balance_all_bikes(HANDOUT_STATIONS)
    >>> HANDOUT_STATIONS == [\
     [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 17, 14, True, True],\
     [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907,\
     15, 8, 7, True, True]]
    True
    '''
    # Notes:
    # Calculate the percentage of bikes available across all stations
    # and balance the number of bikes available at each station so that
    # the percentage is similar across all stations.
    #
    # Remove bikes from a station if and only if the station is renting
    # and there is a bike available to rent, and return a bike if and
    # only if the station is allowing returns and there is a dock
    # available.
    

    new_variance = 0
    placeholder = 0

    old_variance = calculate_variance(stations)
    print('old_variance', old_variance)

    for station1 in range (len(stations)):
                
                for station2 in range (1,len(stations)):
                  
                    

                    while old_variance > new_variance and placeholder <= new_variance:
                            placeholder = new_variance

                            stations[station2][BIKES_AVAILABLE] +=  1
                            stations[station2][DOCKS_AVAILABLE] -=  1            
                            stations[station1][BIKES_AVAILABLE] -= 1
                            stations[station1][DOCKS_AVAILABLE] += 1
                            print(stations)
                            new_variance = calculate_variance(stations)
                            print('new_variance',new_variance)


                            if old_variance < new_variance :
                                
                                stations[station1][BIKES_AVAILABLE] +=  1
                                stations[station1][DOCKS_AVAILABLE] -=  1            
                                stations[station2][BIKES_AVAILABLE] -= 1
                                stations[station2][DOCKS_AVAILABLE] += 1


                            #variance = new_variance
                          #  print('****')
               
                    stations[station2][BIKES_AVAILABLE] +=  1
                    stations[station2][DOCKS_AVAILABLE] -=  1            
                    stations[station1][BIKES_AVAILABLE] -= 1
                    stations[station1][DOCKS_AVAILABLE] += 1

    print(stations)
    print('old_variance', old_variance)



































##def calculate_variance(station1: float, station2: float) -> float:
##
##        
##        bikes_total = station1[BIKES_AVAILABLE] + station2[BIKES_AVAILABLE]
##        total_capacity = station1[CAPACITY] + station2[CAPACITY]        
##        target = bikes_total/total_capacity
##    
##        return (((station1[BIKES_AVAILABLE]/station1[CAPACITY]) - target) **2 + ((station2[BIKES_AVAILABLE]/station2[CAPACITY])- target)**2) /2
##    
####def can_rent (station_id: int, stations: SystemData) -> bool:
####
###### for index in range (len(stations)):
######        if stations[index][ID] == station_id:
######            if stations[index][IS_RENTING] and stations[index][BIKES_AVAILABLE] >= 1:
######                return True
######            return False
######        return False
##            
##def balance_all_bikes(stations: SystemData) -> None:
##    '''Update stations by redistributing bikes so that, as closely as
##    possible, all bike stations has the same percentage of bikes available.
##
##    >>> balance_all_bikes(HANDOUT_STATIONS)
##    >>> HANDOUT_STATIONS == [\
##     [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 17, 14, True, True],\
##     [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907,\
##     15, 8, 7, True, True]]
##    True
##    '''
##    # Notes:
##    # Calculate the percentage of bikes available across all stations
##    # and balance the number of bikes available at each station so that
##    # the percentage is similar across all stations.
##    #
##    # Remove bikes from a station if and only if the station is renting
##    # and there is a bike available to rent, and return a bike if and
##    # only if the station is allowing returns and there is a dock
##    # available.
##
##    available_bikes_total = 0
##    total_docks_capacity = 0
##    individual_percentage = []
##    variance =0
## #GET THE TOTAL PERCENTAGE 
##    for index in range (len(stations)):
##        available_bikes_total += stations[index][BIKES_AVAILABLE]
##        total_docks_capacity += stations[index][CAPACITY]
##    
##    percentage_available = (available_bikes_total / total_docks_capacity)
##
##        
##    #GET INDIVIDUAL PERCENTAGE
##    for index2 in range(len(stations)):
##        individual_percentage.append((stations[index2][BIKES_AVAILABLE]/stations[index2][CAPACITY]))
##
##
##
##    for index3 in range(len(individual_percentage)):
##        variance += ((individual_percentage[index3]- percentage_available) ** 2)/ len(individual_percentage)
##
##    old_variance=variance
##    new_variance = 0
##    placeholder = 0
##
##    for station1 in range (len(stations)):                
##                for station2 in range (1,len(stations)):
##                  #  old_variance = calculate_variance(stations[station1], stations[station2])
##
##                    if stations[station1][IS_RENTING] and stations[station1][BIKES_AVAILABLE] >= 1 and stations[station2][IS_RETURNING] and stations[station2][DOCKS_AVAILABLE] >= 1:
##
##                        while old_variance > new_variance and old_variance <= new_variance:
##                            placeholder = new_variance
##                            if stations[station1][IS_RENTING] and stations[station1][BIKES_AVAILABLE] >= 1 and stations[station2][IS_RETURNING] and stations[station2][DOCKS_AVAILABLE] >= 1:
##
##                                
##                                stations[station2][BIKES_AVAILABLE] +=  1
##                                stations[station2][DOCKS_AVAILABLE] -=  1            
##                                stations[station1][BIKES_AVAILABLE] -= 1
##                                stations[station1][DOCKS_AVAILABLE] += 1
##                                new_variance = calculate_variance(stations[station1], stations[station2])
##
##
##                            if old_variance < new_variance :
##                                
##                                stations[station1][BIKES_AVAILABLE] +=  1
##                                stations[station1][DOCKS_AVAILABLE] -=  1            
##                                stations[station2][BIKES_AVAILABLE] -= 1
##                                stations[station2][DOCKS_AVAILABLE] += 1
##               
##                        stations[station2][BIKES_AVAILABLE] +=  1
##                        stations[station2][DOCKS_AVAILABLE] -=  1            
##                        stations[station1][BIKES_AVAILABLE] -= 1
##                        stations[station1][DOCKS_AVAILABLE] += 1
##    print(new_variance)
##    print(stations)

######
######def helper9(stations: SystemData)-> float:
######   # return individual_percentage
######    available_bikes_total = 0
######    total_docks_capacity = 0
######    individual_percentage = []
######    variance =0
######    Sum =0
###### #GET THE TOTAL PERCENTAGE 
######    total_bikes = get_total(BIKES_AVAILABLE, stations)
######    total_capacity = get_total(CAPACITY, stations)
######    percentage = (total_bikes/total_capacity)
######
######        
######    #GET INDIVIDUAL PERCENTAGE
######    for index2 in range(len(stations)):
######        individual_percentage.append((stations[index2][BIKES_AVAILABLE]/stations[index2][CAPACITY]))
######
######    for index3 in range(len(individual_percentage)):
######        Sum += ((individual_percentage[index3]- percentage) ** 2)
######    variance = Sum / (len(individual_percentage))
######
######    return variance
######
######def balance_all_bikes(stations: SystemData) -> None:
######
######
######    total_bikes = get_total(BIKES_AVAILABLE, stations)
######    total_capacity = get_total(CAPACITY, stations)
######    percentage = (total_bikes/total_capacity)
######    old_variance = helper9(stations)
######    new_variance = 0
######    print('$$$',old_variance)
######    for i in range (len(stations)):
######
######        j=0
######        while old_variance < new_variance:
######            if j == i:
######                j= j+1
######  
######            print('$',j)   
######            if stations[i][IS_RETURNING] and stations[j][IS_RENTING]:
######                stations[i][BIKES_AVAILABLE] +=  1
######                stations[i][DOCKS_AVAILABLE] -=  1            
######                stations[j][BIKES_AVAILABLE] -= 1
######                stations[j][DOCKS_AVAILABLE] += 1
######            new_variance = helper9(stations)
######            print('$$',new_variance)
######            print('$$$',old_variance)
######            if j < 1:
######                j=j+1
######            
######                
######
######        stations[j][BIKES_AVAILABLE] +=  1
######        stations[j][DOCKS_AVAILABLE] -=  1            
######        stations[i][BIKES_AVAILABLE] -= 1
######        stations[i][DOCKS_AVAILABLE] += 1
######        j = 0
######        while old_variance > new_variance:
######            if j == i:
######                j= j+1
######            print('*',j)     
######            if stations[i][IS_RENTING] and stations[j][IS_RETURNING]:
######                stations[j][BIKES_AVAILABLE] +=  1
######                stations[j][DOCKS_AVAILABLE] -=  1            
######                stations[i][BIKES_AVAILABLE] -= 1
######                stations[i][DOCKS_AVAILABLE] += 1
######            new_variance = helper9(stations)
######            print('**',new_variance)
######
######            if j < len(stations):
######                j=j+1
######            else:
######                break
######
######         
######        stations[i][BIKES_AVAILABLE] +=  1
######        stations[i][DOCKS_AVAILABLE] -=  1            
######        stations[j][BIKES_AVAILABLE] -= 1
######        stations[j][DOCKS_AVAILABLE] += 1
######
######    print(stations)
######
######
######
######
######















        
if __name__ == '__main__':
    # # To test your code with larger lists, you can uncomment the code below to
    # # read data from the provided CSV file.
    stations_file = open('stations.csv')
    bike_stations = csv_to_list(stations_file)
    clean_data(bike_stations)

    # # For example,
    # print('Testing get_station_with_max_bikes: ', \
    #     get_station_with_max_bikes(bike_stations) == 7033)

##def _test():
##    import doctest
##    doctest.testmod()
##if __name__ == "__main__":
##    _test()
##    
