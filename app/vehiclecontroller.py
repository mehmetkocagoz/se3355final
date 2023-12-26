# Controller will interact with model which is vehicle
from app.vehicle import getAllVehicles
import base64


def getAll():
    vehicle_list = getAllVehicles()
    
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

    
