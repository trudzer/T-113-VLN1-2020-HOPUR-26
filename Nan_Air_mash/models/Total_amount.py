
class Total_amount:
    def __init__(self, amount, tax_rate):

        self.amount = amount
        self.tax_rate = tax_rate

    def __str__(self):
        return self.amount + self.tax_rate

