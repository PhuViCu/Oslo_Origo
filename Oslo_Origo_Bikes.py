import requests

def read_API(url, header):
    response = requests.get(url, headers=header)
    API_data = response.json()

    return API_data
#
#The function breaks the data down to a (key, value)-pair,
#and then check the key, and put the value into the corresponding list
#
def get_data(data, key, list1, list2, list3, list4):
    if type(data[key]) is dict:
        for newkey in data[key].keys():
            get_data(data[key], newkey, list1, list2, list3, list4)

    elif type(data[key]) is list:
        for i in range(0,len(data[key])):
            get_data(data[key], i, list1, list2, list3, list4)
    else:
        if (key == 'title'):
            list1.append(data[key])
        elif (key == 'number_of_locks'):
            list2.append(data[key])
        elif (key == 'bikes'):
            list3.append(data[key])
        elif (key == 'id'):
            list4.append(data[key])

def print_to_screen():
    print("{0:35s} {1:20s} {2:10s}".format("Station", "Number Of locks", "Available bikes"))
    print("")

    for i in range(0,len(StationsList)):
        print("{0:40}".format(StationsList[i]), end=' ') #Station's name
        print("{0:<20}".format(LocksList[i]), end=' ')   # Available locks
        station_id = StationIdList[i]                    # Get station's ID at index i
        # Get index of the station_ID that is contained in BikeIdList
        bike_id_index = BikeIdList.index(station_id)
        # Get the available bikes from the BikesList at the bike_id_index,
        # because BikeIdList and BikesList have the same order of the indexes
        print("{0:<10}".format(BikesList[bike_id_index]))

#################################################
### Main program
#################################################

URL_STATIONS = "https://oslobysykkel.no/api/v1/stations"
URL_BIKES = "https://oslobysykkel.no/api/v1/stations/availability"
API_KEY = 'YOUR API_KEY'
HEADER={'Client-Identifier': API_KEY}

StationsList = []  # Names of the stations
LocksList = []     # The number of locks at each station
BikesList = []     # Avaiable bibes at each station
StationIdList = [] # Id of the station contained in station_API
BikeIdList = []    # Id of the station contained in Bikes_API

Stations_API = read_API(URL_STATIONS, HEADER)
Bikes_API    = read_API(URL_BIKES, HEADER)

for key in Stations_API.keys():
    get_data(Stations_API, key, StationsList, LocksList, BikesList, StationIdList)

for key in Bikes_API.keys():
    get_data(Bikes_API, key, StationsList, LocksList, BikesList, BikeIdList)

print_to_screen()

