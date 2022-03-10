class ID:
    def __init__(self, ID_number, ID_type) -> None:
        self.ID_number = ID_number
        self.ID_type = ID_type

    def __str__(self) -> str:
        return self.ID_number + self.ID_type