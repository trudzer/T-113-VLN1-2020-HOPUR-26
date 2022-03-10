from models.ErrorMessage import ErrorMessage

class Bill:
    def __init__(self,data):
        self.data = data

    def create_bill(self, contract_list):
        original_amount = int(contract_list[3])
        car_list = self.data.GetData([contract_list[4],'vehicle'])
        car_tax = int(car_list[9])
        car_tax = car_tax/100 + 1
        final_amount = original_amount * car_tax
        return final_amount


class Printing:
    def __init__(self,data):
        self.data = data 

    def ContractToPrintebleList(self, ContractID):
        contract = self.data.GetData(ContractID)
        if contract == None:
            return ErrorMessage(9898,"contract doesn't exist",None)
        
        customerID = contract[1]
        customer = self.data.GetData([customerID,"customer"])
        
        employeeID = contract[2]
        employee = self.data.GetData([employeeID,"employee"])

        total_amount = contract[3]

        vehicleID = contract[4]
        vehicle = self.data.GetData([vehicleID,"vehicle"])

        date = contract[5]
        time_period = contract[6]
        experation_date = contract[7]
        bill = contract[8]
        
        #billID = contract[8]
        #if billID == "None" or billID == "":
        #    bill = "Eingin reikningur til/gerður"
        #else:
        #    bill = self.data.GetData([billID ,"bill"])

        is_valid = contract[9]

        return [ContractID,customer,employee,total_amount,vehicle,date,time_period,experation_date,bill,is_valid]
    

class Late_fees:
    def __init__(self,data):
        self.data = data

    def late_days_fee(self, days, bill, ContractList):
        bill = int(bill)
        days = int(days)
        car_list = self.data.GetData([ContractList[4],'vehicle'])
        car_tax = int(car_list[9])
        vehicle_tax = car_tax/100 + 1
        fine = (days * (bill * vehicle_tax)) * 1.2
        return fine
