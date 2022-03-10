
import os
from models.Employee import Employee

class DataMain:
    def __init__(self):

        print("Inside data")

    def GetData2(self, data, ID):
        '''Þessi breyta tekur inn frá GetData og leitar að ID-inu til þess að finna rétta hlutin til þess að búta niður í lista og senda upp'''
        for i in data:
                i = i.split(',')
                i.pop(-1)
                # við notum pop hérna því að split var alltaf að búa til auka breytu í endan svo við þurfum alltaf að taka út eina breytu í listanum
                if ID[0] == i[0]:
                    return i

    def GetData(self, ID = []):
        '''GetData er function sem tekur á móti lista sem er með ID og tegund, það leitar að hvaða tegund að skrá sem notandin vill opna og sendir file_streamið að GetData2'''
        if ID[1] == 'employee':
            data = open('data/data/starfsmenn.txt','r', encoding='utf-8')
            data = list(data)
            answer = self.GetData2(data, ID)
        # við berum saman type-inu frá ID listanum og förum svo inn og sækjum skrána og sendum file-streamið í GetData2 sem mun gefa okkur réttan lista af persónu eða öðru til þess að senda í logic main
        elif ID[1] == 'vehicle':
            data = open('data/data/farartaeki.txt','r', encoding='utf-8')
            data = list(data)
            answer = self.GetData2(data, ID)
        elif ID[1] == 'contract':
            data = open('data/data/leiga.txt','r', encoding='utf-8')
            data = list(data)
            answer = self.GetData2(data, ID)
        elif ID[1] == 'locations':
            data = open('data/data/afangastadir.txt','r', encoding='utf-8')
            data = list(data)
            answer = self.GetData2(data, ID)
        elif ID[1] == 'customer':
            data = open('data/data/leigjandi.txt','r', encoding='utf-8')
            data = list(data)
            answer = self.GetData2(data, ID)
        else:
            answer = None
        return answer


    def get_all_employees(self):
        '''þetta function opnar file_streamið og texta skjalið sem heitið á functionið er að fókusa á og sendir það upp til LogicMain fyrir processing '''
        file_stream = open('data/data/starfsmenn.txt', 'r', encoding='utf-8')
        return file_stream
    


    def get_all_customers(self):
        '''þetta function opnar file_streamið og texta skjalið sem heitið á functionið er að fókusa á og sendir það upp til LogicMain fyrir processing '''
        file_stream = open('data/data/leigjandi.txt', 'r', encoding='utf-8')
        return file_stream


    def get_all_vehicle(self):
        '''þetta function opnar file_streamið og texta skjalið sem heitið á functionið er að fókusa á og sendir það upp til LogicMain fyrir processing '''
        file_stream = open('data/data/farartaeki.txt', 'r', encoding='utf-8')
        return file_stream



    def get_all_destinations(self):
        '''þetta function opnar file_streamið og texta skjalið sem heitið á functionið er að fókusa á og sendir það upp til LogicMain fyrir processing '''
        file_stream = open('data/data/afangastadir.txt', 'r', encoding='utf-8')
        return file_stream

    def get_all_contracts(self):
        '''þetta function opnar file_streamið og texta skjalið sem heitið á functionið er að fókusa á og sendir það upp til LogicMain fyrir processing '''
        file_stream = open('data/data/leiga.txt', 'r', encoding='utf-8')
        return file_stream
        

    def add_employee(self, new_employee):
        '''þetta function tekur inn lista af nýjum einstaklingi breytir honum í streng, formattaður eins og allt annað í texta skránni og prentar það inn '''
        file_stream = open("data/data/starfsmenn.txt", "a", encoding='utf-8')
        string = ''
        for i in new_employee:
            string += i + ','
        print(string, file=file_stream)
        file_stream.close()
        

    def add_vehicle(self, new_vehicle):
        '''þetta function tekur inn lista af nýjum einstaklingi breytir honum í streng, formattaður eins og allt annað í texta skránni og prentar það inn '''
        file_stream = open("data/data/farartaeki.txt", "a", encoding='utf-8')
        string = ''
        for i in new_vehicle:
            string += i + ','
        print(string, file=file_stream)
        file_stream.close()
    
    def add_destination(self, new_destination):
        '''þetta function tekur inn lista af nýjum einstaklingi breytir honum í streng, formattaður eins og allt annað í texta skránni og prentar það inn '''
        file_stream = open("data/data/afangastadir.txt", "a", encoding='utf-8')
        string = ''
        for i in new_destination:
            string += i + ','
        print(string, file=file_stream)
        file_stream.close()
    
    def add_customer(self, new_customer):
        '''þetta function tekur inn lista af nýjum einstaklingi breytir honum í streng, formattaður eins og allt annað í texta skránni og prentar það inn '''
        file_stream = open("data/data/leigjandi.txt", "a", encoding='utf-8')
        string = ''
        for i in new_customer:
            if type(i) == int:
                i = str(i)
            string += i + ','
        print(string, file=file_stream)
        file_stream.close()
    
    def add_contract(self, new_contract):
        '''þetta function tekur inn lista af nýjum einstaklingi breytir honum í streng, formattaður eins og allt annað í texta skránni og prentar það inn '''
        file_stream = open("data/data/leiga.txt", "a", encoding='utf-8')
        string = ''
        for i in new_contract:
            if type(i) == int:
                i = str(i)
            string += i + ','
        print(string, file=file_stream)
        file_stream.close()
    
    def final_delete(self, ID, new_file_stream, data):
        '''final_delete tekur á móti file stream frá hinum delete functionum til þess að endurskrifa allt nema ID-ið sem var skilgreint '''
        string = ''
        for i in data:
            i = i.split(',')
            i.pop(-1)
            if i[0] == str(ID):
                # hér sjáum við að þegar ID-in matcha þá er það skipað og ekki skrifað inn
                continue
            for b in i:
                string += b + ','
            print(string, file=new_file_stream)
            string = ''
        new_file_stream.close()

    def delete_employee(self, ID):
        '''delete functionin eru kölluð á individually og sækja file streamið áður en við skrifum yfir það svo það hægt að endurskrifa allt '''
        file_stream = open("data/data/starfsmenn.txt", "r", encoding='utf-8')
        data = list(file_stream)
        # fyrst er starfsmenn sóttir og settir í lista
        new_file_stream = open("data/data/starfsmenn.txt", "w", encoding='utf-8')
        # svo eru starfsmenn texta skjalið skrifað yfir og sent í final delete
        self.final_delete(ID, new_file_stream, data)

    def delete_vehicle(self, ID):
        '''delete functionin eru kölluð á individually og sækja file streamið áður en við skrifum yfir það svo það hægt að endurskrifa allt '''
        file_stream = open("data/data/farartaeki.txt", "r", encoding='utf-8')
        data = list(file_stream)
        new_file_stream = open("data/data/farartaeki.txt", "w", encoding='utf-8')
        self.final_delete(ID, new_file_stream, data)

    def delete_customer(self, ID):
        '''delete functionin eru kölluð á individually og sækja file streamið áður en við skrifum yfir það svo það hægt að endurskrifa allt '''
        file_stream = open("data/data/leigjandi.txt", "r", encoding='utf-8')
        data = list(file_stream)
        new_file_stream = open("data/data/leigjandi.txt", "w", encoding='utf-8')
        self.final_delete(ID, new_file_stream, data)
    
    def delete_location(self, ID):
        '''delete functionin eru kölluð á individually og sækja file streamið áður en við skrifum yfir það svo það hægt að endurskrifa allt '''
        file_stream = open("data/data/afangastadir.txt", "r", encoding='utf-8')
        data = list(file_stream)
        new_file_stream = open("data/data/afangastadir.txt", "w", encoding='utf-8')
        self.final_delete(ID, new_file_stream, data)
    
    def delete_contract(self, ID):
        '''delete functionin eru kölluð á individually og sækja file streamið áður en við skrifum yfir það svo það hægt að endurskrifa allt '''
        file_stream = open("data/data/leiga.txt", "r", encoding='utf-8')
        data = list(file_stream)
        new_file_stream = open("data/data/leiga.txt", "w", encoding='utf-8')
        self.final_delete(ID, new_file_stream, data)
    
    def final_change(self, ID, new_file_stream, data, new_Data):
        '''final change functionið skrifar inn í texta skjalið við það sem á við, í staðinn að skrifa sama strengin mun kóðinn stinga inn nýja listann inn í staðinn og breyta hann yfir í streng og gera loka breytinguni'''
        string = ''
        for i in data:
            i = i.split(',')
            i.pop(-1)
            if i[0] == str(ID[0]):
                i = new_Data
            for b in i:
                if type(b)==int:
                    b=str(b)
                string += b + ','
            print(string, file=new_file_stream)
            string = ''
        new_file_stream.close()

    def change_employee(self, ID, changed_employee):
        file_stream = open("data/data/starfsmenn.txt", "r", encoding='utf-8')
        data = list(file_stream)
        new_file_stream = open("data/data/starfsmenn.txt", "w", encoding='utf-8')
        self.final_change(ID, new_file_stream, data, changed_employee)

    def change_customer(self, ID, changed_customer):
        file_stream = open("data/data/leigjandi.txt", "r", encoding='utf-8')
        data = list(file_stream)
        new_file_stream = open("data/data/leigjandi.txt", "w", encoding='utf-8')
        self.final_change(ID, new_file_stream, data, changed_customer)
    
    def change_vehicle(self, ID, changed_vehicle):
        file_stream = open("data/data/farartaeki.txt", "r", encoding='utf-8')
        data = list(file_stream)
        new_file_stream = open("data/data/farartaeki.txt", "w", encoding='utf-8')
        self.final_change(ID, new_file_stream, data, changed_vehicle)

    def change_location(self, ID, changed_location):
        file_stream = open("data/data/afangastadir.txt", "r", encoding='utf-8')
        data = list(file_stream)
        new_file_stream = open("data/data/afangastadir.txt", "w", encoding='utf-8')
        self.final_change(ID, new_file_stream, data, changed_location)

    def change_contract(self, ID, changed_contract):
        file_stream = open("data/data/leiga.txt", "r", encoding='utf-8')
        data = list(file_stream)
        new_file_stream = open("data/data/leiga.txt", "w", encoding='utf-8')
        self.final_change(ID, new_file_stream, data, changed_contract)
        

    