# Controller will interact with model which is vehicle

from app.vehicle import getAllVehicles

# We will group vehicles by their price
# Some additional grouping or business logic can be apply
def getAll():
    vehicle_list = getAllVehicles()
    grouped_vehicles = {}
    for vehicle in vehicle_list:
        group_key = getattr(vehicle, 'DailyRentPrice')

        if group_key not in grouped_vehicles:
            grouped_vehicles[group_key] = []

        grouped_vehicles[group_key].append(vehicle)
    print(grouped_vehicles.keys())
    return grouped_vehicles