
class Flights:
    def __init__(self, departure, destination, time_period):
        self.departure = departure
        self.destination = destination
        self.time_period = time_period

    def __str__(self):

        return self.departure + self.destination + self.time_period
