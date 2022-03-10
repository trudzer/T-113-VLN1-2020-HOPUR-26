
class Employee:
    def __init__(self, name, ssn, address, email, mobilephone, phone, loaction):
        self.name = name
        self.ssn = ssn
        self.address = address
        self.email = email
        self.mobilephone = mobilephone
        self.phone = phone
        self.location = loaction
    
    
    def __str__(self):
        return self.name + self.ssn + self.address + self.email + self.mobilephone + self.phone + self.location