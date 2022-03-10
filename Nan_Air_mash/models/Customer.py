class Customer:
    def __init__(self, name, ssn, GSM, phone, home_address, email, License) -> None:
        self.name = name
        self.ssn = ssn
        self.phone = phone
        self.GSM = GSM
        self.home_address = home_address
        self.email = email
        self.License = License
    
    def __str__(self) -> str:
        return self.name + self.GSM + self.home_address + self.email + self.License


