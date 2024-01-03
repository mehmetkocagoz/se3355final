# Controller will interact with model which is vehicle
from app.vehicle import getAllVehiclesFromDatabase
import base64


def getAllWithOffice(car_id_list):
    vehicle_list = getAllVehiclesFromDatabase()
    
    vehicle_list_array = []
    for vehicle in vehicle_list:
        Image = vehicle.Image
        base64_image = base64.b64encode(Image).decode('utf-8')
        mime_type = 'image/jpeg'
        image_url = f'data:{mime_type};base64,{base64_image}'

        # Discount will be applied based on the type of the car.
        if vehicle.CarType == 'EKONOMİK':
            discountRate = 30
        else:
            discountRate = 35

        if vehicle.ID in car_id_list:
            discount = (vehicle.DailyRentPrice/100)*discountRate
            discountedPrice = vehicle.DailyRentPrice - discount
            vehicle_dict ={
                'CarType' : vehicle.CarType,
                'Brand' : vehicle.Brand,
                'Model' : vehicle.Model,
                'Transmission' : vehicle.Transmission,
                'FuelType' : vehicle.FuelType,
                'DepositPrice' : vehicle.DepositPrice,
                'DailyRentPrice' : vehicle.DailyRentPrice,
                'DiscountedPrice' : discountedPrice,
                'Discount' : discount,
                'DefaultKM' : vehicle.DefaultKM,
                'Image' : image_url
            }
            vehicle_list_array.append(vehicle_dict)
    
    return vehicle_list_array

    
def getAllVehicles():
    vehicle_list = getAllVehiclesFromDatabase()
    print("here")
    vehicle_list_array = []
    for vehicle in vehicle_list:
        Image = vehicle.Image
        base64_image = base64.b64encode(Image).decode('utf-8')
        mime_type = 'image/jpeg'
        image_url = f'data:{mime_type};base64,{base64_image}'

        # Discount will be applied based on the type of the car.
        if vehicle.CarType == 'EKONOMİK':
            discountRate = 30
        else:
            discountRate = 35

        
        discount = (vehicle.DailyRentPrice/100)*discountRate
        discountedPrice = vehicle.DailyRentPrice - discount
        vehicle_dict ={
                'CarType' : vehicle.CarType,
                'Brand' : vehicle.Brand,
                'Model' : vehicle.Model,
                'Transmission' : vehicle.Transmission,
                'FuelType' : vehicle.FuelType,
                'DepositPrice' : vehicle.DepositPrice,
                'DailyRentPrice' : vehicle.DailyRentPrice,
                'DiscountedPrice' : discountedPrice,
                'Discount' : discount,
                'DefaultKM' : vehicle.DefaultKM,
                'Image' : image_url
            }
        vehicle_list_array.append(vehicle_dict)
    
    return vehicle_list_array

def order_vehicle_list(car_type,price_order,transmission_type,vehicle_data):
    if price_order == 'DESC':
        ordered_vehicle_list = sorted(vehicle_data, key=lambda x: x['DailyRentPrice'], reverse=True)
        vehicle_data = ordered_vehicle_list
    if price_order == 'ASC':
        ordered_vehicle_list = sorted(vehicle_data, key=lambda x: x['DailyRentPrice'], reverse=False)
        vehicle_data = ordered_vehicle_list
    if transmission_type != 'ALL':
        filtered_vehicle_list = [vehicle for vehicle in vehicle_data if vehicle['Transmission'] == transmission_type]
        vehicle_data = filtered_vehicle_list

    return vehicle_data