from data.DataMain import DataMain
from logic.skyrsla import * #reikningur, prentvaent, dagsektir
from logic.leiga import LLContract
from logic.annad import * #afangastadur, afendingSkil, farataeki, starfsmen
from models.ErrorMessage import ErrorMessage

class LogicMash:
    def __init__(self):
        print("Inside logic Mash")
        self.Logic = LogicMain()
    
    def starfsmenn_read_list(self):
        return self.Logic.all_employees()
    
    def afangastadir_read_list(self):
        return self.Logic.all_destinations()

    def add_starfsmenn_results(self,starfsmadur_dict, id, nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning):
        employeeList=[id, nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning]
        if id in starfsmadur_dict:
            return self.Logic.change_employee(employeeList)
        return self.Logic.create_employee(employeeList)

    def eyda_element(self, the_class, id):
        if  the_class == "starfsmadur_dict":
            self.Logic.delete_employee(id)
        elif the_class == "afangastadir_dict":
            self.Logic.delete_location(id)
        elif the_class == "farartaeki_dict":
            self.Logic.delete_Vehicle(id)
        elif the_class == "leigjandi_dict":
            self.Logic.delete_customer(id)
        elif the_class == "leiga_dict":
            self.Logic.delete_contract(id)
        else:
            return ErrorMessage(3244,"class dose not exist",None)

    
    def add_afangastadir_results(self,afangastadir_dict, id, borg, land, flugvollur, simanumer, opnunartimi):
        DestinationList = [id, borg, land, flugvollur, simanumer, opnunartimi]
        if int(id) in afangastadir_dict.keys():
            return self.Logic.Change_Location(DestinationList)
        else:
            ret = self.Logic.create_location(DestinationList)
            if type(ret) == ErrorMessage:
                return ret
            return "None"

    def add_farartaeki_results(self,farartaeki_dict, id, nafn, numeraplata, fratekid, typa, stadsetning, vidhald, litur, argerd, taxi, km, gerd):
        vehicleInfoList=[id, nafn, numeraplata, fratekid, typa, stadsetning, vidhald, litur, argerd, taxi, km, gerd]
        if id in farartaeki_dict:
            return self.Logic.change_vehicle(vehicleInfoList)
        
        return self.Logic.create_vehicle(vehicleInfoList)
    
    def farartaeki_read_list(self):
        return self.Logic.all_vehicles()

    def leiga_read_list(self):
        return self.Logic.all_contracts()
    def leigjandi_read_list(self):
        return self.Logic.all_customers()

    def add_leiga_results(self,leiga_dict, id_samningur, id_leigjandi, id_starfsmadur, kostnadur, id_farartaeki,id_afangastadir, samningur_stofnadur, byrjun_samningur, endir_samningur, pickup_timi, rukkadur, motaka):
        contract=[id_samningur, id_leigjandi, id_starfsmadur, kostnadur, id_farartaeki, samningur_stofnadur, byrjun_samningur, endir_samningur, pickup_timi, rukkadur, motaka]
        if id in leiga_dict:
            return self.Logic.change_contract(contract)
        return self.Logic.create_contract(contract)

    def add_leigjandi_results(self,leigjandi_dict, id, nafn, kennitala,simanumer,heimilisfang,tolvupostur,typa):
        leigjandi=[id, nafn, kennitala,simanumer,heimilisfang,tolvupostur,typa]
        if id in leigjandi_dict:
            return self.Logic.change_customer(leigjandi)                                       
        return self.Logic.create_customer(leigjandi)


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
            id = int(i[0])
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
            id = int(i[0])
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
            id = int(i[0])
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
            id = int(i[0])
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
            id = int(i[0])
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
    
    def select_Vehicles(self, item, value):#ekki testað
        new_dict={}
        if item == "type":
            x=10
        else:
            ErrorMessage(3345,"not a valid item",None) 

        vehicles=self.all_vehicles() # nær í öll fara tæki
        for key in vehicles.keys():
            #bír til lista til að vinna með
            nafn, kennitala, simanumer, heimilisfang, email, time_period, pickup_time, reception, bill, license_plate, vehicle_type = vehicles[key]
            vehicle=[nafn, kennitala, simanumer, heimilisfang, email, time_period, pickup_time, reception, bill, license_plate, vehicle_type]
            if vehicle[x] == value: # flokkar fara tækið í nýtt dict
                new_dict[key]=vehicles[key]
        return new_dict

    def change_select_vehicles(self, item, value ,changelist):#ekki testa
        Vehicles = self.select_Vehicles( item, value) # fær áhveðið sett af faratækjum
        for key in Vehicles.keys():
            vehicleInfoList=[key]+changelist
            change = self.change_vehicle(vehicleInfoList) #breitri fara tækinu samhvæmt fyrir mælum

            if type(change) == ErrorMessage: #ef það kemur error þarf að backtrakka og setja gömlu uplýsingarnar inn í gagna grunnin
                for key in Vehicles.keys():
                    nafn, kennitala, simanumer, heimilisfang, email, time_period, pickup_time, reception, bill, license_plate, vehicle_type = Vehicles[key]
                    vehicle=[key,nafn, kennitala, simanumer, heimilisfang, email, time_period, pickup_time, reception, bill, license_plate, vehicle_type]
                    self.change_vehicle(vehicle)
                    return change
    
    def create_employee(self,employeeList):
        employee = self.Employee.TestEmployeeList(employeeList)
        if type(employee)== ErrorMessage: #gæti komið error við að búatil vehicle
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
        if type(vehicle)== ErrorMessage: #gæti komið error við að búatil vehicle
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
        OGVehicleVar = self.data.GetData([str(vehicleInfoList[0]),"vehicle"]) # nær í gamla faratækið með ID
        NoC="None"
        vehicleInfoList2=[]
        for i in vehicleInfoList[0:]: #fer yfir listan svo hann sé á réttu formati
            if i == NoC:
                i=None
            vehicleInfoList2.append(i) 

        NewVehicle = self.vehicle.changeVehicle(vehicleInfoList2,OGVehicleVar) 
        NewVehicleT = self.vehicle.TestVehicleList(NewVehicle)
        
        if type(NewVehicleT)== ErrorMessage: #gæti komið error við að testa
            Message = NewVehicleT
            return Message
        
        self.data.change_vehicle([vehicleInfoList[0],"vehicle"],NewVehicle)
    
    def change_employee(self,employeeInfoList):
        OGEmployeeVar = self.data.GetData([employeeInfoList[0], "employee"])
        NoC="None"
        employeeInfoList2=[]
        for i in employeeInfoList:
            if i == NoC:
                i=None
            employeeInfoList2.append(i)

        NewEmployee = self.Employee.changeEmployee(employeeInfoList2,OGEmployeeVar)
        NewEmployeeT = self.Employee.TestEmployeeList(NewEmployee)
        
        if type(NewEmployeeT)== ErrorMessage: #gæti komið error við að testa
            Message = NewEmployeeT
            return Message
        
        self.data.change_employee([employeeInfoList[0], "employee"],NewEmployee)

    def change_customer(self, customerVarList):
        OGCustomerVar = self.data.GetData([customerVarList[0], "customer"])
        NoC = "None"
        customerInfoList2 = []
        for i in customerVarList:
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
        for i in contractVarList:
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
        '''þetta function er notað til að eyða farartaeki '''
        self.data.delete_vehicle(VehicleID)
    

    def delete_contract(self, contractID):
        ''' þetta function er notað til að eyða samninga'''
        self.data.delete_contract(contractID)
    

    def delete_location(self, LocationID):
        '''þetta er notað til að eyða út destination'''
        self.data.delete_location(LocationID)
    

    def delete_customer(self, CustomerID):
        '''þetta er notað til að eyða út viðskiptavin'''
        self.data.delete_customer(CustomerID)
    
    def delete_employee(self, EmployeeID):
        '''þettar er notað til að eyða starfsmanni'''
        self.data.delete_employee(EmployeeID)
