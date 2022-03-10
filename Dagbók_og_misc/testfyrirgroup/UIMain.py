from datetime import date, datetime
from LogicMain import LogicMain


class UIMain():

    def __init__(self):
        self.logic = LogicMain()
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
        print("| id: \t| nafn: \t\t\t\t| númeraplata:\t| frátekið:\t| týpa:\t| staðsetning:\t| viðhald:\t| litur:\t\t| árgerð:\t| taxi:\t| km:\t\t|\t|")
        print("|" + "—" * 191 +"|")
        for id in sorted_list:
            print("| {} \t| {:<32}\t| {:4}\t| {:<8}\t| {:<2}\t| {:<10}\t| {:<8}\t| {:<14}\t| {:<6}\t| {:<4}%\t| {:<6} KM\t|\t|".format(id, result_dict[id][1], result_dict[id][2], result_dict[id][3], result_dict[id][4], result_dict[id][5],result_dict[id][6],result_dict[id][7],result_dict[id][8],result_dict[id][9],result_dict[id][10]))


    def print_leiga_list(self,result_dict, other_dict):
        self.result_dict = result_dict
        self.other_dict = other_dict
        sorted_list = sorted(result_dict)
        print("| id: \t| nafn: \t\t\t| kennitala:\t| símanúmer:\t\t| heimilisfang:\t\t| tölvupóstur:\t\t\t| byrjun leigu:\t| endir leigu:\t| sækja:| mótekin:\t|")
        print("|" + "—" * 191 +"|")
        for id in sorted_list:
            print("| {} \t| {:<22}\t| {:4}\t| {:<14}\t| {:<16}\t| {:<28}\t| {:<8}\t| {:<6}\t| {:<3}\t| {:<3}\t\t|".format(id, result_dict[id][0], result_dict[id][1], result_dict[id][2], result_dict[id][3], result_dict[id][4],other_dict[id][6],other_dict[id][7],other_dict[id][8],other_dict[id][10]))


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
                starfsmadur_dict = {}
                afangastadir_dict = {}
                logic.get_starfsmadur_file(starfsmadur_dict)
                logic.get_afangastadir_file(afangastadir_dict)
                while input_list != "b":
                    try:
                        logic.starfsmenn_read_list(starfsmadur_dict)
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
                                    print("—" * 25)
                                    for i in afangastadir_dict:
                                        counter += 1
                                        print(counter, "-", afangastadir_dict[i][0])
                                    print("—" * 25)
                                    input_list = int(input("staðsetning:\t| "))
                                    counter = 0
                                    for i in afangastadir_dict:
                                        counter += 1
                                        if input_list == counter:
                                            stadsetning = afangastadir_dict[i][0]

                                    logic.get_starfsmadur(starfsmadur_dict, id, nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning)
                                    if id > 1:
                                        logic.add_starfsmenn_results(starfsmadur_dict, id, nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning)
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
                                    while input_number != "b":
                                        print()
                                        print("|" + "—" * 191 +"|")
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
                                            print("—" * 25)
                                            for i in afangastadir_dict:
                                                counter += 1
                                                print(counter, "-", afangastadir_dict[i][0])
                                            print("—" * 25)
                                            input_list = int(input("staðsetning:\t| "))
                                            counter = 0
                                            for i in afangastadir_dict:
                                                counter += 1
                                                if input_list == counter:
                                                    stadsetning = afangastadir_dict[i][0]
                                        else:
                                            print("#########################")
                                            print("##### Invalid input #####")
                                            print("#########################")
                                    logic.get_starfsmadur(starfsmadur_dict, id, nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning)
                                    if id > 1:
                                        logic.add_starfsmenn_results(starfsmadur_dict, id, nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning)
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
                            if id in starfsmadur_dict:
                                logic.eyda_element(starfsmadur_dict, id)
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
                afangastadir_dict = {}
                logic.get_afangastadir_file(afangastadir_dict)
                try:
                    while input_list != "b":
                        logic.afangastadir_read_list(afangastadir_dict)
                        print("|" + "—" * 191 +"|")
                        print("|\t", str_today, "\t|\t\tÁfangastaðir\t\t|\t\t\t\t\t\t\t\t\t\t\t\t\t|\t(B) back\t|")
                        print("|" + "—" * 191 +"|")
                        self.print_afangastadir_list(afangastadir_dict)
                        print("|" + "—" * 191 +"|")
                        print("|\t(S) skrá áfangastað\t\t|\t(F) finna og breyta áfangastað\t\t|\t(E) eyða áfangastað\t\t|\t\t\t\t\t\t\t\t|")
                        print("|" + "—" * 191 +"|")
                        input_list = input("input: ")


                        if input_list == "s":
                            try:
                                id = int(input("id: "))
                                if id not in afangastadir_dict:
                                    borg = input("borg:\t\t| ")
                                    land = input("land:\t\t| ")
                                    flugvollur = input("flugvöllur:\t| ")
                                    simanumer = input("símanúmer:\t| ")
                                    print("—" * 25)
                                    print("1. 08:00\n2. 09:00\n3. 10:00\n4. 11:00")
                                    print("—" * 25)
                                    time_imput1 = int(input("input: "))
                                    if time_imput1 == 1:
                                        open_time = "08:00"
                                    elif time_imput1 == 2:
                                        open_time = "09:00"
                                    elif time_imput1 == 3:
                                        open_time = "10:00"
                                    elif time_imput1 == 4:
                                        open_time = "11:00"
                                    print()
                                    print("—" * 25)
                                    print("1. 20:00\n2. 21:00\n3. 22:00\n4. 23:00")
                                    print("—" * 25)
                                    time_imput2 = int(input("input: "))
                                    if time_imput2 == 1:
                                        close_time = "20:00"
                                    elif time_imput2 == 2:
                                        close_time = "21:00"
                                    elif time_imput2 == 3:
                                        close_time = "22:00"
                                    elif time_imput2 == 4:
                                        close_time = "23:00"
                                    opnunartimi = "{}-{}".format(open_time, close_time)
                                    logic.get_afangastadir(afangastadir_dict, id, borg, land, flugvollur, simanumer, opnunartimi)
                                    if id > 1:
                                        logic.add_afangastadir_results(afangastadir_dict, id, borg, land, flugvollur, simanumer, opnunartimi)
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
                                if id in afangastadir_dict:
                                    borg = afangastadir_dict[id][0]
                                    land = afangastadir_dict[id][1]
                                    flugvollur = afangastadir_dict[id][2]
                                    simanumer = afangastadir_dict[id][3]
                                    opnunartimi = afangastadir_dict[id][4]
                                    while input_number != "b":
                                        print()
                                        print("|" + "—" * 191 +"|")
                                        print("| 1. borg", "\t"*23 + "|\n| 2. land", "\t"*23 + "|\n| 3. flugvöllur", "\t"*22 + "|\n| 4. símanúmer", "\t"*23 + "|\n| 5. opnunartími", "\t"*22 + "|")
                                        print("|" + "—" * 191 +"|")
                                        print()
                                        input_number = input("input: ")
                                        if input_number == "1":
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
                                        
                                    logic.get_afangastadir(afangastadir_dict, id, borg, land, flugvollur, simanumer, opnunartimi)
                                    if id > 1:
                                        logic.add_afangastadir_results(afangastadir_dict, id, borg, land, flugvollur, simanumer, opnunartimi)
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
                                logic.eyda_element(afangastadir_dict, id)
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
                farartaeki_dict = {}
                afangastadir_dict = {}
                logic.get_farartaeki_file(farartaeki_dict)
                logic.get_afangastadir_file(afangastadir_dict)
                try:
                    while input_list != "b":
                        logic.farartaeki_read_list(farartaeki_dict)
                        print("|" + "—" * 191 +"|")
                        print("|\t", str_today, "\t|\t\tFarartaeki\t\t|\t\t\t\t\t\t\t\t\t\t\t\t\t|\t(B) back\t|")
                        print("|" + "—" * 191 +"|")
                        self.print_farartaeki_list(farartaeki_dict)
                        print("|" + "—" * 191 +"|")
                        print("|\t(S) skrá farartæki\t\t|\t(F) finna og breyta farartæki\t\t|\t(E) eyða farartæki\t\t|\t\t\t\t\t\t\t\t|")
                        print("|" + "—" * 191 +"|")
                        input_list = input("input: ")


                        if input_list == "s":
                            try:
                                id = int(input("id: "))
                                if id not in farartaeki_dict:
                                    nafn = input("nafn:\t\t| ")
                                    numeraplata = input("númeraplata:\t| ")
                                    fratekid = input("frátekið:\t| ")
                                    print("—" * 25)
                                    print("1. A\n2. B\n3. C\n4. D")
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
                                    counter = 0
                                    for i in afangastadir_dict:
                                        counter += 1
                                        print(counter, "-", afangastadir_dict[i][0])
                                    print("—" * 25)
                                    input_list = int(input("staðsetning:\t| "))
                                    counter = 0
                                    for i in afangastadir_dict:
                                        counter += 1
                                        if input_list == counter:
                                            stadsetning = afangastadir_dict[i][0]
                                            area = input_list
                                    vidhald = input("viðhald:\t| ")
                                    litur = input("litur:\t\t| ")
                                    argerd = input("árgerð:\t\t| ")
                                    taxi = input("taxi:\t\t| ")
                                    km = input("km:\t\t| ")
                                    logic.get_farartaeki(farartaeki_dict, id, area, nafn, numeraplata, fratekid, typa, stadsetning, vidhald, litur, argerd, taxi, km)
                                    if id > 1:
                                        logic.add_farartaeki_results(farartaeki_dict, id, area, nafn, numeraplata, fratekid, typa, stadsetning, vidhald, litur, argerd, taxi, km)
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
                                    area = farartaeki_dict[id][0]
                                    nafn = farartaeki_dict[id][1]
                                    numeraplata = farartaeki_dict[id][2]
                                    fratekid = farartaeki_dict[id][3]
                                    typa = farartaeki_dict[id][4]
                                    stadsetning = farartaeki_dict[id][5]
                                    vidhald = farartaeki_dict[id][6]
                                    litur = farartaeki_dict[id][7]
                                    argerd = farartaeki_dict[id][8]
                                    taxi = farartaeki_dict[id][9]
                                    km = farartaeki_dict[id][10]
                                    while input_number != "b":
                                        print()
                                        print("|" + "—" * 191 +"|")
                                        print("| 1. nafn", "\t"*23 + "|\n| 2. númeraplata", "\t"*22 + "|\n| 3. frátekið", "\t"*23 + "|\n| 4. týpa", "\t"*23 + "|\n| 5. staðsetning", "\t"*22 + "|\n| 6. viðhald", "\t"*23 + "|\n| 7. litur", "\t"*23 + "|\n| 8. árgerð", "\t"*23 + "|\n| 9. taxi", "\t"*23 + "|\n| 10. km", "\t"*23 + "|")
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
                                            print("—" * 25)
                                            print("1. A\n2. B\n3. C\n4. D")
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
                                            print("—" * 25)
                                        elif input_number == "5":
                                            print("—" * 25)
                                            counter = 0
                                            for i in afangastadir_dict:
                                                counter += 1
                                                print(counter, "-", afangastadir_dict[i][0])
                                            print("—" * 25)
                                            input_list = int(input("staðsetning:\t| "))
                                            counter = 0
                                            for i in afangastadir_dict:
                                                counter += 1
                                                if input_list == counter:
                                                    stadsetning = afangastadir_dict[i][0]
                                                    area = input_list
                                        elif input_number == "6":
                                            vidhald = input("| viðhald:\t| ")
                                        elif input_number == "7":
                                            litur = input("| litur:\t| ")
                                        elif input_number == "8":
                                            argerd = input("| árgerð:\t| ")
                                        elif input_number == "9":
                                            taxi = input("| taxi:\t| ")
                                        elif input_number == "10":
                                            km = input("| km:\t| ")
                                        else:
                                            print("#########################")
                                            print("##### Invalid input #####")
                                            print("#########################")
                                    logic.get_farartaeki(farartaeki_dict, id, area, nafn, numeraplata, fratekid, typa, stadsetning, vidhald, litur, argerd, taxi, km)
                                    if id > 1:
                                        logic.add_farartaeki_results(farartaeki_dict, id, area, nafn, numeraplata, fratekid, typa, stadsetning, vidhald, litur, argerd, taxi, km)
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
                                logic.eyda_element(farartaeki_dict, id)
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
                leiga_dict = {}
                leigjandi_dict = {}
                farartaeki_dict = {}
                starfsmadur_dict = {}
                afangastadir_dict = {}
                logic.get_leiga_file(leiga_dict)
                logic.get_leigjandi_file(leigjandi_dict)
                logic.get_farartaeki_file(farartaeki_dict)
                logic.get_starfsmadur_file(starfsmadur_dict)
                logic.get_afangastadir_file(afangastadir_dict)
                try:
                    while input_list != "b":
                        logic.leiga_read_list(leiga_dict)
                        logic.leigjandi_read_list(leigjandi_dict)
                        print("|" + "—" * 191 +"|")
                        print("|\t", str_today, "\t|\t\tLeiga\t\t\t|\t\t\t\t\t\t\t\t\t\t\t\t\t|\t(B) back\t|")
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
                                    for i in farartaeki_dict:
                                        counter += 1
                                        print("{}. {:<32}\t{:<10}\t{:<10}\t{:<10}".format(counter, farartaeki_dict[i][1], farartaeki_dict[i][3], farartaeki_dict[i][4], farartaeki_dict[i][5]))
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
                                            id_afangastadir = farartaeki_dict[i][0]
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
                                    logic.get_leiga(leiga_dict, id_samningur, id_leigjandi, id_starfsmadur, kostnadur, id_farartaeki,id_afangastadir, samningur_stofnadur, byrjun_samningur, endir_samningur, pickup_timi, rukkadur, motaka)
                                    logic.get_leigjandi(leigjandi_dict, id, nafn, kennitala,simanumer,heimilisfang,tolvupostur,typa)
                                    if id > 1:
                                        logic.add_leiga_results(leiga_dict, id_samningur, id_leigjandi, id_starfsmadur, kostnadur, id_farartaeki,id_afangastadir, samningur_stofnadur, byrjun_samningur, endir_samningur, pickup_timi, rukkadur, motaka)
                                        logic.add_leigjandi_results(leigjandi_dict, id, nafn, kennitala,simanumer,heimilisfang,tolvupostur,typa)
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
                                        print("|" + "—" * 191 +"|")
                                        print("| 1. nafn", "\t"*23 + "|\n| 2. símanumer", "\t"*23 + "|\n| 3. heimilisfang", "\t"*22 + "|\n| 4. tölvupóstur", "\t"*22 + "|\n| 5. byrjun samningur", "\t"*22 + "|\n| 6. endir samningur", "\t"*22 + "|\n| 7. sækja klukkan", "\t"*22 + "|\n| 8. mótaka", "\t"*23 + "|\n| 9. breyta bíl","\t"*22 + "|")
                                        print("|" + "—" * 191 +"|")
                                        print()
                                        input_number = input("input: ")
                                        if input_number == "1":
                                            nafn = input("| nafn:\t| ")
                                        elif input_number == "2":
                                            simanumer = input("| símanumer:\t\t| ")
                                        elif input_number == "3":
                                            heimilisfang = input("| heimilisfang:\t| ")
                                        elif input_number == "4":
                                             tolvupostur = input("| tölvupóstur:\t| ")
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
                                            print("| 1. Já\n| 2. Nei\n| 3. Skil")
                                            skil_list = int(input("| mótaka: "))
                                            if skil_list == 1:
                                                motaka = "Já"
                                            if skil_list == 2:
                                                motaka = "Nei"
                                            if skil_list == 3:
                                                motaka = "Skil"
                                            print("—" * 25)
                                        elif input_number == "9":
                                            print()
                                            print("—" * 25)
                                            counter = 0
                                            for i in farartaeki_dict:
                                                counter += 1
                                                print(counter, "-", farartaeki_dict[i][1])
                                            print("—" * 25)
                                            id_farartaeki = int(input("| farartæki: "))
                                            print()
                                            print("—" * 25)
                                            counter = 0
                                        else:
                                            print("#########################")
                                            print("##### Invalid input #####")
                                            print("#########################")

                                    logic.get_leiga(leiga_dict, id_samningur, id_leigjandi, id_starfsmadur, kostnadur, id_farartaeki,id_afangastadir, samningur_stofnadur, byrjun_samningur, endir_samningur, pickup_timi, rukkadur, motaka)
                                    logic.get_leigjandi(leigjandi_dict, id, nafn, kennitala,simanumer,heimilisfang,tolvupostur,typa)
                                    if id > 1:
                                        logic.add_leiga_results(leiga_dict, id_samningur, id_leigjandi, id_starfsmadur, kostnadur, id_farartaeki,id_afangastadir, samningur_stofnadur, byrjun_samningur, endir_samningur, pickup_timi, rukkadur, motaka)
                                        logic.add_leigjandi_results(leigjandi_dict, id, nafn, kennitala,simanumer,heimilisfang,tolvupostur,typa)
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
                                logic.eyda_element(leigjandi_dict, id)
                                logic.eyda_element(leiga_dict, id)
                                self.clear()
                            else:
                                self.clear()
                                print("#######################")
                                print("##### ID ekki til #####")
                                print("#######################")

                        elif input_list == "p":
                            try:
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
                                            if id_farartaeki == counter:
                                                id_afangastadir = farartaeki_dict[i][0]
                                                farartaeki = farartaeki_dict[i][1]
                                                numeraplata = farartaeki_dict[i][2]
                                                fratekid = farartaeki_dict[i][3]
                                                typa = farartaeki_dict[i][4]
                                                afangastadur = farartaeki_dict[i][5]
                                                vidhald = farartaeki_dict[i][6]
                                                litur = farartaeki_dict[i][7]
                                                argerd = farartaeki_dict[i][8]
                                                taxi = farartaeki_dict[i][9]
                                                km = farartaeki_dict[i][10]
                                            
                                            for j in afangastadir_dict:
                                                if j == id_afangastadir:
                                                    borg = afangastadir_dict[j][0]
                                                    land = afangastadir_dict[j][1]
                                                    flugvollur = afangastadir_dict[j][2]
                                                    simanumer = afangastadir_dict[j][3]
                                                    opnunartimi = afangastadir_dict[j][4]


                                        print("|" + "—" * 191 +"|")
                                        print("|\t", str_today, "\t|\t\tLeiga\t\t\t|\t\t\t\t\t\t\t\t\t\t\t\t\t|\t(B) back\t|")
                                        print("|" + "—" * 191 +"|")
                                        print("|\t\t\t\tEinstaklingur\t\t\t|\t\t\tBifreið\t\t\t\t\t|\t\t\tStaðsetning\t\t\t\t|")
                                        print("|" + "—" * 191 +"|")
                                        print("|\tNafn:\t\t\t{:<22}\t\t| tegund:\t\t{:<32}\t| áfangastaður:\t\t{:<14}\t\t\t\t|".format(leigjandi_dict[id][0],farartaeki,borg))
                                        print("|" + "—" * 191 +"|")
                                        print("|\tSímanúmer:\t\t{:<18}\t\t| númeraplata:\t\t{:<8}\t\t\t\t| land:\t\t\t{:<14}\t\t\t\t|".format(leigjandi_dict[id][2],numeraplata,land))
                                        print("|" + "—" * 191 +"|")
                                        print("|\tHeimilisfang:\t\t{:<20}\t\t| frátekið:\t\t{:<6}\t\t\t\t\t| flugvöllur:\t\t{:<24}\t\t|".format(leigjandi_dict[id][3],fratekid,flugvollur))
                                        print("|" + "—" * 191 +"|")
                                        print("|\tTölvupóstur:\t\t{:<24}\t| týpa:\t\t\t{:<4}\t\t\t\t\t| símanúmer:\t\t{:<16}\t\t\t|".format(leigjandi_dict[id][4],typa,simanumer))
                                        print("|" + "—" * 191 +"|")
                                        print("|\tFrátekið tímabil:\t{:<8}/{:<8}\t\t| áfangastaður:\t\t{:<18}\t\t\t| opnunartími:\t\t{:<18}\t\t\t|".format(leiga_dict[id][6],leiga_dict[id][7],afangastadur,opnunartimi))
                                        print("|" + "—" * 191 +"|")
                                        print("|\tAfhending:\t\t{:<8}\t\t\t| viðhald:\t\t{:<8}\t\t\t\t|\t\t\t\t\t\t\t\t|".format(leiga_dict[id][8],vidhald))
                                        print("|" + "—" * 191 +"|")
                                        print("|\tMótaka:\t\t\t{:<4}\t\t\t\t| litur:\t\t{:<16}\t\t\t|\t\t\t\t\t\t\t\t|".format(leiga_dict[id][10],litur))
                                        print("|" + "—" * 191 +"|")
                                        print("|\tUpphæð + taxi:\t\t{:<6} kr\t\t\t| árgerð:\t\t{:<6}\t\t\t\t\t|\t\t\t\t\t\t\t\t|".format(leiga_dict[id][2],argerd))
                                        print("|" + "—" * 191 +"|")
                                        print("|\t\t\t\t\t\t\t\t| taxi:\t\t\t{}%\t\t\t\t\t|\t\t\t\t\t\t\t\t|".format(taxi))
                                        print("|" + "—" * 191 +"|")
                                        print("|\t\t\t\t\t\t\t\t| kílómetrar keyrðir:\t{:<6} KM\t\t\t\t|\t\t\t\t\t\t\t\t|".format(km))
                                        print("|" + "—" * 191 +"|")
                                        input_number = input("input: ")
                                        self.clear()
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
                