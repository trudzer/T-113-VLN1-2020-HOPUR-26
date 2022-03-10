class Bill:
    def __init__(self, contractID, tax_rate, payed, fines, interest):
        self.contractID = contractID
        self.tax_rate = tax_rate
        self.payed = payed
        self.fines = fines
        self.interest = interest


    def __str__(self):

        return self.contractID + self.tax_rate + self.payed + self.fines + self.interest


# to be added to when it  gets used -Logi B
