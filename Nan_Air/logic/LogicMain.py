from data.DataMain import DataMain
from logic.skyrsla import * #reikningur, prentvaent, dagsektir
from logic.leiga import LLContract
from logic.annad import * #afangastadur, afendingSkil, farataeki, starfsmen
from models.ErrorMessage import ErrorMessage

class LogicMain:
    def __init__(self):
        print("Inside logic")
        self.data = DataMain()
        self.leiga = LLContract(self.data)
        self.vehicle = LLVehicle(self.data)
        Vehicle(None,None,None,None,None,None,None,None,None,None,None,None)
        self.destination = destination(self.data)
        self.Employee = LLEmployee(self.data)
        Employee(None,None,None,None,None,None,None)
        self.Bill = Bill(self.data)
        self.Printing = Printing(self.data)
        self.Late_fees = Late_fees(self.data)

    def all_employees(self):
        data_dict = {}
        file_stream = self.data.get_all_employees()
        for i in file_stream:
            i = i.split(",")
            id = i[0]
            nafn = i[1]
            kennitala = i[2]
            heimilisfang = i[3] 
            tolvupostur = i[4] 
            simanumer = i[5]
            heimilissimi = i[6]
            stadsetning = i[7]
            if id in data_dict:
                data_dict[id] = nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning
            else:
                data_dict[id] = nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning
        return data_dict
    
    def all_customers(self):
        data_dict = {}
        file_stream = self.data.get_all_customers()
        for i in file_stream:
            i = i.split(",")
            id = i[0]
            nafn = i[1]
            kennitala = i[2]
            simanumer = i[3] 
            heimilisfang = i[4] 
            email = i[5]
            certification = i[6]
            if id in data_dict:
                data_dict[id] = nafn, kennitala, simanumer, heimilisfang, email, certification
            else:
                data_dict[id] = nafn, kennitala, simanumer, heimilisfang, email, certification
        return data_dict

    def all_vehicles(self):
        data_dict = {}
        file_stream = self.data.get_all_vehicle()
        for i in file_stream:
            i = i.split(",")
            id = i[0]
            model = i[1]
            licence_plate = i[2]
            vehicle_catagory = i[3] 
            is_rented = i[4] 
            location = i[5]
            condition = i[6]
            color = i[7]
            year_model = i[8]
            tax = i[9]
            km_driven = i[10]
            vehicle_type = i[11]
            if id in data_dict:
                data_dict[id] = model, licence_plate, vehicle_catagory, is_rented, location, condition, color, year_model, tax, km_driven, vehicle_type
            else:
                data_dict[id] = model, licence_plate, vehicle_catagory, is_rented, location, condition, color, year_model, tax, km_driven, vehicle_type
        return data_dict
    
    def all_destinations(self):
        data_dict = {}
        file_stream = self.data.get_all_destinations()
        for i in file_stream:
            i = i.split(",")
            id = i[0]
            location = i[1]
            country = i[2]
            airport = i[3] 
            phone_number = i[4] 
            departure_arrival = i[5]
            
            if id in data_dict:
                data_dict[id] = location, country, airport, phone_number, departure_arrival
            else:
                data_dict[id] = location, country, airport, phone_number, departure_arrival
        return data_dict
    
    def all_contracts(self):
        data_dict = {}
        file_stream = self.data.get_all_contracts()
        for i in file_stream:
            i = i.split(",")
            id = i[0]
            customerID = i[1]
            employeeID = i[2]
            amount = i[3] 
            vehicleID = i[4] 
            LocationID = i[5]
            date_made = i[6]
            date_started = i[7]
            date_ended = i[8]
            expiration_time = i[9]
            has_paid = i[10]
            returned = i[11]
            if id in data_dict:
                data_dict[id] = customerID, employeeID, amount, vehicleID, LocationID, date_made, date_started, date_ended, expiration_time, has_paid, returned
            else:
                data_dict[id] = customerID, employeeID, amount, vehicleID, LocationID, date_made, date_started, date_ended, expiration_time, has_paid, returned
        return data_dict
    
    def select_Vehicles(self, item, value):#ekki testa??
        new_dict={}
        if item == "type":
            x=10
        else:
            ErrorMessage(3345,"not a valid item",None) 

        vehicles=self.all_vehicles() # n??r ?? ??ll fara t??ki
        for key in vehicles.keys():
            #b??r til lista til a?? vinna me??
            nafn, kennitala, simanumer, heimilisfang, email, time_period, pickup_time, reception, bill, license_plate, vehicle_type = vehicles[key]
            vehicle=[nafn, kennitala, simanumer, heimilisfang, email, time_period, pickup_time, reception, bill, license_plate, vehicle_type]
            if vehicle[x] == value: # flokkar fara t??ki?? ?? n??tt dict
                new_dict[key]=vehicles[key]
        return new_dict

    def change_select_vehicles(self, item, value ,changelist):#ekki testa
        Vehicles = self.select_Vehicles( item, value) # f??r ??hve??i?? sett af farat??kjum
        for key in Vehicles.keys():
            vehicleInfoList=[key]+changelist
            change = self.change_vehicle(vehicleInfoList) #breitri fara t??kinu samhv??mt fyrir m??lum

            if type(change) == ErrorMessage: #ef ??a?? kemur error ??arf a?? backtrakka og setja g??mlu upl??singarnar inn ?? gagna grunnin
                for key in Vehicles.keys():
                    nafn, kennitala, simanumer, heimilisfang, email, time_period, pickup_time, reception, bill, license_plate, vehicle_type = Vehicles[key]
                    vehicle=[key,nafn, kennitala, simanumer, heimilisfang, email, time_period, pickup_time, reception, bill, license_plate, vehicle_type]
                    self.change_vehicle(vehicle)
                    return change
    
    def create_employee(self,employeeList):
        employee = self.Employee.TestEmployeeList(employeeList)
        if type(employee)== ErrorMessage: #g??ti komi?? error vi?? a?? b??atil vehicle
            Message = employee
            return Message
        
        self.data.add_employee(employee)
    


    def create_contract(self, contract):
        Contract = self.leiga.TestContractList(contract)
        if type(Contract) == ErrorMessage:
            Message = Contract
            return Message
        self.data.add_contract(contract)

    def create_vehicle(self,vehicleInfoList):
        vehicle = self.vehicle.TestVehicleList(vehicleInfoList)
        if type(vehicle)== ErrorMessage: #g??ti komi?? error vi?? a?? b??atil vehicle
            Message = vehicle
            return Message
        self.data.add_vehicle(vehicle)
    
    
    def create_location(self, DestinationList):
        Destination = self.destination.TestDestinationList(DestinationList)
        if type(Destination) == ErrorMessage:
            Error = Destination
            return Error
        else:
            self.data.add_destination(DestinationList)
    
    def create_customer(self, CustomerVarList):
        customer = self.leiga.TestCustomerList(CustomerVarList)
        if type(customer) == ErrorMessage:
            Error = customer
            return Error
        self.data.add_customer(CustomerVarList)

    def Get_Destination(self, destinationID):
        return self.data.GetData(destinationID)
    
    def Get_Customer(self, customerID):
        return self.data.GetData(customerID)
    
    def Get_Employee(self, employeeID):
        return self.data.GetData(employeeID)
    
    def Get_Contract(self, contractID):
        return self.data.GetData(contractID)
    
    def Get_Vehicle(self, vehicleID):
        return self.data.GetData(vehicleID)

    def Change_Location(self, DestinationList):
        OGLocation = self.data.GetData([DestinationList[0], "locations"])
        NoC = 'None'
        DestinationList2 = []
        for i in DestinationList[0:]:
            if i == NoC:
                i = None
            DestinationList2.append(i)
        
        NewLocation = self.destination.changeLocation(DestinationList2, OGLocation)
        NewLocationT = self.destination.TestDestinationList(NewLocation)

        if type(NewLocationT) == ErrorMessage:
            Error = NewLocationT
            return Error
        
        self.data.change_location([DestinationList[0], "locations"], NewLocation)
    
    def change_vehicle(self,vehicleInfoList):
        OGVehicleVar = self.data.GetData([vehicleInfoList[0],"vehicle"]) # n??r ?? gamla farat??ki?? me?? ID
        NoC="None"
        vehicleInfoList2=[]
        for i in vehicleInfoList[1:]: #fer yfir listan svo hann s?? ?? r??ttu formati
            if i == NoC:
                i=None
            vehicleInfoList2.append(i) 

        NewVehicle = self.vehicle.changeVehicle(vehicleInfoList2,OGVehicleVar) 
        NewVehicleT = self.vehicle.TestVehicleList(NewVehicle)
        
        if type(NewVehicleT)== ErrorMessage: #g??ti komi?? error vi?? a?? testa
            Message = NewVehicleT
            return Message
        
        self.data.change_vehicle([vehicleInfoList[0],"vehicle"],NewVehicle)
    
    def change_employee(self,employeeInfoList):
        OGEmployeeVar = self.data.GetData([employeeInfoList[0], "employee"])
        NoC="None"
        employeeInfoList2=[]
        for i in employeeInfoList[1:]:
            if i == NoC:
                i=None
            employeeInfoList2.append(i)

        NewEmployee = self.Employee.changeEmployee(employeeInfoList2,OGEmployeeVar)
        NewEmployeeT = self.Employee.TestEmployeeList(NewEmployee)
        
        if type(NewEmployeeT)== ErrorMessage: #g??ti komi?? error vi?? a?? testa
            Message = NewEmployeeT
            return Message
        
        self.data.change_employee([employeeInfoList[0], "employee"],NewEmployee)

    def change_customer(self, customerVarList):
        OGCustomerVar = self.data.GetData([customerVarList[0], "customer"])
        NoC = "None"
        customerInfoList2 = []
        for i in customerVarList[0:]:
            if i == NoC:
                i = None
            customerInfoList2.append(i)
        NewCustomer = self.leiga.change_customer(customerInfoList2, OGCustomerVar)
        NewCustomerT = self.leiga.TestCustomerList(NewCustomer)
    
        if type(NewCustomerT) == ErrorMessage:
            Error = NewCustomerT
            return Error
        
        self.data.change_customer([customerVarList[0], "customer"], NewCustomer)

    def change_contract(self, contractVarList):
        OGContractVar = self.data.GetData([contractVarList[0], "contract"])
        NoC = "None"
        ContractInfoList2 = []
        for i in contractVarList[0:]:
            if i == NoC:
                i = None
            ContractInfoList2.append(i)
        NewContract = self.leiga.change_contract(ContractInfoList2, OGContractVar)
        NewContractT = self.leiga.TestContractList(NewContract)


        if type(NewContractT) == ErrorMessage:
            Error = NewContractT
            return Error
        
        self.data.change_contract([contractVarList[0], "contract"], NewContract)

    def delete_Vehicle(self, VehicleID):
        '''??etta function er nota?? til a?? ey??a farartaeki '''
        self.data.delete_vehicle(VehicleID)
    

    def delete_contract(self, contractID):
        ''' ??etta function er nota?? til a?? ey??a samninga'''
        self.data.delete_contract(contractID)
    

    def delete_location(self, LocationID):
        '''??etta er nota?? til a?? ey??a ??t destination'''
        self.data.delete_location(LocationID)
    

    def delete_customer(self, CustomerID):
        '''??etta er nota?? til a?? ey??a ??t vi??skiptavin'''
        self.data.delete_customer(CustomerID)
    
    def delete_employee(self, EmployeeID):
        '''??ettar er nota?? til a?? ey??a starfsmanni'''
        self.data.delete_employee(EmployeeID)
