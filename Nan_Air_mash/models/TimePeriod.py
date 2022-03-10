class TimePeriod:
    def __init__(self, starting_date, ending_date) -> None:
        self.starting_date = starting_date
        self.ending_date = ending_date

    def __str__(self) -> str:
        return self.starting_date + self.ending_date
