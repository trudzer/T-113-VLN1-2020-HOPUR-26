from datetime import date

class DataTest:

    def __init__(self):
        self.result_dict = {}

    def open_file(self):
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

    def get_starfsmadur(self, result_dict):
        testList = []
        self.result_dict = result_dict
        id = int(input("id: "))
        if id not in result_dict:
            nafn = input("nafn:\t\t| ")
            kennitala = input("kennitala:\t| ")
            heimilisfang = input("heimilisfang:\t| ")
            tolvupostur = input("tölvupóstur:\t| ")
            simanumer = input("símanúmer:\t| ")
            heimilissimi = input("heimilissími:\t| ")
            stadsetning = input("staðsetning:\t| ")
            print()
            result_dict[id] = nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning
            testList.append(result_dict[id])
        else:
            print()
            print("########################")
            print("##### ID þegar til #####")
            print("########################")

    def change_starfsmadur(self, result_dict):
        testList = []
        self.result_dict = result_dict
        input_number = input
        id = int(input("id: "))
        if id in result_dict:
            nafn = result_dict[id][0]
            kennitala = result_dict[id][1]
            heimilisfang = result_dict[id][2]
            tolvupostur = result_dict[id][3]
            simanumer = result_dict[id][4]
            heimilissimi = result_dict[id][5]
            stadsetning = result_dict[id][6]
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
                result_dict[id] = nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning
                testList.append(result_dict[id])
        else:
            print("\n" * 150)
            print("#######################")
            print("##### ID ekki til #####")
            print("#######################")
    
        return testList

    def eyda_starfsmanni(self, result_dict):
        self.result_dict = result_dict
        id = int(input("id:\t\t| "))
        if id in result_dict:
            result_dict.pop(id)

    def get_starfsmadur_file(self,file_stream,result_dict):
        self.result_dict = result_dict
        resultList = []
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


    def print_list(self,result_dict):
        self.result_dict = result_dict
        sorted_list = sorted(result_dict)
        print("| id: \t| nafn: \t\t\t| kennitala:\t| heimilisfang:\t\t| tölvupóstur:\t\t\t| símanúmer:\t\t| heimilissími:\t\t| staðsetning:\t\t\t|")
        print("|" + "—" * 191 +"|")
        for id in sorted_list:
            print("| {} \t| {:<22}\t| {:<12}\t| {:<20}\t| {:<22}\t| {:<14}\t| {:<14}\t| {:<16} \t\t|".format(id, result_dict[id][0], result_dict[id][1], result_dict[id][2], result_dict[id][3], result_dict[id][4], result_dict[id][5],result_dict[id][6]))


def clear():
        print("\n" * 150)


# Main
def Main():
    today = date.today()
    data1 = DataTest()
    starfsmadur_dict = {}
    id = 0
    nafn = ""
    kennitala = ""
    heimilisfang = ""
    tolvupostur = ""
    simanumer = ""
    heimilissimi = ""
    stadsetning = ""
    file_list = data1.open_file()
    input_list = input

    while input_list != "q":
        print("|" + "—" * 191 +"|")
        starfs_list = data1.get_starfsmadur_file(file_list, starfsmadur_dict)
        print("|",today,"\t|\t\t\t\t\t\t\t\t\tNaN Air\t\t\t\t\t\t\t\t\t\t|\t(Q) quit\t|")
        print("|" + "—" * 191 +"|")
        print("| 1. Starfsmenn\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
        print("| 2. Áfangastaðir\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
        print("| 3. Farartæki\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
        print("| 4. Leiga\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
        print("|" + "—" * 191 +"|")
        input_list = input("input: ")
        clear()
        if input_list == "1":
            while input_list != "b":
                data1.write_list(starfsmadur_dict)
                print("|" + "—" * 191 +"|")
                print("| Starfsmenn\t|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|\t(B) back\t|")
                print("|" + "—" * 191 +"|")
                data1.print_list(starfsmadur_dict)
                print("|" + "—" * 191 +"|")
                print("|\t(S) skrá starfsmann\t\t|\t(F) finna og breyta starfsmanni\t\t|\t(E) eyða starfsmanni\t\t|\t\t\t\t\t\t\t\t|")
                print("|" + "—" * 191 +"|")
                input_list = input("input: ")


                if input_list == "s":
                    data1.get_starfsmadur(starfsmadur_dict)
                    if id > 1:
                        data1.add_results(starfsmadur_dict, id, nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning)
                    print()
                    clear()

                if input_list == "f":
                    data1.change_starfsmadur(starfsmadur_dict)
                    if id > 1:
                        data1.add_results(starfsmadur_dict, id, nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning)
                    print()
                    clear()

                if input_list == "e":
                    data1.eyda_starfsmanni(starfsmadur_dict)
                    print()
                    clear()

                if input_list == "b":
                    clear()
                    break


#Main
if __name__ == "__main__":
    Main()