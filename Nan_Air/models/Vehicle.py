class Vehicle:
    def __init__(self, id, model, licence_plate, is_rented, vehicle_catagory, location, condition, color, year_model, tax, km_driven, vehicle_type) -> None:
        self.id = id
        self.model = model
        self.licence_plate = licence_plate
        self.vehicle_catagory = vehicle_catagory
        self.is_rented = is_rented 
        self.location = location
        self.condition = condition
        self.color = color
        self.year_model = year_model
        self.tax = tax
        self.km_driven = km_driven
        self.vehicle_type = vehicle_type
    
    def __str__(self) -> str:
        return str(self.model) + str(self.licence_plate) + str(self.is_rented) + str(self.vehicle_catagory) + str(self.location) + str(self.condition) + str(self.color) + str(self.year_model) + str(self.tax) + str(self.km_driven)