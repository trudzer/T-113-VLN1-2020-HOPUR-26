from logic.LogicMain import LogicMain 


class UIMain:
    def __init__(self):
        print("Inside UI")
        self.logic = LogicMain()
        self.ui_loop()
    
    def ui_loop(self):
        while True:
            print("\n1. Starfsmenn\n2. Farartæki\n3. Áfangastaðir \n4. Leiga \n5. Prenta útfærslur")
            command = input("Input: ")
            command = command.lower()
            if command == "1":
                while command != "b":
                    results = self.logic.all_employees() #results is a dictionary
                    position = self.logic.position()
                    print("\nStarfsmenn: ")
                    
                    #print(employee, end='')
                    #employee_info = results[employee]
                    sorted_list = {k: v for k, v in sorted(results.items(), key= lambda v:[1])} #Sorted by id
                    print(sorted_list)
                    print("|\t| id: \t| nafn: \t\t\t| kennitala:\t| heimilisfang:\t\t| tölvupóstur:\t\t\t| símanúmer:\t\t| heimilissími:\t\t| staðsetning:\t\t|")
                    print("|" + "-" * 191 +"|")
                    for id in sorted_list:
                        print("| {}.\t| {:<22}\t| {:<12}\t| {:<20}\t| {:<22}\t| {:<14}\t| {:<14}\t| {:<16} \t|".format(id, results[id][0], results[id][1], results[id][2], results[id][3], results[id][4], results[id][5],results[id][6]))
                        print("|" + "-" * 191 +"|")
                        
                    print("|\t (s) skrá starfsmann\t| (f) breyta starfsmanni\t| (e) eyða starfsmanni\t| (b) til baka \t|")
                    command = input("input: ").lower()
                    
                    if command == "s":
                        print("Skrá starfmann")
                        self.logic.create_employee()
                    
                    elif command == "f" + position:
                        print("Breyta starfsmanni")
                        self.logic.change_employee()
                    
                    elif command == "e":
                        print("Eyða starfsmanni")
                        self.logic.delete_employee()
                    
                    elif command == "b":
                        break


            elif command == "2":
                while command != "b":
                    results = self.logic.all_vehicles()
                    position = self.logic.position()
                    print("\nFarartæki: ")

                    sorted_list = {k: v for k, v in sorted(results.items(), key= lambda v:[1])} #Sorted by id
                    print("|\t| id: \t| tegund: \t\t\t| bílaplata:\t| frátekið:\t\t| staðsetning:\t\t\t| viðhald:\t\t| litur:\t\t| árgerð:\t\t| taxi:\t\t| KM:\t\t|")
                    print("|" + "-" * 191 +"|")
                    for id in sorted_list:
                        print("| {}.\t| {:<22}\t| {:<12}\t| {:<20}\t| {:<22}\t| {:<14}\t| {:<14}\t| {:<16} \t| {:<16} \t| {:<16} \t| {:<16} \t|".format(id, results[id][0], results[id][1], results[id][2], results[id][3], results[id][4], results[id][5], results[id][6], results[id][7], results[id][8], results[id][9]))
                        print("|" + "-" * 191 +"|")
                     

                    #for vehicle in results:
                    #    print(vehicle)
                    
                    command = input("input: ").lower()
                    
                    if command == "s":
                        print("Skrá farartæki")
                        self.logic.create_vehicle()
                    
                    elif command == "f" + position:
                        print("Breyta farartæki")
                        self.logic.change_vehicle()
                    
                    elif command == "e":
                        print("Eyða farartæki")
                        self.logic.delete_vehicle()
                    
                    elif command == "b":
                        break
            

            elif command == "3":
                while command != "b":
                    results = self.logic.all_destinations()
                    position = self.logic.position()
                    print("\nÁfangastaðir: ")

                    sorted_list = {k: v for k, v in sorted(results.items(), key= lambda v:[1])} #Sorted by id
                    print("|\t| id: \t| flugvöllur: \t| símanúmer:\t| opnunartímar:\t\t| staðsetning:\t|")
                    print("|" + "-" * 191 +"|")
                    for id in sorted_list:
                        print("| {}.\t| {:<22}\t| {:<12}\t| {:<20}\t| {:<22}\t|".format(id, results[id][0], results[id][1], results[id][2], results[id][3]))
                        print("|" + "-" * 191 +"|")
                     

                    #for locations in results:
                    #    print(locations)
                    command = input("input: ").lower()
                    
                    if command == "s":
                        print("Skrá áfangastað")
                        self.logic.create_location()
                    
                    elif command == "f" + position:
                        print("Breyta áfangastað")
                        self.logic.change_location()
                    
                    elif command == "e":
                        print("Eyða áfangastað")
                        self.logic.delete_location()
                    
                    elif command == "b":
                        break
            
            
            elif command == "4":
                while command != "b":
                    results = self.logic.all_contracts()
                    position = self.logic.position()
                    print("\nLeiga: ")
                    
                    for contracts in results:
                        print(contracts)
                    command = input("input: ").lower()
                    
                    if command == "s":
                        print("Skrá leigu")
                        self.logic.create_contracts()
                    
                    elif command == "f" + position:
                        print("Breyta leigu")
                        self.logic.change_contracts()
                    
                    elif command == "e":
                        print("Eyða leigu")
                        self.logic.delete_contracts()
                    
                    elif command == "p" + position:
                        print("Prenta leigu")
                        self.logic.print_contracts()
                        command = input("input: ")
                        
                        if command == "b":
                            break
                        
                        else:
                            print("Invalid input")
                    
                    elif command == "b":
                        break
            
            
            elif command == "5":
                while command != "b":
                    print("\n1. Yfirlit yfir tekjum (flokkað eftir áfangastöðum) \n2. Yfirlit yfir nýtingu farartækja \n3. Yfirlit yfir reikninga á ákveðnu tímabili  (flokkað eftir viðskiptavinum)")
                    command = input("Input: ")

                    if command == "1":
                        while command != "b":
                            date_check = self.logic.date_check()
                            print("Prenta útfærslur")
                            print("Tímabil: ")
                            command = input("input: ")
                            
                            if date_check == True:
                                results = self.logic.income_overview()
                                
                                for income_overview in results:
                                    print(income_overview)
                                command = input("input: ")
                                
                                if command == "b":
                                    break
                                
                                else:
                                    print("Invalid input")

                            elif command == "b":
                                break
                            
                            else:
                                print("Invalid date")

                    elif command == "2":
                        print("Yfirlit yfir nýtingu farartækja")
                        results = self.logic.utilization_of_vehicles()
                        
                        for utilization_of_vehicles in results:
                            print(utilization_of_vehicles)
                        command = input("input: ")

                        if command == "b":
                            break
                        
                        else:
                            print("Invalid input")
                            
                    elif command == "3":
                        while command != "b":
                            print("Yfirlit yfir reikninga á ákveðnu tímabili (flokkað eftir viðskiptavinum)")
                            date_check = self.logic.date_check()
                            print("Prenta útfærslur")
                            print("Tímabil: ")
                            command = input("input: ")
                            
                            if date_check == True:
                                results = self.logic.account_overview()
                                
                                for account_overview in results:
                                    print(account_overview)
                                command = input("input: ")

                                if command == "b":
                                    break
                                
                                else:
                                    print("Invalid input")
                            
                            elif command == "b":
                                break

                            else:
                                print("Invalid date")

                    elif command == "b":
                        break
            
            
            elif command == "q":
                break
            
            else:
                print("Invalid command, try again")
