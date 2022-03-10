from datetime import date, datetime
from logic.LogicMain import *


class UIMain():

    def __init__(self,start):
        self.logic = LogicMash()
        if start:
            self.ui_loop()

    def clear(self):
        print("\n" * 150)

    def print_starfsmenn_list(self,result_dict):
        self.result_dict = result_dict
        sorted_list = sorted(result_dict)
        print("| id: \t| nafn: \t\t\t| kennitala:\t| heimilisfang:\t\t| tölvupóstur:\t\t\t| símanúmer:\t\t| heimilissími:\t\t| staðsetning:\t\t\t|")
        print("|" + "—" * 191 +"|")
        for id in sorted_list:
            print("| {} \t| {:<22}\t| {:<12}\t| {:<20}\t| {:<22}\t| {:<14}\t| {:<14}\t| {:<16} \t\t|".format(id, result_dict[id][0], result_dict[id][1], result_dict[id][2], result_dict[id][3], result_dict[id][4], result_dict[id][5],result_dict[id][6]))


    def print_afangastadir_list(self,result_dict):
        self.result_dict = result_dict
        sorted_list = sorted(result_dict)
        print("| id: \t| borg: \t| land:\t\t\t| flugvöllur:\t\t\t| símanúmer:\t\t\t| opnunartími:\t\t\t\t\t\t\t\t\t|")
        print("|" + "—" * 191 +"|")
        for id in sorted_list:
            print("| {} \t| {:<8}\t| {:<20}\t| {:<28}\t| {:<22}\t| {:<14}\t|\t\t\t\t\t\t\t|".format(id, result_dict[id][0], result_dict[id][1], result_dict[id][2], result_dict[id][3], result_dict[id][4]))

    def print_farartaeki_list(self,result_dict):
        self.result_dict = result_dict
        sorted_list = sorted(result_dict)
        print("| id: \t| módel: \t\t\t\t| númeraplata:\t| frátekið:\t| týpa:\t| staðsetning:\t| viðhald:\t| litur:\t\t| árgerð:\t| taxi:\t| km:\t\t| bíla týpa: \t\t|")
        print("|" + "—" * 207 +"|")
        for id in sorted_list:
            print("| {} \t| {:<32}\t| {:4}\t| {:<8}\t| {:<2}\t| {:<10}\t| {:<8}\t| {:<14}\t| {:<6}\t| {:<4}%\t| {:<6} KM\t|{:<10}\t\t|".format(id, result_dict[id][0], result_dict[id][1], result_dict[id][2], result_dict[id][3], result_dict[id][4],result_dict[id][5],result_dict[id][6],result_dict[id][7],result_dict[id][8],result_dict[id][9],result_dict[id][10]))


    def print_leiga_list(self,result_dict, other_dict):
        self.result_dict = result_dict
        self.other_dict = other_dict
        sorted_list = sorted(result_dict)
        print("| id: \t| nafn: \t\t\t| kennitala:\t| símanúmer:\t\t| heimilisfang:\t\t| tölvupóstur:\t\t\t| byrjun leigu:\t| endir leigu:\t| sækja:| mótekin:\t|")
        print("|" + "—" * 191 +"|")
        for id in sorted_list:
            print("| {} \t| {:<22}\t| {:4}\t| {:<14}\t| {:<16}\t| {:<28}\t| {:<8}\t| {:<6}\t| {:<3}\t| {:<3}\t\t|".format(id, result_dict[id][0], result_dict[id][1], result_dict[id][2], result_dict[id][3], result_dict[id][4],other_dict[id][6],other_dict[id][7],other_dict[id][8],other_dict[id][10]))
    
    def multi_select(self,values_list,name):
        print_list=[str(i+1)+". "+values_list[i] for i in range(len(values_list))]
        printing="\n".join(print_list)
        print("—" * 25)
        print(printing)
        print("—" * 25)
        try:
            type_input = int(input(name+": "))
            return values_list[type_input-1]
        except IndexError:
            return ErrorMessage(1021,"invalid input",type_input)
        except TypeError:
            return ErrorMessage(1022,"invalid input",type_input)
    
    def stadsetning_select(self):
        print("—" * 25)
        counter = 0
        afangastadir_dict=self.logic.afangastadir_read_list()#VG
        for i in afangastadir_dict:
            counter += 1
            print(counter, "-", afangastadir_dict[i][0])
            
        print("—" * 25)
        try:
            input_list=input("{:<16}|".format("Staðsetning:")) #býr til basic info 
        
        except ValueError:
            return ErrorMessage(1031,"invalid input",None)
            
        counter = 0
        for i in afangastadir_dict:
            counter += 1
            if int(input_list) == counter:
                stadsetning = afangastadir_dict[i][0]
                return stadsetning
        return ErrorMessage(1032,"invalid input",None)
    
    def error_print(self,ErrorMessage):
        pass
    
    def make_info(self,class_dict,needed_info_list):
        """tekur alt nema id og breitir í spurninga lista"""
        info_list=[]
        id = int(input("id: "))
        if id not in class_dict:
            info_list=[id]
            for item in needed_info_list:
                if item == "Staðsetning":
                    new_info=self.stadsetning_select()
                elif type(item) == tuple:
                    new_info=self.multi_select(item[1],item[0])#VG
                elif type(item) == list: #til að fá kl þá [[["08:00","09:00","10:00","11:00"],["20:00","21:00","22:00","23:00"]],"-"]
                    try:
                        error=(False,"error")
                        new_info_list=[]
                        for i in item[0]:
                            new_info_item=self.multi_select(i,"input") 
                            if type(new_info_item) == ErrorMessage:
                                error=(True,new_info_item)
                            new_info_list.append(new_info_item)
                        if error[0]:
                            new_info=error[1]
                        else:
                            new_info=item[1].join(new_info_list)

                    except ValueError:
                        new_info = ErrorMessage(1012,"value error",None)    
                else: 
                    item1=item+":"
                    new_info=input("{:<16}|".format(item1)) #býr til basic info 

                if type(new_info)==ErrorMessage:
                    return ErrorMessage
                info_list.append(new_info)
            return info_list
        else:
            return ErrorMessage(1011,"invalid id",None)

    def ui_loop(self):
        logic = self.logic
        today = str(date.today())
        today = today.split("-")
        today[0] = today[0][2:4]
        new_day = today[::-1]
        str_today = ''
        for i in new_day:
            str_today += i+"-"
        str_today = str_today[:-1]
        input_list = input

        while input_list != "q":
            print("|" + "—" * 191 +"|")
            print("|",str_today,"\t|\t\t\t\t\t\t\t\t\tNaN Air\t\t\t\t\t\t\t\t\t\t|\t(Q) quit\t|")
            print("|" + "—" * 191 +"|")
            print("| 1. Starfsmenn\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
            print("| 2. Áfangastaðir\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
            print("| 3. Farartæki\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
            print("| 4. Leiga\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
            print("|" + "—" * 191 +"|")
            input_list = input("input: ")
            self.clear()
            
            
            if input_list == "1":
                #starfsmadur_dict = {}
                #afangastadir_dict = {}
                #logic.get_starfsmadur_file(starfsmadur_dict))
                #logic.get_afangastadir_file(afangastadir_dict)
                while input_list != "b":

                    try:
                        starfsmadur_dict=logic.starfsmenn_read_list()
                        print("|" + "—" * 191 +"|")
                        print("|\t",str_today,"\t|\t\tStarfsmenn\t\t|\t\t\t\t\t\t\t\t\t\t\t\t\t|\t(B) back\t|")
                        print("|" + "—" * 191 +"|")
                        self.print_starfsmenn_list(starfsmadur_dict)
                        print("|" + "—" * 191 +"|")
                        print("|\t(S) skrá starfsmann\t\t|\t(F) finna og breyta starfsmanni\t\t|\t(E) eyða starfsmanni\t\t|\t\t\t\t\t\t\t\t|")
                        print("|" + "—" * 191 +"|")
                        input_list = input("input: ")


                        if input_list == "s":
                            try:
                                counter = 0
                                input_list = input
                                id = int(input("id: "))
                                if id not in starfsmadur_dict:
                                    nafn = input("nafn:\t\t| ")
                                    kennitala = input("kennitala:\t| ")
                                    heimilisfang = input("heimilisfang:\t| ")
                                    tolvupostur = input("tölvupóstur:\t| ")
                                    simanumer = input("símanúmer:\t| ")
                                    heimilissimi = input("heimilissími:\t| ")
                                    stadsetning = self.stadsetning_select()
                                    if type(stadsetning)==ErrorMessage:
                                        int("error")

                                    #logic.get_starfsmadur(starfsmadur_dict, id, nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning)
                                    starfsmadur_dict = logic.starfsmenn_read_list()#VG
                                    if id > 1: #ha? VG
                                        ret=logic.add_starfsmenn_results(starfsmadur_dict, id, nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning)
                                        if type(ret) == ErrorMessage : #VG ret = return
                                            int("ValueError") 
                                        self.clear()
                                else:
                                    self.clear()
                                    print("########################")
                                    print("##### ID þegar til #####")
                                    print("########################")
                    
                            except ValueError:
                                self.clear()
                                print("#########################")
                                print("##### Invalid input #####")
                                print("#########################")
                        

                        elif input_list == "f":
                            input_number = input
                            try:
                                counter = 0
                                id = int(input("id: "))
                                if id in starfsmadur_dict:
                                    nafn = starfsmadur_dict[id][0]
                                    kennitala = starfsmadur_dict[id][1]
                                    heimilisfang = starfsmadur_dict[id][2]
                                    tolvupostur = starfsmadur_dict[id][3]
                                    simanumer = starfsmadur_dict[id][4]
                                    heimilissimi = starfsmadur_dict[id][5]
                                    stadsetning = starfsmadur_dict[id][6]
                                    while input_number != "b": #VG ætti ekki að vera option að vera búinn(done) í staðin fyrir að þurfa að fara til bak þegar það er oftast skilið sem hætta við en ekki halda áfram
                                        print()
                                        print("|\t(B) back\t|" + "—" * 167 +"|")
                                        print("| 1. heimilisfang", "\t"*22 + "|\n| 2. tölvupóstur", "\t"*22 + "|\n| 3. símanúmer", "\t"*23 + "|\n| 4. heimilissími", "\t"*22 + "|\n| 5. staðsetning", "\t"*22 + "|")
                                        print("|" + "—" * 191 +"|")
                                        input_number = input("input: ")
                                        if input_number == "1":
                                            heimilisfang = input("| heimilisfang:\t| ")
                                        elif input_number == "2":
                                            tolvupostur = input("| tölvupóstur:\t| ")
                                        elif input_number == "3":
                                            simanumer = input("| símanúmer:\t| ")
                                        elif input_number == "4":
                                            heimilissimi = input("| heimilissími:\t| ")
                                        elif input_number == "5":
                                            stadsetning = self.stadsetning_select()
                                            if type(stadsetning)==ErrorMessage:
                                                int("error")
                                        elif input_number == 'b':
                                            continue
                                        else:
                                            print("#########################")
                                            print("##### Invalid input #####")
                                            print("#########################")
                                    #logic.get_starfsmadur(starfsmadur_dict, id, nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning)
                                    if id > 1:
                                        ret=logic.add_starfsmenn_results(starfsmadur_dict, id, nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning)
                                        if type(ret) == ErrorMessage : #VG ret = return
                                            int("ValueError") 
                                        self.clear() # ætti að ver a nýt func fyrir að breita gera_seinna VG
                                else:
                                    self.clear()
                                    print("#######################")
                                    print("##### ID ekki til #####")
                                    print("#######################")
                            except ValueError:
                                self.clear()
                                print("#########################")
                                print("##### Invalid input #####")
                                print("#########################")
                        

                        elif input_list == "e":
                            id = int(input("id:\t\t| "))
                            if id in starfsmadur_dict:
                                logic.eyda_element("starfsmadur_dict", id) #VG
                                self.clear()
                            else:
                                self.clear()
                                print("#######################")
                                print("##### ID ekki til #####")
                                print("#######################")

                        elif input_list == "b":
                            self.clear()
                            break

                        else:
                            self.clear()
                            print("#########################")
                            print("##### Invalid input #####")
                            print("#########################")

                    except ValueError:
                        self.clear()
                        print("#########################")
                        print("##### Invalid input #####")
                        print("#########################")

            elif input_list == "2":
                #afangastadir_dict = {}
                #logic.get_afangastadir_file(afangastadir_dict)
                try:
                    while input_list != "b":
                        afangastadir_dict = logic.afangastadir_read_list() #VG
                        print("|" + "—" * 191 +"|")
                        print("|", str_today, "\t| Áfangastaðir\t|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|\t(B) back\t|")
                        print("|" + "—" * 191 +"|")
                        self.print_afangastadir_list(afangastadir_dict)
                        print("|" + "—" * 191 +"|")
                        print("|\t(S) skrá áfangastað\t\t|\t(F) finna og breyta áfangastað\t\t|\t(E) eyða áfangastað\t\t|\t\t\t\t\t\t\t\t|")
                        print("|" + "—" * 191 +"|")
                        input_list = input("input: ")


                        if input_list == "s":
                            try:
                                input_list = input
                                list_of_info = self.make_info(afangastadir_dict,["borg","land","flugvöllur","símanúmer",[[["08:00","09:00","10:00","11:00"],["20:00","21:00","22:00","23:00"]],"-"]])
                                
                                    #logic.get_afangastadir(afangastadir_dict, id, borg, land, flugvollur, simanumer, opnunartimi)
                                afangastadir_dict = logic.afangastadir_read_list() #VG
                                
                                ret=logic.add_afangastadir_results(afangastadir_dict, str(list_of_info[0]), list_of_info[1], list_of_info[2], list_of_info[3], list_of_info[4], list_of_info[5])
                                if type(ret) == ErrorMessage : #VG ret = return
                                    int("ValueError")
                                self.clear()
                                
                            except ValueError:
                                self.clear()
                                print("#########################")
                                print("##### Invalid input #####")
                                print("#########################")
                        

                        elif input_list == "f":
                            input_number = input
                            try:
                                id = int(input("id: "))
                                if id in afangastadir_dict:
                                    borg = afangastadir_dict[id][0]
                                    land = afangastadir_dict[id][1]
                                    flugvollur = afangastadir_dict[id][2]
                                    simanumer = afangastadir_dict[id][3]
                                    opnunartimi = afangastadir_dict[id][4]
                                    while input_number != "b":
                                        print()
                                        print("|\t(B) back\t|" + "—" * 167 +"|")
                                        print("| 1. borg", "\t"*23 + "|\n| 2. land", "\t"*23 + "|\n| 3. flugvöllur", "\t"*22 + "|\n| 4. símanúmer", "\t"*23 + "|\n| 5. opnunartími", "\t"*22 + "|")
                                        print("|" + "—" * 191 +"|")
                                        print()
                                        input_number = input("input: ")
                                        if input_number =="b" or input_number == "B":
                                            continue
                                        elif input_number == "1":
                                            borg = input("| borg:\t| ")
                                        elif input_number == "2":
                                            land = input("| land:\t\t| ")
                                        elif input_number == "3":
                                            flugvollur = input("| flugvöllur:\t| ")
                                        elif input_number == "4":
                                            simanumer = input("| símanumer:\t| ")
                                        elif input_number == "5":
                                            print("—" * 25)
                                            print("1. 08:00\n2. 09:00\n3. 10:00\n4. 11:00")
                                            print("—" * 25)
                                            time_imput1 = int(input("input: "))
                                            if time_imput1 == 1:
                                                open_time = "08:00"
                                            if time_imput1 == 2:
                                                open_time = "09:00"
                                            if time_imput1 == 3:
                                                open_time = "10:00"
                                            if time_imput1 == 4:
                                                open_time = "11:00"
                                            print()
                                            print("—" * 25)
                                            print("1. 20:00\n2. 21:00\n3. 22:00\n4. 23:00")
                                            print("—" * 25)
                                            time_imput2 = int(input("input: "))
                                            if time_imput2 == 1:
                                                close_time = "20:00"
                                            if time_imput2 == 2:
                                                close_time = "21:00"
                                            if time_imput2 == 3:
                                                close_time = "22:00"
                                            if time_imput2 == 4:
                                                close_time = "23:00"
                                            opnunartimi = "{}-{}".format(open_time, close_time)
                                        else:
                                            print("#########################")
                                            print("##### Invalid input #####")
                                            print("#########################")
                                    #logic.get_afangastadir(afangastadir_dict, id, borg, land, flugvollur, simanumer, opnunartimi)
                                    if id > 1:
                                        ret=logic.add_afangastadir_results(afangastadir_dict, str(id), borg, land, flugvollur, simanumer, opnunartimi)
                                        if type(ret) == ErrorMessage : #VG ret = return
                                            int("ValueError") 
                                        self.clear()
                                else:
                                    self.clear()
                                    print("#######################")
                                    print("##### ID ekki til #####")
                                    print("#######################")
                            except ValueError:
                                self.clear()
                                print("#########################")
                                print("##### Invalid input #####")
                                print("#########################")
                        

                        elif input_list == "e":
                            id = int(input("id:\t\t| "))
                            if id in afangastadir_dict:
                                logic.eyda_element("afangastadir_dict", id)
                                self.clear()
                            else:
                                self.clear()
                                print("#######################")
                                print("##### ID ekki til #####")
                                print("#######################")

                        elif input_list == "b":
                            self.clear()
                            break

                        else:
                            self.clear()
                            print("#########################")
                            print("##### Invalid input #####")
                            print("#########################")

                except ValueError:
                    self.clear()
                    print("#########################")
                    print("##### Invalid input #####")
                    print("#########################")

            elif input_list == "3":
                #farartaeki_dict = {}
                #afangastadir_dict = {}
                #logic.get_farartaeki_file(farartaeki_dict)
                #logic.get_afangastadir_file(afangastadir_dict)
                try:
                    while input_list != "b":
                        farartaeki_dict = logic.farartaeki_read_list()
                        print("|" + "—" * 207 +"|")
                        print("|", str_today, "\t| Farartaeki\t|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|\t(B) back\t|")
                        print("|" + "—" * 207 +"|")
                        self.print_farartaeki_list(farartaeki_dict)
                        print("|" + "—" * 207 +"|")
                        print("|\t(S) skrá farartæki\t\t|\t(F) finna og breyta farartæki\t\t|\t(E) eyða farartæki\t\t|\t\t\t\t\t\t\t\t\t\t|")
                        print("|" + "—" * 207 +"|")
                        input_list = input("input: ")


                        if input_list == "s":
                            try:
                                id = int(input("id: "))
                                if id not in farartaeki_dict:
                                    nafn = input("nafn:\t\t| ")
                                    numeraplata = input("númeraplata:\t| ")
                                    fratekid = input("frátekið:\t| ")
                                    typa = self.multi_select(["A","B","C","D"],"ökuréttindi")
                                    if type(typa)== ErrorMessage:
                                        int("error")
                                    print()
                                    stadsetning = self.stadsetning_select()
                                    if type(stadsetning)==ErrorMessage:
                                        int("error")
                                            
                                    vidhald = self.multi_select(["Í lagi","Bilað"],"Vidhald")
                                    litur = input("litur:\t\t| ")
                                    argerd = input("árgerð:\t\t| ")
                                    km = input("km:\t\t| ")
                                    gerd = self.multi_select(["Fólksbíll","Jeppi","Mótorhjól","Trukkur","Seglbátur","Snekkja","Spíttbátur"],"Gerð")#VG
                                    if gerd == "Fólksbíll":
                                        taxi = str(12)
                                    elif gerd == "Jeppi":
                                        taxi = str(14)
                                    elif gerd == "Mótorhjól":
                                        taxi = str(8)
                                    elif gerd == "Trukkur":
                                        taxi = str(20)
                                    elif gerd == "Seglbátur":
                                        taxi = str(10)
                                    elif gerd == "Snekkja":
                                        taxi = str(35)
                                    elif gerd == "Spíttbátur":
                                        taxi = str(24)

                                    if type(gerd)== ErrorMessage:
                                        int("error")
                                    #logic.get_farartaeki(farartaeki_dict, id, area, nafn, numeraplata, fratekid, typa, stadsetning, vidhald, litur, argerd, taxi, km)
                                    if id > 1:
                                        ret=logic.add_farartaeki_results(farartaeki_dict, id, nafn, numeraplata, fratekid, typa, stadsetning, vidhald, litur, argerd, taxi, km,gerd)
                                        if type(ret) == ErrorMessage : #VG ret = return
                                            int("ValueError") 
                                        self.clear()
                                else:
                                    self.clear()
                                    print("########################")
                                    print("##### ID þegar til #####")
                                    print("########################")
                            except ValueError:
                                self.clear()
                                print("#########################")
                                print("##### Invalid input #####")
                                print("#########################")
                        

                        elif input_list == "f":
                            input_number = input
                            try:
                                id = int(input("id: "))
                                if id in farartaeki_dict:
                                    
                                    nafn = farartaeki_dict[id][0]
                                    numeraplata = farartaeki_dict[id][1]
                                    fratekid = farartaeki_dict[id][2]
                                    typa = farartaeki_dict[id][3]
                                    stadsetning = farartaeki_dict[id][4]
                                    vidhald = farartaeki_dict[id][5]
                                    litur = farartaeki_dict[id][6]
                                    argerd = farartaeki_dict[id][7]
                                    taxi = farartaeki_dict[id][8]
                                    km = farartaeki_dict[id][9]
                                    gerd = farartaeki_dict[id][10]

                                    while input_number != "b":
                                        print()
                                        print("|\t(B) back\t|" + "—" * 167 +"|")
                                        print("| 1. nafn", "\t"*23 + "|\n| 2. númeraplata", "\t"*22 + "|\n| 3. frátekið", "\t"*23 + "|\n| 4. týpa", "\t"*23 + "|\n| 5. staðsetning", "\t"*22 + "|\n| 6. viðhald", "\t"*23 + "|\n| 7. litur", "\t"*23 + "|\n| 8. árgerð", "\t"*23 + "|\n| 9. km", "\t"*23 + "|\n| 10. farartækja gerð", "\t"*22 + "|")
                                        print("|" + "—" * 191 +"|")
                                        print()
                                        input_number = input("input: ")
                                        if input_number == "1":
                                            nafn = input("| nafn:\t| ")
                                        elif input_number == "2":
                                            numeraplata = input("| númeraplata:\t\t| ")
                                        elif input_number == "3":
                                            fratekid = input("| frátekið:\t| ")
                                        elif input_number == "4":
                                            
                                            typa = self.multi_select(["A","B","C","D"],"ökuréttindi")
                                            if type(typa)== ErrorMessage:
                                                int("error")
                                            
                                            print("—" * 25)
                                        elif input_number == "5":
                                            stadsetning = self.stadsetning_select()
                                            if type(stadsetning)== ErrorMessage:
                                                int("error")
                                            
                                        elif input_number == "6":
                                            vidhald = self.multi_select(["Í lagi","Bilað"],"Vidhald")
                                        elif input_number == "7":
                                            litur = input("| litur:\t| ")
                                        elif input_number == "8":
                                            argerd = input("| árgerð:\t| ")
                                        elif input_number == "9":
                                            km = input("| km:\t| ")
                                        elif input_number == "10":
                                            gerd = self.multi_select(["Fólksbíll","Jeppi","Mótorhjól","Trukkur","Seglbátur","Snekkja","Spíttbátur"],"Gerð")#VG
                                            if gerd == "Fólksbíll":
                                                taxi = str(12)
                                            elif gerd == "Jeppi":
                                                taxi = str(14)
                                            elif gerd == "Mótorhjól":
                                                taxi = str(8)
                                            elif gerd == "Trukkur":
                                                taxi = str(20)
                                            elif gerd == "Seglbátur":
                                                taxi = str(10)
                                            elif gerd == "Snekkja":
                                                taxi = str(35)
                                            elif gerd == "Spíttbátur":
                                                taxi = str(24)
                                        elif input_number == 'b':
                                            continue
                                        else:
                                            print("#########################")
                                            print("##### Invalid input #####")
                                            print("#########################")
                                    #logic.get_farartaeki(farartaeki_dict, id, nafn, numeraplata, fratekid, typa, stadsetning, vidhald, litur, argerd, taxi, km, gerd)
                                    if id > 1:
                                        ret=logic.add_farartaeki_results(farartaeki_dict, id,  nafn, numeraplata, fratekid, typa, stadsetning, vidhald, litur, argerd, taxi, km, gerd)
                                        if type(ret) == ErrorMessage : #VG ret = return
                                            int("ValueError") 
                                        self.clear()
                                else:
                                    self.clear()
                                    print("#######################")
                                    print("##### ID ekki til #####")
                                    print("#######################")
                            except ValueError:
                                self.clear()
                                print("#########################")
                                print("##### Invalid input #####")
                                print("#########################")
                        

                        elif input_list == "e":
                            id = int(input("id:\t\t| "))
                            if id in farartaeki_dict:
                                logic.eyda_element("farartaeki_dict", id)
                                self.clear()
                            else:
                                self.clear()
                                print("#######################")
                                print("##### ID ekki til #####")
                                print("#######################")

                        elif input_list == "b":
                                self.clear()
                                break

                        else:
                            self.clear()
                            print("#########################")
                            print("##### Invalid input #####")
                            print("#########################")

                except ValueError:
                    self.clear()
                    print("#########################")
                    print("##### Invalid input #####")
                    print("#########################")

            elif input_list == "4":
                #leiga_dict = {}
                #leigjandi_dict = {}
                #farartaeki_dict = {}
                #starfsmadur_dict = {}
                #afangastadir_dict = {}
                #logic.get_leiga_file(leiga_dict)
                #logic.get_leigjandi_file(leigjandi_dict)
                #logic.get_farartaeki_file(farartaeki_dict)
                #logic.get_starfsmadur_file(starfsmadur_dict)
                #logic.get_afangastadir_file(afangastadir_dict)
                
                leiga_dict = logic.leiga_read_list()
                leigjandi_dict = logic.leigjandi_read_list()
                farartaeki_dict = logic.farartaeki_read_list()
                starfsmadur_dict = logic.starfsmenn_read_list()
                afangastadir_dict = logic.afangastadir_read_list()
                
                try:
                    while input_list != "b":
                        leiga_dict=logic.leiga_read_list()
                        leigjandi_dict=logic.leigjandi_read_list()
                        print("|" + "—" * 191 +"|")
                        print("|", str_today, "\t|\t\tLeiga\t\t\t|\t\t\t\t\t\t\t\t\t\t\t\t\t\t|\t(B) back\t|")
                        print("|" + "—" * 191 +"|")
                        self.print_leiga_list(leigjandi_dict, leiga_dict)
                        print("|" + "—" * 191 +"|")
                        print("|\t(S) skrá leigu\t\t|\t(F) finna og breyta leigu\t\t|\t(E) eyða leigu\t\t|\t(P) prenta leigusamning\t\t\t\t\t\t\t|")
                        print("|" + "—" * 191 +"|")
                        input_list = input("input: ")


                        if input_list == "s":
                            try:
                                counter = 0
                                id = int(input("id: "))
                                print()
                                if id not in leigjandi_dict:
                                    id_samningur = id
                                    id_leigjandi = id
                                    nafn = input("| nafn:\t\t\t\t| ")
                                    kennitala = input("| kennitala:\t\t\t| ")
                                    simanumer = input("| símanúmer:\t\t\t| ")
                                    heimilisfang = input("| heimilisfang:\t\t\t| ")
                                    tolvupostur = input("| tölvupóstur:\t\t\t| ")
                                    print("—" * 25)
                                    print("| 1. A\n| 2. B\n| 3. C\n| 4. D")
                                    print("—" * 25)
                                    type_input = int(input("ökuréttindi: "))
                                    if type_input == 1:
                                        typa = "A"
                                    if type_input == 2:
                                        typa = "B"
                                    if type_input == 3:
                                        typa = "C"
                                    if type_input == 4:
                                        typa = "D"
                                    print()
                                    print("—" * 25)
                                    print("\tNafn\t\t\t\tLaus\t\tTýpa\t\tStaðsetning")
                                    print("—" * 95)
                                    counter=0
                                    for i in farartaeki_dict:
                                        counter += 1
                                        print("{}. {:<32}\t{:<10}\t{:<10}\t{:<10}".format(counter, farartaeki_dict[i][0], farartaeki_dict[i][2], farartaeki_dict[i][3], farartaeki_dict[i][4]))
                                    print("—" * 25)
                                    id_farartaeki = int(input("| farartæki: "))
                                    print()
                                    print("—" * 25)
                                    counter = 0
                                    for i in starfsmadur_dict:
                                        counter += 1
                                        print(counter, "-", starfsmadur_dict[i][0])
                                    print("—" * 25)
                                    input_list = int(input("| id starfsmaður: "))
                                    counter = 0
                                    for i in starfsmadur_dict:
                                        counter += 1
                                        if input_list == counter:
                                            id_starfsmadur = counter
                                    print()
                                    print("—" * 25)
                                    for i in farartaeki_dict:
                                        if i == id_farartaeki:
                                            afangastadir = farartaeki_dict[i][4]
                                            for j in afangastadir_dict:
                                                if afangastadir == afangastadir_dict[j][0]:
                                                    id_afangastadir = j


                                    print()
                                    kostnadur = int(input("| kostnaður:\t\t| "))

                                    counter = 0
                                    

                                    samningur_stofnadur = str_today
                                    byrjun_samningur = input("byrjun samnings:\t| ")
                                    endir_samningur = input("endir samnings:\t\t| ")
                                    print()
                                    print("—" * 25)
                                    print("| 1. 10:00\n| 2. 11:00\n| 3. 12:00\n| 4. 13:00\n| 5. 14:00\n| 6. 15:00")
                                    print("—" * 25)
                                    time_imput = int(input("| sækja klukkan: "))
                                    if time_imput == 1:
                                        pickup_timi = "10:00"
                                    if time_imput == 2:
                                        pickup_timi = "11:00"
                                    if time_imput == 3:
                                        pickup_timi = "12:00"
                                    if time_imput == 4:
                                        pickup_timi = "13:00"
                                    if time_imput == 5:
                                        pickup_timi = "14:00"
                                    if time_imput == 6:
                                        pickup_timi = "15:00"
                                    print()
                                    print("—" * 25)
                                    print("| 1. Já\n| 2. Nei")
                                    pay_list = int(input("| rukkaður: "))
                                    if pay_list == 1:
                                        rukkadur = "Já"
                                    if pay_list == 2:
                                        rukkadur = "Nei"
                                    print("—" * 25)
                                    print("| 1. Já\n| 2. Nei\n| 3. Skil")
                                    skil_list = int(input("| Mótaka: "))
                                    if skil_list == 1:
                                        motaka = "Já"
                                    if skil_list == 2:
                                        motaka = "Nei"
                                    if skil_list == 3:
                                        motaka = "Skil"
                                    print("—" * 25)
                                    #logic.get_leiga(leiga_dict, id_samningur, id_leigjandi, id_starfsmadur, kostnadur, id_farartaeki,id_afangastadir, samningur_stofnadur, byrjun_samningur, endir_samningur, pickup_timi, rukkadur, motaka)
                                    #logic.get_leigjandi(leigjandi_dict, id, nafn, kennitala,simanumer,heimilisfang,tolvupostur,typa)
                                    
                                    leigjandi_dict=logic.leigjandi_read_list()
                                    leiga_dict=logic.leiga_read_list()
                                    if id > 1:
                                        
                                        ret2=logic.add_leigjandi_results(leigjandi_dict, str(id_leigjandi), nafn, kennitala,simanumer,heimilisfang,tolvupostur,typa)

                                        ret1=logic.add_leiga_results(leiga_dict, str(id_samningur), str(id_leigjandi), str(id_starfsmadur), kostnadur, str(id_farartaeki),str(id_afangastadir), samningur_stofnadur, byrjun_samningur, endir_samningur, pickup_timi, rukkadur, motaka)
                                        if type(ret1) == ErrorMessage or type(ret2) == ErrorMessage: #VG ret = return
                                            print(ret1)
                                            print(ret2)
                                            #delet?
                                            int("ValueError") 
                                        self.clear()
                                else:
                                    self.clear()
                                    print("########################")
                                    print("##### ID þegar til #####")
                                    print("########################")
                            except ValueError:
                                self.clear()
                                print("#########################")
                                print("##### Invalid input #####")
                                print("#########################")
                        

                        elif input_list == "f":
                            input_number = input
                            try:
                                id = int(input("id: "))
                                if id in leigjandi_dict:
                                    nafn = leigjandi_dict[id][0]
                                    kennitala = leigjandi_dict[id][1]
                                    simanumer = leigjandi_dict[id][2]
                                    heimilisfang = leigjandi_dict[id][3]
                                    tolvupostur = leigjandi_dict[id][4]
                                    typa = leigjandi_dict[id][5]
                                    id_leigjandi = leiga_dict[id][0]
                                    id_starfsmadur = leiga_dict[id][1]
                                    kostnadur = leiga_dict[id][2]
                                    id_farartaeki = leiga_dict[id][3]
                                    id_afangastadir = leiga_dict[id][4]
                                    samningur_stofnadur = leiga_dict[id][5]
                                    byrjun_samningur = leiga_dict[id][6]
                                    endir_samningur = leiga_dict[id][7]
                                    pickup_timi = leiga_dict[id][8]
                                    rukkadur = leiga_dict[id][9]
                                    motaka = leiga_dict[id][10]
                                    while input_number != "b":
                                        id_samningur = id
                                        id_leigjandi = id
                                        print()
                                        print("|\t(B) back\t|" + "—" * 167 +"|")
                                        print("| 1. nafn", "\t"*23 + "|\n| 2. símanumer", "\t"*23 + "|\n| 3. heimilisfang", "\t"*22 + "|\n| 4. ökuréttindi", "\t"*22 + "|\n| 5. byrjun samningur", "\t"*22 + "|\n| 6. endir samningur", "\t"*22 + "|\n| 7. sækja klukkan", "\t"*22 + "|\n| 8. rukkaður", "\t"*23 + "|\n| 9. mótaka", "\t"*23 +"|\n| 10. farartæki", "\t"*23+ "|")
                                        print("|" + "—" * 191 +"|")
                                        print()
                                        input_number = input("input: ")
                                        if input_number =="b":
                                            continue
                                        elif input_number == "1":
                                            nafn = input("| nafn:\t| ")
                                        elif input_number == "2":
                                            simanumer = input("| símanumer:\t\t| ")
                                        elif input_number == "3":
                                            heimilisfang = input("| heimilisfang:\t| ")
                                        elif input_number == "4":
                                             print("—" * 25)
                                             print("| 1. A\n| 2. B\n| 3. C\n| 4. D")
                                             print("—" * 25)
                                             type_input = int(input("| ökuréttindi: "))
                                             if type_input == 1:
                                                 typa = "A"
                                             if type_input == 2:
                                                 typa = "B"
                                             if type_input == 3:
                                                 typa = "C"
                                             if type_input == 4:
                                                 typa = "D"
    
                                        elif input_number == "5":
                                            byrjun_samningur = input("| byrjun samningur:\t| ")
                                        elif input_number == "6":
                                            endir_samningur = input("| endir samningur:\t| ")
                                        elif input_number == "7":
                                            print("—" * 25)
                                            print("| 1. 10:00\n| 2. 11:00\n| 3. 12:00\n| 4. 13:00\n| 5. 14:00\n| 6. 15:00")
                                            print("—" * 25)
                                            time_imput = int(input("| sækja klukkan: "))
                                            if time_imput == 1:
                                                pickup_timi = "10:00"
                                            if time_imput == 2:
                                                pickup_timi = "11:00"
                                            if time_imput == 3:
                                                pickup_timi = "12:00"
                                            if time_imput == 4:
                                                pickup_timi = "13:00"
                                            if time_imput == 5:
                                                pickup_timi = "14:00"
                                            if time_imput == 6:
                                                pickup_timi = "15:00"
                                        elif input_number == "8":
                                            print("—" * 25)
                                            print("| 1. Já\n| 2. Nei")
                                            pay_list = int(input("| rukkaður: "))
                                            if pay_list == 1:
                                                rukkadur = "Já"
                                            if pay_list == 2:
                                                rukkadur = "Nei"
                                        elif input_number == "9":
                                            print("—" * 25)
                                            print("| 1. Já\n| 2. Nei\n| 3. Skil")
                                            skil_list = int(input("| mótaka: "))
                                            if skil_list == 1:
                                                motaka = "Já"
                                            if skil_list == 2:
                                                motaka = "Nei"
                                            if skil_list == 3:
                                                motaka = "Skil"
                                            print("—" * 25)
                                        elif input_number == "10":
                                            
                                            print("\tNafn\t\t\t\tLaus\t\tTýpa\t\tStaðsetning")
                                            print("—" * 95)
                                            counter=0
                                            for i in farartaeki_dict:
                                                counter += 1
                                                print("{}. {:<32}\t{:<10}\t{:<10}\t{:<10}".format(counter, farartaeki_dict[i][0], farartaeki_dict[i][2], farartaeki_dict[i][3], farartaeki_dict[i][4]))
                                            print("—" * 25)
                                            id_farartaeki = int(input("| farartæki: "))
                                            print()
                                            print("—" * 25)
                                        else:
                                            print("#########################")
                                            print("##### Invalid input #####")
                                            print("#########################")

                                    #logic.get_leiga(leiga_dict, id_samningur, id_leigjandi, id_starfsmadur, kostnadur, id_farartaeki,id_afangastadir, samningur_stofnadur, byrjun_samningur, endir_samningur, pickup_timi, rukkadur, motaka)
                                    #logic.get_leigjandi(leigjandi_dict, id, nafn, kennitala,simanumer,heimilisfang,tolvupostur,typa)
                                    leiga_dict=logic.leiga_read_list()
                                    leigjandi_dict=logic.leigjandi_read_list()
                                    if id > 1:
                                        ret2=logic.add_leigjandi_results(leigjandi_dict, str(id_leigjandi), nafn, kennitala,simanumer,heimilisfang,tolvupostur,typa)

                                        ret1=logic.add_leiga_results(leiga_dict, str(id_samningur), str(id_leigjandi), str(id_starfsmadur), kostnadur, str(id_farartaeki),str(id_afangastadir), samningur_stofnadur, byrjun_samningur, endir_samningur, pickup_timi, rukkadur, motaka)
                                        if type(ret1) == ErrorMessage or type(ret2) == ErrorMessage:
                                            int("ValueError")
                                        self.clear()
                                else:
                                    self.clear()
                                    print("#######################")
                                    print("##### ID ekki til #####")
                                    print("#######################")
                            except ValueError:
                                self.clear()
                                print("#########################")
                                print("##### Invalid input #####")
                                print("#########################")
                        

                        elif input_list == "e":
                            id = int(input("id:\t\t| "))
                            if id in leigjandi_dict:
                                logic.eyda_element("leigjandi_dict", id)
                                logic.eyda_element("leiga_dict", id)
                                self.clear()
                            else:
                                self.clear()
                                print("#######################")
                                print("##### ID ekki til #####")
                                print("#######################")

                        elif input_list == "p":
                            leiga_dict=logic.leiga_read_list()
                            leigjandi_dict=logic.leigjandi_read_list()

                            input_number = input
                            id = int(input("id:\t\t| "))
                            if id in leigjandi_dict:
                                while input_number != "b":
                                    self.clear()


                                    nafn = leigjandi_dict[id][0]
                                    kennitala = leigjandi_dict[id][1]
                                    simanumer = leigjandi_dict[id][2]
                                    heimilisfang = leigjandi_dict[id][3]
                                    tolvupostur = leigjandi_dict[id][4]
                                    typa = leigjandi_dict[id][5]
                                    id_leigjandi = leiga_dict[id][0]
                                    id_starfsmadur = leiga_dict[id][1]
                                    kostnadur = leiga_dict[id][2]
                                    id_farartaeki = leiga_dict[id][3]
                                    id_afangastadir = leiga_dict[id][4]
                                    samningur_stofnadur = leiga_dict[id][5]
                                    byrjun_samningur = leiga_dict[id][6]
                                    endir_samningur = leiga_dict[id][7]
                                    pickup_timi = leiga_dict[id][8]
                                    rukkadur = leiga_dict[id][9]
                                    motaka = leiga_dict[id][10]
                                    
                                    counter = 0
                                    for i in farartaeki_dict:
                                        counter += 1
                                        if int(id_farartaeki) == counter:
                                            farartaeki = farartaeki_dict[i][0]
                                            numeraplata = farartaeki_dict[i][1]
                                            fratekid = farartaeki_dict[i][2]
                                            typa = farartaeki_dict[i][3]
                                            afangastadur = farartaeki_dict[i][4]
                                            vidhald = farartaeki_dict[i][5]
                                            litur = farartaeki_dict[i][6]
                                            argerd = farartaeki_dict[i][7]
                                            taxi = farartaeki_dict[i][8]
                                            km = farartaeki_dict[i][9]
                                            gerð = farartaeki_dict[i][10]
                                            
                                            for j in afangastadir_dict:
                                                if afangastadir_dict[j][0] == afangastadur: #VG 
                                                    borg = afangastadir_dict[j][0]
                                                    land = afangastadir_dict[j][1]
                                                    flugvollur = afangastadir_dict[j][2]
                                                    simanumer = afangastadir_dict[j][3]
                                                    opnunartimi = afangastadir_dict[j][4]


                                    print("|" + "—" * 191 +"|")
                                    print("|", str_today, "\t|\t\tLeiga\t\t\t|\t\t\t\t\t\t\t\t\t\t\t\t\t\t|\t(B) back\t|")
                                    print("|" + "—" * 191 +"|")
                                    print("|\t\t\t\tEinstaklingur\t\t\t|\t\t\tBifreið\t\t\t\t\t|\t\t\t\tStaðsetning\t\t\t|")
                                    print("|" + "—" * 191 +"|")
                                    print("|\tNafn:\t\t\t{:<22}\t\t| tegund:\t\t{:<32}\t| áfangastaður:\t{:<14}\t\t\t\t\t|".format(leigjandi_dict[id][0],farartaeki,borg))
                                    print("|" + "—" * 191 +"|")
                                    print("|\tSímanúmer:\t\t{:<18}\t\t| númeraplata:\t\t{:<8}\t\t\t\t| land:\t\t{:<14}\t\t\t\t\t\t|".format(leigjandi_dict[id][2],numeraplata,land))
                                    print("|" + "—" * 191 +"|")
                                    print("|\tHeimilisfang:\t\t{:<20}\t\t| frátekið:\t\t{:<6}\t\t\t\t\t| flugvöllur:\t{:<24}\t\t\t|".format(leigjandi_dict[id][3],fratekid,flugvollur))
                                    print("|" + "—" * 191 +"|")
                                    print("|\tTölvupóstur:\t\t{:<24}\t| týpa:\t\t\t{:<4}\t\t\t\t\t| símanúmer:\t{:<16}\t\t\t\t|".format(leigjandi_dict[id][4],typa,simanumer))
                                    print("|" + "—" * 191 +"|")
                                    print("|\tFrátekið tímabil:\t{:<8}-{:<8}\t\t| áfangastaður:\t\t{:<18}\t\t\t| opnunartími:\t{:<18}\t\t\t\t|".format(leiga_dict[id][6],leiga_dict[id][7],afangastadur,opnunartimi))
                                    print("|" + "—" * 191 +"|")
                                    print("|\tAfhending:\t\t{:<8}\t\t\t| viðhald:\t\t{:<8}\t\t\t\t|\t\t\t\t\t\t\t\t|".format(leiga_dict[id][8],vidhald))
                                    print("|" + "—" * 191 +"|")
                                    print("|\tMótaka:\t\t\t{:<4}\t\t\t\t| litur:\t\t{:<16}\t\t\t|\t\t\t\t\t\t\t\t|".format(leiga_dict[id][10],litur))
                                    print("|" + "—" * 191 +"|")
                                    print("|\tUpphæð + taxi:\t\t{:<10}\t\t\t| árgerð:\t\t{:<6}\t\t\t\t\t|\t\t\t\t\t\t\t\t|".format(leiga_dict[id][2],argerd))
                                    print("|" + "—" * 191 +"|")
                                    print("|\t\t\t\t\t\t\t\t| taxi:\t\t\t{}%\t\t\t\t\t|\t\t\t\t\t\t\t\t|".format(taxi))
                                    print("|" + "—" * 191 +"|")
                                    print("|\t\t\t\t\t\t\t\t| kílómetrar keyrðir:\t{:<6} KM\t\t\t\t|\t\t\t\t\t\t\t\t|".format(km))
                                    print("|" + "—" * 191 +"|")
                                    print("|\t\t\t\t\t\t\t\t| gerð:\t\t\t{:<8}   \t\t\t\t|\t\t\t\t\t\t\t\t|".format(gerð))
                                    print("|" + "—" * 191 +"|")
                                    input_number = input("input: ")
                                    self.clear()

                        elif input_list == "b":
                                self.clear()
                                break

                        else:
                            self.clear()
                            print("#########################")
                            print("##### Invalid input #####")
                            print("#########################")

                except ValueError:
                    self.clear()
                    print("#########################")
                    print("##### Invalid input #####")
                    print("#########################")


            elif input_list == "q":
                    break
            
            else:
                print("#########################")
                print("##### Invalid input #####")
                print("#########################")
                