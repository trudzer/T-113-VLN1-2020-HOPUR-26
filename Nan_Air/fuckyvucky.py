    def create_contract(self, ContractVarList):
        ''' þetta er fyrir TUI að búa til nýtt contract'''
        CustomerIDVar         = ContractVarList[0]
        if self.data.GetData([CustomerIDVar, "customer"]) == None:
            ErrorMessage(7841,"Customer id ekki til", None)

        employeeIDVar         = ContractVarList[1]
        if self.data.GetData([employeeIDVar, "employee"]) == None:
            ErrorMessage(7842,"Employee id ekki til", None)        

        total_amountVar       = ContractVarList[2]       
        try:
            total_amountVar = int(total_amountVar)
        except TypeError:
            ErrorMessage(7851,"Upphæðin þarf að vera tala",TypeError)


        VehicleIDVar          = ContractVarList[3]  
        if self.data.GetData([VehicleIDVar, "vehicle"]) == None:
            ErrorMessage(7843,"Vehicle id ekki til", None) 

        dateVar               = ContractVarList[4]
        check=self.check_date(dateVar)
        if type(check) == ErrorMessage:
            return check
        
        time_periodVar        = ContractVarList[5]
        check=self.check_date(time_periodVar)
        if type(check) == ErrorMessage:
            return check

        expiration_dateVar    = ContractVarList[6]
        check=self.check_date(expiration_dateVar)
        if type(check) == ErrorMessage:
            return check

        chargedVar             = ContractVarList[7]
        charged         = "Rukkaður"
        not_charged     = "Órukkaður"
        if chargedVar != charged or chargedVar != not_charged:
            ErrorMessage(7881, "ATH Leyfðir innslættir væru Rukkaður eða Órukkaður",None) 

        recievedVar           = ContractVarList[8]        
        recieved        = "Já"
        not_recieved    = "Nei"
        returned        = "Skil"
        if recievedVar != recieved or recievedVar != not_recieved or recievedVar != returned:
            ErrorMessage(7891,"ATG Leyfðir innslætir væru Já, Nei eða Skil!", None)

       
        return Contract(CustomerIDVar,employeeIDVar,total_amountVar, VehicleIDVar, dateVar, time_periodVar, expiration_dateVar, chargedVar, recievedVar)

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

        else:
            return ErrorMessage(7875,"Dæmi um innslátt tímabils: XX-XX-XX þar sem X-in eru tölustafir",None)
