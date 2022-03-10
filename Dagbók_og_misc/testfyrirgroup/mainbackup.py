from datetime import date

class DataMain:
    def __init__(self):
        print("Inside data")

    def open_starfsmenn_file(self):
        try:
            file_object = open("starfsmenn.txt", 'r', encoding='utf8')
            return file_object
        except FileNotFoundError:
            return None

    def write_list(self, result_dict):
        self.result_dict = result_dict
        resultList = []
        try:
            file_object = open("starfsmenn.txt", 'w', encoding='utf8')
            for id in result_dict:
                nafn = result_dict[id][0]
                kennitala = result_dict[id][1]
                heimilisfang = result_dict[id][2]
                tolvupostur = result_dict[id][3]
                simanumer = result_dict[id][4]
                heimilissimi = result_dict[id][5]
                stadsetning = result_dict[id][6]
                if len(result_dict) > 1:
                    file_object.writelines(str("{},{},{},{},{},{},{},{},\n".format(id,nafn,kennitala,heimilisfang,tolvupostur,simanumer,heimilissimi,stadsetning)))
            file_object.close()
        except FileNotFoundError:
            return None

    def open_afangastadir_file(self):
        try:
            file_object = open("./files/afangastadir.txt", 'r', encoding='utf8')
            return file_object
        except FileNotFoundError:
            return None

    def write_afangastadir_list(self, result_dict):
        self.result_dict = result_dict
        resultList = []
        try:
            file_object = open("./files/afangastadir.txt", 'w', encoding='utf8')
            for id in result_dict:
                borg = result_dict[id][0]
                land = result_dict[id][1]
                flugvollur = result_dict[id][2]
                simanumer = result_dict[id][3]
                opnunartimi = result_dict[id][4]
                if len(result_dict) > 1:
                    file_object.writelines(str("{},{},{},{},{},{},\n".format(id,borg,land,flugvollur,simanumer,opnunartimi)))
            file_object.close()
        except FileNotFoundError:
            return None

class LogicMain:

    def __init__(self):
        self.data = DataMain()

    def get_starfsmadur(self, result_dict, id, nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning):
        result_list = []
        self.result_dict = result_dict
        self.id = id
        self.nafn = nafn
        self.kennitala = kennitala
        self.heimilisfang = heimilisfang
        self.tolvupostur = tolvupostur
        self.simanumer = simanumer
        self.heimilissimi = heimilissimi
        self.stadsetning = stadsetning
        result_dict[id] = nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning
        result_list.append(result_dict[id])
    
        return result_list

    def eyda_starfsmanni(self, result_dict, id):
        self.result_dict = result_dict
        self.id = id
        result_dict.pop(id)

    def starfsmenn_read_list(self, result_dict):
        self.data.write_list(result_dict)

    def get_starfsmadur_file(self, result_dict):
        self.result_dict = result_dict
        resultList = []
        file_stream = self.data.open_starfsmenn_file()
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
            result_dict[id] = nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning
        for id in result_dict:
            resultList.append(result_dict[id])
        return resultList
    
    
    def add_results(self, result_dict, id, nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning):
        self.result_dict = result_dict
        result_dict[id] = nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning

    def get_afangastadir(self, result_dict, id, borg, land, flugvollur, simanumer, opnunartimi):
            result_list = []
            self.result_dict = result_dict
            self.id = id
            self.borg = borg
            self.land = land
            self.flugvollur = flugvollur
            self.simanumer = simanumer
            self.opnunartimi = opnunartimi
            result_dict[id] = borg, land, flugvollur, simanumer, opnunartimi
            result_list.append(result_dict[id])
    
            return result_list

    def eyda_afangastad(self, result_dict, id):
        self.result_dict = result_dict
        self.id = id
        result_dict.pop(id)

    def afangastadir_read_list(self, result_dict):
        self.data.write_afangastadir_list(result_dict)

    def get_afangastadir_file(self, result_dict):
        self.result_dict = result_dict
        resultList = []
        file_stream = self.data.open_afangastadir_file()
        for i in file_stream:
            i = i.split(",")
            id = int(i[0])
            borg = i[1]
            land = i[2]
            flugvollur = i[3] 
            simanumer = i[4] 
            opnunartimi = i[5]
            result_dict[id] = borg, land, flugvollur, simanumer, opnunartimi
        for id in result_dict:
            resultList.append(result_dict[id])
        return resultList
    
    
    def add_afangastadir_results(self, result_dict, id, borg, land, flugvollur, simanumer, opnunartimi):
        self.result_dict = result_dict
        result_dict[id] = borg, land, flugvollur, simanumer, opnunartimi


# Main
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


    def ui_loop(self):
        logic = self.logic
        today = date.today()
        input_list = input

        while input_list != "q":
            print("|" + "—" * 191 +"|")
            print("|",today,"\t|\t\t\t\t\t\t\t\t\tNaN Air\t\t\t\t\t\t\t\t\t\t|\t(Q) quit\t|")
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
                logic.get_starfsmadur_file(starfsmadur_dict)
                while input_list != "b":
                    logic.starfsmenn_read_list(starfsmadur_dict)
                    print("|" + "—" * 191 +"|")
                    print("| Starfsmenn\t|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|\t(B) back\t|")
                    print("|" + "—" * 191 +"|")
                    self.print_starfsmenn_list(starfsmadur_dict)
                    print("|" + "—" * 191 +"|")
                    print("|\t(S) skrá starfsmann\t\t|\t(F) finna og breyta starfsmanni\t\t|\t(E) eyða starfsmanni\t\t|\t\t\t\t\t\t\t\t|")
                    print("|" + "—" * 191 +"|")
                    input_list = input("input: ")


                    if input_list == "s":
                        id = int(input("id: "))
                        if id not in starfsmadur_dict:
                            nafn = input("nafn:\t\t| ")
                            kennitala = input("kennitala:\t| ")
                            heimilisfang = input("heimilisfang:\t| ")
                            tolvupostur = input("tölvupóstur:\t| ")
                            simanumer = input("símanúmer:\t| ")
                            heimilissimi = input("heimilissími:\t| ")
                            stadsetning = input("staðsetning:\t| ")
                            logic.get_starfsmadur(starfsmadur_dict, id, nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning)
                            if id > 1:
                                logic.add_results(starfsmadur_dict, id, nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning)
                                self.clear()
                        else:
                            self.clear()
                            print("########################")
                            print("##### ID þegar til #####")
                            print("########################")
                        
                        

                    if input_list == "f":
                        input_number = input
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
                                if input_number == "2":
                                    tolvupostur = input("| tölvupóstur:\t| ")
                                if input_number == "3":
                                    simanumer = input("| símanúmer:\t| ")
                                if input_number == "4":
                                    heimilissimi = input("| heimilissími:\t| ")
                                if input_number == "5":
                                    stadsetning = input("| staðsetning:\t| ")
                            logic.get_starfsmadur(starfsmadur_dict, id, nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning)
                            if id > 1:
                                logic.add_results(starfsmadur_dict, id, nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning)
                                self.clear()
                        else:
                            self.clear()
                            print("#######################")
                            print("##### ID ekki til #####")
                            print("#######################")
                        

                    if input_list == "e":
                        id = int(input("id:\t\t| "))
                        if id in starfsmadur_dict:
                            logic.eyda_starfsmanni(starfsmadur_dict, id)
                            self.clear()
                        else:
                            self.clear()
                            print("#######################")
                            print("##### ID ekki til #####")
                            print("#######################")

                    if input_list == "b":
                        self.clear()
                        break

            elif input_list == "2":
                afangastadir_dict = {}
                logic.get_afangastadir_file(afangastadir_dict)
                while input_list != "b":
                    logic.afangastadir_read_list(afangastadir_dict)
                    print("|" + "—" * 191 +"|")
                    print("|", today, "\t| Áfangastaðir\t|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|\t(B) back\t|")
                    print("|" + "—" * 191 +"|")
                    self.print_afangastadir_list(afangastadir_dict)
                    print("|" + "—" * 191 +"|")
                    print("|\t(S) skrá áfangastað\t\t|\t(F) finna og breyta áfangastað\t\t|\t(E) eyða áfangastað\t\t|\t\t\t\t\t\t\t\t|")
                    print("|" + "—" * 191 +"|")
                    input_list = input("input: ")


                    if input_list == "s":
                        id = int(input("id: "))
                        if id not in afangastadir_dict:
                            borg = input("borg:\t\t| ")
                            land = input("land:\t\t| ")
                            flugvollur = input("flugvöllur:\t| ")
                            simanumer = input("símanúmer:\t| ")
                            opnunartimi = input("opnunartími:\t| ")
                            logic.get_afangastadir(afangastadir_dict, id, borg, land, flugvollur, simanumer, opnunartimi)
                            if id > 1:
                                logic.add_afangastadir_results(afangastadir_dict, id, borg, land, flugvollur, simanumer, opnunartimi)
                                self.clear()
                        else:
                            self.clear()
                            print("########################")
                            print("##### ID þegar til #####")
                            print("########################")
                        

                    if input_list == "f":
                        input_number = input
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
                                if input_number == "2":
                                    land = input("| land:\t\t| ")
                                if input_number == "3":
                                    flugvollur = input("| flugvollur:\t| ")
                                if input_number == "4":
                                    simanumer = input("| simanumer:\t| ")
                                if input_number == "5":
                                    opnunartimi = input("| opnunartimi:\t| ")
                            logic.get_afangastadir(afangastadir_dict, id, borg, land, flugvollur, simanumer, opnunartimi)
                            if id > 1:
                                logic.add_afangastadir_results(afangastadir_dict, id, borg, land, flugvollur, simanumer, opnunartimi)
                                self.clear()
                        else:
                            self.clear()
                            print("#######################")
                            print("##### ID ekki til #####")
                            print("#######################")
                        

                    if input_list == "e":
                        id = int(input("id:\t\t| "))
                        if id in afangastadir_dict:
                            logic.eyda_afangastad(afangastadir_dict, id)
                            self.clear()
                        else:
                            self.clear()
                            print("#######################")
                            print("##### ID ekki til #####")
                            print("#######################")

                    if input_list == "b":
                        self.clear()
                        break


            elif input_list == "q":
                    break
            
            else:
                print("#########################")
                print("##### Invalid input #####")
                print("#########################")


#main
if __name__ == "__main__":
    ui = UIMain()