class Destination:
    def __init__(self, airport, phone_number, opening_times, location)  -> None:
        self.airport = airport
        self.phone_number = phone_number
        self.opening_times = opening_times
        self.location = location
    
    def __str__(self) -> str:
        return self.airport + self.phone_number + self.opening_times + self.location
