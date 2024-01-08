from app.models.office import list_of_offices,office_id_query,car_id_list_query,city_id_query,town_list_query,lat_long_query

def takeOfficeListFromDatabase(user_city):
    if isinstance(user_city, tuple):
        user_city = user_city[0]
    
    user_city = user_city.upper()
    user_city = user_city.replace('I','İ')
    offices = list_of_offices(user_city)
    office_list = []
    for office in offices:
        officeDict = {
            'city' : office.city,
            'title' : office.title,
            'address' : office.address,
            'number' : office.phone_number
        }
        office_list.append(officeDict)
    
    return office_list

def takeOfficesCarListFromDatabase(pickup_office):
    # First we need office_id
    office_id = office_id_query(pickup_office)

    # Then form car_office_assignment table take car_ids

    car_id_list = car_id_list_query(office_id)
    # car_id_list is a tuple like (2,),(3,)
    # Therefore make it a list o values
    car_id_list_values = [item[0] for item in car_id_list]
    return car_id_list_values

def takeCityIdFromDatabase(user_city):
    city_id = city_id_query(user_city)
    city_id = city_id[0]
    return city_id

def takeTownListFromDatabase(city_id):
    town_list = town_list_query(city_id)


    towns = []
    for town in town_list:
        town_name = town[2]
        town_latitude = town[3]
        town_longitude = town[4]

        town_dict = {
            "town_name" : town_name,
            "town_latitude" : town_latitude,
            "town_longitude" : town_longitude
        }
        towns.append(town_dict)
    return towns

def takeLatLong(town_name):
    info = lat_long_query(town_name)
    lat = info[0][0]
    long = info[0][1]
    return lat,long