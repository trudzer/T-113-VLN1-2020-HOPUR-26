class Contract:
    def __init__(self, customerID, employeeID, total_amount, vehicleID, destinationID, date, time_period, experation_date, billID, is_valid):
        self.customerID = customerID
        self.employeeID = employeeID
        self.total_amount = total_amount
        self.vehicleID = vehicleID
        self.destinationID = destinationID
        self.date = date
        self.time_period = time_period
        self.experation_date = experation_date
        self.billID = billID
        self.is_valid = is_valid

    def __str__(self):
        return self.customerID + self.employeeID + self.total_amount + self.vehicleID + self. date + self.time_period + self.experation_date + self.billID + self.is_valid  