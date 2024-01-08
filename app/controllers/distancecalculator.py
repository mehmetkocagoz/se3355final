import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in kilometers

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c  # Distance in kilometers
    return distance

def calculate_distance(selected_town,town_list):
    print(town_list)
    print(selected_town)
    for town in town_list:
        if town['town_name'] == selected_town:
            selected_town_info = town
    closest_town_list = []
    for town in town_list:
        distance = haversine(selected_town_info['town_latitude'],selected_town_info['town_longitude'],town['town_latitude'],town['town_longitude'])
        if distance <= 30:
            closest_town_list.append(town)
    print(closest_town_list)
    return closest_town_list