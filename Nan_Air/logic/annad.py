from models.ErrorMessage import ErrorMessage
from models.Vehicle import Vehicle
class destination:
    def __init__(self, data):
        self.data = data
    
    def TestDestinationList(self, DestinationVar):
        '''fer yfir allar breitur í lista svo hann sé eins og hann á að vera'''
        for num in DestinationVar[4]:
            if not(num.lower() in ['1','2','3','4','5','6','7','8','9','0','-','+']):
                return ErrorMessage(6660, 'Please add a valid phone number',None)
        
        for num in DestinationVar[5]:
            if not(num.lower() in ['1','2','3','4','5','6','7','8','9','0',':','+','-']):
                return ErrorMessage(6661, 'Departure and Arrival time ate incorrect, please insert a valid time with only integers and ":" and "-"',None)
        
        locationVar     = str(DestinationVar[1])
        if not(locationVar.lower() in ["reykjavík","nuuk","kulusuk","tingwall","longyearbyen","þórshöfn"]):
            return ErrorMessage(8765,'location is not valid ("Reykjavík","Nuuk","Kulusuk","Tingwall","Longyearbyen","Þórshöfn")',TypeError)
    
    def changeLocation(self, LocationVarList, OGLocationVar):
        """tekur faratæki og lista af bretingum og saameinar með villimeldingum"""
        #þetta er faratækið sem er fyrir
        
        #byrjun á að sorta uplýsingar frá breitingum
        IDVar               = LocationVarList[0]
        locationVar         = LocationVarList[1]
        countryVar          = LocationVarList[2]
        airportVar          = LocationVarList[3]
        phoneVar            = LocationVarList[4]
        opening_timesVar    = LocationVarList[5]
        
        #skoða hverju var breit og hverju var ekki breitt
        NoC=type(None) #No change
        
        if type(IDVar)               == NoC:
            IDVar                    = OGLocationVar[0]
        if type(locationVar)         == NoC:
            locationVar              = OGLocationVar[1]
        if type(countryVar)          == NoC:
            countryVar               = OGLocationVar[2]
        if type(airportVar)          == NoC:
            airportVar               = OGLocationVar[3]
        if type(phoneVar)            == NoC:
            phoneVar                 = OGLocationVar[4]
        if type(opening_timesVar)    == NoC:
            opening_timesVar         = OGLocationVar[5]
        
        #búatil nýtt fara tæki til að setja í staðinn
        NewLocation = [IDVar, locationVar, countryVar, airportVar,phoneVar ,opening_timesVar]
        return NewLocation #annað hvort Vehicle eða ErrorMsg

class LLVehicle:
    def __init__(self, data):
        self.data = data

    def TestVehicleList(self, VehicleVarList):
        """fer yfir allar breitur í lista svo hann sé eins og hann á að vera"""
        nameVar         = str(VehicleVarList[1])

        licence_plateVar= str(VehicleVarList[2])
        if "-" in licence_plateVar:
            if len(licence_plateVar)==6:
                if not(licence_plateVar[2] == "-"):
                    return ErrorMessage(7653,'licence plate hyphen is not a valid (XX-XXX)',licence_plateVar)
            else:
                return ErrorMessage(7654,'licence plate invalid number of charecters(XX-XXX)',licence_plateVar)
        else:
            if not(len(licence_plateVar)==5):
                return ErrorMessage(7655,'licence plate invalid number of charecters(XX-XXX)',licence_plateVar)
            licence_plateVar=licence_plateVar[:2]+"-"+licence_plateVar[2:]


        isRentedVar     = str(VehicleVarList[3])
        if not(isRentedVar.lower() in ["já","nei","0","1"]):
            return ErrorMessage(7890,'is Rented is not a valid boolean ("já","nei","0","1")',TypeError)

        categoriesVar   = VehicleVarList[4]
        if not(categoriesVar.lower() in ["a","b","c","d"]):
            return ErrorMessage(4321,'categories is not valid ("a","b","c","d")',TypeError)

        destinations = self.data.get_all_destinations()
        destinationList=[]
        for key in destinations.keys():
            destinationList.append(destinations[key][1].lower())

        locationVar     = str(VehicleVarList[5])
        if not(locationVar.lower() in destinationList): #
            return ErrorMessage(8765,'location is not valid '+str(destinationList),TypeError)

        conditionVar    = str(VehicleVarList[6])
        if not(conditionVar.lower() in ["í lagi","bilað","1","0"]):
            return ErrorMessage(9876,'condition is not valid ("Í lagi","Bilað","1","0")',TypeError)

        colorVar        = str(VehicleVarList[7])

        try:
            yearModelVar  = int(VehicleVarList[8])
        except TypeError:
            return ErrorMessage(1234,"Year model is not a valid number",TypeError)
        taxVar          = str(VehicleVarList[9])
        
        
        try:
            taxVarint= int(taxVar)
        except TypeError:
            return ErrorMessage(3243,"tax is not a valid number",TypeError)
        if 0>taxVarint>50:
            return ErrorMessage(3244,"tax is not a valid number",TypeError)#MSG þarfa að breita

        try:
            km_drivenVar    = int(VehicleVarList[10])
        except TypeError:
            return ErrorMessage(5678,"km driven is not a valid number",TypeError)

        typeVar     = str(VehicleVarList[11])
        if not(typeVar.lower() in ["Fólksbíll","Jeppi","Mótorhjól","Trukkur","Seglbátur","Snekkja","Spíttbátur"]): #
            return ErrorMessage(8765,'type is not valid ("Fólksbíll","Jeppi","Mótorhjól","Trukkur","Seglbátur","Snekkja","Spíttbátur")',TypeError)

        #VehicleVar = Vehicle(nameVar,licence_plateVar, isRentedVar,categoriesVar,locationVar,conditionVar, colorVar, yearModelVar, taxVar,km_drivenVar)
        VehicleVar= [nameVar,licence_plateVar, isRentedVar,categoriesVar,locationVar,conditionVar, colorVar, yearModelVar, taxVar,km_drivenVar, typeVar]
        VehicleVarStr=[]
        for i in VehicleVar:
            VehicleVarStr.append(str(i))
        return VehicleVarStr

        
    def changeVehicle(self, VehicleVarList, OGVehicleVar):
        """tekur faratæki og lista af bretingum og saameinar með villimeldingum"""
        #þetta er faratækið sem er fyrir
        
        #byrjun á að sorta uplýsingar frá breitingum
        nameVar         = VehicleVarList[1]
        licence_plateVar= VehicleVarList[2]
        isRentedVar     = VehicleVarList[3]
        
        if isRentedVar.lower() == "já":
            if (OGVehicleVar[3]).lower() == "já":
                return ErrorMessage(2345,"Vehicle is all reddy rented out",OGVehicleVar[3])
            if (OGVehicleVar[6]).lower() == "bilað":
                return ErrorMessage(3456,"Vehicle can not be rented out due to its condision",OGVehicleVar[6])

        categoriesVar   = VehicleVarList[4]
        locationVar     = VehicleVarList[5]
        conditionVar    = VehicleVarList[6]
        colorVar        = VehicleVarList[7]
        yearModelVar    = VehicleVarList[8]
        taxVar          = VehicleVarList[9]
        km_drivenVar    = VehicleVarList[10]
        vehicle_typeVar = VehicleVarList[11]
        
        #skoða hverju var breit og hverju var ekki breitt
        NoC=type(None) #No change
        
        if type(nameVar)         == NoC:
            nameVar              = OGVehicleVar[1]
        if type(licence_plateVar)== NoC:
            licence_plateVar     = OGVehicleVar[2]
        if type(isRentedVar)     == NoC:
            isRentedVar          = OGVehicleVar[3]
        if type(categoriesVar)   == NoC:
            categoriesVar        = OGVehicleVar[4]
        if type(locationVar)     == NoC:
            locationVar          = OGVehicleVar[5]
        if type(conditionVar)    == NoC:
            conditionVar         = OGVehicleVar[6]
        if type(colorVar)        == NoC:
            colorVar             = OGVehicleVar[7]
        if type(yearModelVar)    == NoC:
            yearModelVar         = OGVehicleVar[8]
        if type(taxVar)          == NoC:
            taxVar               = OGVehicleVar[9]
        if type(km_drivenVar)    == NoC:
            km_drivenVar         = OGVehicleVar[10]
        if type(vehicle_typeVar) == NoC:
            vehicle_typeVar      == OGVehicleVar[11]
        
        #búatil nýtt fara tæki til að setja í staðinn
        NewVehicle = [VehicleVarList[0],nameVar,licence_plateVar, isRentedVar,categoriesVar,locationVar,conditionVar, colorVar, yearModelVar, taxVar, km_drivenVar, vehicle_typeVar]
        return NewVehicle #annað hvort Vehicle eða ErrorMsg
        
from models.Employee import Employee
            
class LLEmployee:
    def __init__(self, data):
        self.data = data
    

 
    def TestEmployeeList(self, EmployeeVarList):
        """tekur inn lista af variables sem á að fara í Employee klasa að klasa"""
        nameVar      = str(EmployeeVarList[1])
        ktVar        = EmployeeVarList[2]
        for i in ktVar:
            if not (i in "0123456789-"):
                return ErrorMessage(8034,'ssn numbers invalid ("0123456789-")',(ktVar,i))

        addressVar   = str(EmployeeVarList[3])
        
        EmailVar     = str(EmployeeVarList[4])
        if "@" in EmailVar[1:]:
            if not("." in EmailVar[EmailVar.index("@")+1:]):
                return ErrorMessage(4536,"email invalid format(xxx@xxx.xx)",EmailVar)
        else:
            return ErrorMessage(4537,"email invalid format(xxx@xxx.xx)",EmailVar)

        GSMVar       = str(EmployeeVarList[5])
        for i in GSMVar:
            if not (i in "+0123456789-"):
                return ErrorMessage(8025,'GSM numbers invalid ("+0123456789-")',None)

        HomePhoneVar = EmployeeVarList[6]
        for i in HomePhoneVar:
            if not (i in "+0123456789-"):
                return ErrorMessage(8025,'Home Phone numbers invalid ("+0123456789-")',None)
        
        LocartionVar = EmployeeVarList[7]
        if not(LocartionVar.lower() in ["reykjavík","nuuk","kulusuk","tingwall","longyearbyen","þórshöfn"]):
            return ErrorMessage(8775,'location is not valid ("Reykjavík","Nuuk","Kulusuk","Tingwall","Longyearbyen","Þórshöfn")',TypeError)

        
        return [nameVar, ktVar, addressVar, EmailVar, GSMVar, HomePhoneVar,LocartionVar] #Employee(nameVar, ktVar, addressVar, EmailVar, GSMVar, HomePhoneVar,LocartionVar)
        

    def changeEmployee(self, EmployeeVarList, OGEmployeeVar):
        """tekur faratæki og lista af bretingum og saameinar með villimeldingum"""
        #þetta er faratækið sem er fyrir
        
        #byrjun á að sorta uplýsingar frá breitingum
        nameVar      = EmployeeVarList[1]
        ktVar        = EmployeeVarList[2]
        addressVar   = EmployeeVarList[3]
        EmailVar     = EmployeeVarList[4]
        GSMVar       = EmployeeVarList[5]
        HomePhoneVar = EmployeeVarList[6]
        LocationVar  = EmployeeVarList[7]
        
        #skoða hverju var breit og hverju var ekki breitt
        NoC=type(None) #No change

        if type(nameVar)      == NoC:
            nameVar           = OGEmployeeVar[1]
        if type(ktVar)        == NoC:
            ktVar             = OGEmployeeVar[2]
        if type(addressVar)   == NoC:
            addressVar        = OGEmployeeVar[3]
        if type(EmailVar)     == NoC:
            EmailVar          = OGEmployeeVar[4]
        if type(GSMVar)       == NoC:
            GSMVar            = OGEmployeeVar[5]
        if type(HomePhoneVar) == NoC:
            HomePhoneVar      = OGEmployeeVar[6]
        if type(LocationVar)  == NoC:
            LocationVar       = OGEmployeeVar[7]

        #búatil nýtt fara tæki til að setja í staðinn
        NewEmployee = [EmployeeVarList[0],nameVar, ktVar, addressVar, EmailVar, GSMVar, HomePhoneVar, LocationVar]
        return NewEmployee
        