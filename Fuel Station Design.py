
class FuelStation:
    def __init__(self, diesel, petrol, electric):
        self.available_spots = {"diesel": diesel, "petrol": petrol, "electric": electric}

    def fuel_vehicle(self, fuel_type):
        if self.available_spots[fuel_type] > 0:
            self.available_spots[fuel_type] -= 1
            return True
        else:
            return False

    def open_fuel_slot(self, fuel_type):
        if self.available_spots[fuel_type] < self.get_total_spots(fuel_type):
            self.available_spots[fuel_type] += 1
            return True
        else:
            return False

    def get_total_spots(self, fuel_type):
        return self.available_spots[fuel_type]

fuel_station = FuelStation(diesel=2, petrol=2, electric=1)

print(fuel_station.fuel_vehicle("diesel")) 
print(fuel_station.fuel_vehicle("petrol")) 
print(fuel_station.fuel_vehicle("diesel")) 
print(fuel_station.fuel_vehicle("electric")) 
print(fuel_station.fuel_vehicle("diesel")) 

print(fuel_station.open_fuel_slot("diesel"))  
print(fuel_station.fuel_vehicle("diesel"))  
print(fuel_station.open_fuel_slot("electric"))  
print(fuel_station.open_fuel_slot("electric"))  
