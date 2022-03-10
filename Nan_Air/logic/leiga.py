from models.Contract import Contract 
from models.Vehicle import Vehicle
from models.Customer import Customer
from models.ErrorMessage import ErrorMessage
class LLContract:
    def __init__(self, data):
        self.data = data
    
    
    def TestContractList(self, ContractVarList):
        #hérna er eftir að koma test function fyrir contracts:
        customer = ContractVarList[1]
        customer = self.data.GetData([customer, 'customer'])
        vehicle = ContractVarList[4]
        vehicle = self.data.GetData([vehicle, 'vehicle'])
        if customer == None:
            return ErrorMessage(2222, "Customer doesn't exist",None)
        if vehicle[4] == 'B':
            if not(customer[6] != 'B' or 'C' or 'D'):
                return ErrorMessage(9595, "Customer does not have the license to operate this vehicle",None)
        if  vehicle[4] == 'C':
            if not(customer[6] != 'C' or 'D'):
                return ErrorMessage(9596, "Customer does not have the license to operate this vehicle",None)
        if vehicle[4] == 'D':
            if customer[6] != 'D':
                return ErrorMessage(95967, "Customer does not have the license to operate this vehicle",None)

        employee = ContractVarList[2]
        employee = self.data.GetData([employee, 'employee'])
        if employee == None:
            return ErrorMessage(3333, "Employee doesn't exist",None)

        amount = ContractVarList[3]
        try:
            if int(amount) <= 0:
                return ErrorMessage(9536,"amount is not a valid number",TypeError)
        except TypeError:
            return ErrorMessage(9537,"amount is not a valid number",TypeError)
        
        if vehicle == None:
            return ErrorMessage(4444, "vehicle doesn't exist",None)

        startDate = ContractVarList[5]
        check = self.check_date( startDate )
        if type(check) == ErrorMessage:
            return check
        
        EndDate = ContractVarList[6]
        check = self.check_date( EndDate )
        if type(check) == ErrorMessage:
            return check

        time_of_termination = ContractVarList[7]
        check = self.check_date( time_of_termination )
        if type(check) == ErrorMessage:
            return check
        
        chargedVar = ContractVarList[7]
        charged         = "Rukkaður"
        not_charged     = "Órukkaður"
        if chargedVar != charged or chargedVar != not_charged:
            ErrorMessage(7881, "ATH Leyfðir innslættir væru Rukkaður eða Órukkaður",None) 

        #bill = ContractVarList[7] #á ekki að vera user input
        #if bill != "None":
        #    bill = self.data.GetData(bill, 'bill')
        #    if bill == None:
        #        return ErrorMessage(5555, "Bill doesn't exist",None)

        is_location_real = self.data.GetData([ContractVarList[5], 'locations'])
        if is_location_real == None:
            return ErrorMessage(12579, "the location doesn't exist", None)

        is_valid = ContractVarList[8]        
        recieved        = "Já"
        not_recieved    = "Nei"
        if is_valid != recieved or is_valid != not_recieved:
            ErrorMessage(7891,"is_valid Leyfir innslætir væru Já, Nei eða Skil!", None)


    def check_date(self, dateVar):
        if len(dateVar) == 8:

                try:
                    series_of_integers = ""
                    count = 0
                    for i in dateVar:
                        series_of_integers += dateVar[count]
                        count += 1
                        series_of_integers += dateVar[count]
                        if count == 7:
                            break
                        count += 2
                    series_of_integers = int(series_of_integers)
                except TypeError:
                    return ErrorMessage(7871,"Dæmi um innslátt tímabils: XX-XX-XX þar sem X-in eru tölustafir",TypeError)

                if dateVar[2] != "-" or dateVar[5] != "-":
                    return ErrorMessage(7872,"Passa sig að ekki nota bil. Dæmi um innslátt tímabils: XX-XX-XX þar sem X-in eru tölustafir",None)

                
                if int(dateVar[3:5]) >= 13 or int(dateVar[3:5]) <= 0:
                    return ErrorMessage(7874,"Ath: Bara 12 mánuðir í hverju ári. Dæmi um innslátt tímabils: XX-XX-XX þar sem X-in eru tölustafir",None)

                elif int(dateVar[3:5]) == 2:
                    if int(dateVar[0:2]) <= 0 or int(dateVar[0:2]) >= 30:
                        return ErrorMessage(7873,"Aðeins 29 dagar í febrúar (PASSA SIG Á HLAUPÁRUM)", ValueError)

                elif dateVar[3:5] == 4 or dateVar[3:5] == 6 or dateVar[3:5] == 9 or dateVar[3:5] == 11:
                    if int(dateVar[0:2]) <= 0 or int(dateVar[0:2]) >= 31:
                        return ErrorMessage(7873,"Aðeins 29 dagar í febrúar (PASSA SIG Á HLAUPÁRUM)", ValueError)
                
                elif dateVar[3:5] == 1 or dateVar[3:5] == 3 or dateVar[3:5] == 5 or dateVar[3:5] == 7 or dateVar[3:5] == 8 or dateVar[3:5] == 10 or dateVar[3:5] == 12:
                    if int(dateVar[0:2]) <= 0 or int(dateVar[0:2]) >= 32 or int(dateVar[9:11]) <= 0 or int(dateVar[9:11]) >= 32:
                        return ErrorMessage(7873,"Aðeins 29 dagar í febrúar (PASSA SIG Á HLAUPÁRUM)", ValueError)

    def change_contract(self, ContractVarList, OGContractvar):
        '''tekur samning og lista af breytingum og sameinar þá með villimeldingum'''
        #þetta er contract sem er fyrir
        
        #byrjun á að sorta uplýsingar frá breitingum
        CustomerIDVar         = ContractVarList[1]
        employeeIDVar         = ContractVarList[2]
        total_amountVar       = ContractVarList[3]
        VehicleIDVar          = ContractVarList[4]
        dateVar               = ContractVarList[5]
        time_periodVar        = ContractVarList[6]
        expiration_dateVar    = ContractVarList[7]
        billIDVar             = ContractVarList[8]
        is_validVar           = ContractVarList[9]
        #skoða hverju var breit og hverju var ekki breitt
        NoC=None #No change

        if type(CustomerIDVar)           == NoC:
            CustomerIDVar                = OGContractvar[1]
        if type(employeeIDVar)           == NoC:
            employeeIDVar                = OGContractvar[2]
        if type(total_amountVar)         == NoC:
            total_amountVar              = OGContractvar[3]
        if type(VehicleIDVar)            == NoC:
            VehicleIDVar                 = OGContractvar[4]
        if type(dateVar)                 == NoC:
            dateVar                      = OGContractvar[5]
        if type(time_periodVar)          == NoC:
            time_periodVar               = OGContractvar[6]
        if type(expiration_dateVar)      == NoC:
            expiration_dateVar           = OGContractvar[7]
        if type(billIDVar)               == NoC:
            billIDVar                    = OGContractvar[8]
        if type(is_validVar)             == NoC:
            is_validVar                  = OGContractvar[9]
        #búatil nýtt Contract til að setja í staðinn
        #gera samkvæmt modelklasa
        NewContract = [ContractVarList[0],CustomerIDVar,employeeIDVar, total_amountVar,VehicleIDVar,dateVar,time_periodVar, expiration_dateVar,billIDVar,is_validVar]
        return NewContract


    def TestCustomerList(self, CustomerVarList):
        """tekur inn lista af variables sem á að fara í Employee klasa að klasa"""
        nameVar      = str(CustomerVarList[1])
        ktVar        = CustomerVarList[2]
        for i in ktVar:
            if not (i in "0123456789-"):
                return ErrorMessage(9034,'ssn numbers invalid ("0123456789-")',(ktVar,i))

        
        GSMVar       = str(CustomerVarList[3])
        for i in GSMVar:
            if not (i in "+0123456789-"):
                return ErrorMessage(9025,'GSM numbers invalid ("+0123456789-")',None)

        HomePhoneVar = CustomerVarList[4]
        for i in HomePhoneVar:
            if not (i in "+0123456789-"):
                return ErrorMessage(9025,'Home Phone numbers invalid ("+0123456789-")',None)
        
        addressVar   = str(CustomerVarList[5])
        EmailVar     = str(CustomerVarList[6])
        if "@" in EmailVar[1:]:
            if not("." in EmailVar[EmailVar.index("@")+1:]):
                return ErrorMessage(5536,"email invalid format(xxx@xxx.xx)",EmailVar)
        else:
            return ErrorMessage(5537,"email invalid format(xxx@xxx.xx)",EmailVar)


        
        LicenseVar   = CustomerVarList[7] 
        if not(LicenseVar.lower() in ["a","b","c","d"]):
            return ErrorMessage(5321,'License is not valid ("a","b","c","d")',TypeError)
        
        return [nameVar, ktVar, GSMVar, HomePhoneVar, addressVar, EmailVar, LicenseVar] #Employee(nameVar, ktVar, addressVar, EmailVar, GSMVar, HomePhoneVar,LocartionVar)
        

    
    def change_customer(self,CustomerVarList, OGCostumerVar):
        '''Tekur leigjanda og breytir honum'''


        nameVar            = CustomerVarList[1]
        ssnVar             = CustomerVarList[2]
        GSMVar             = CustomerVarList[3]
        phoneVar           = CustomerVarList[4]
        home_addressVar    = CustomerVarList[5]
        emailVar           = CustomerVarList[6]
        LicenseVar         = CustomerVarList[7]

        NoC=None #No change

        if type(nameVar)           == NoC:
            nameVar                = OGCostumerVar[1]
        if type(ssnVar)            == NoC:
            ssnVar                 = OGCostumerVar[2]
        if type(GSMVar)            == NoC:
            GSMVar                 = OGCostumerVar[3]
        if type(phoneVar)          == NoC:
            phoneVar               = OGCostumerVar[4]
        if type(home_addressVar)   == NoC:
            home_addressVar        = OGCostumerVar[5]
        if type(emailVar)          == NoC:
            emailVar               = OGCostumerVar[6]
        if type(LicenseVar)        == NoC:
            LicenseVar             = OGCostumerVar[7]
        
        NewCostumer = [CustomerVarList[0],nameVar, ssnVar, GSMVar, phoneVar, home_addressVar, emailVar, LicenseVar]
        return NewCostumer
        