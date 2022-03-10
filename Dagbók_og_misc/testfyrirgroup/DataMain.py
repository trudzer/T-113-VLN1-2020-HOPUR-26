class DataMain:

    def open_starfsmenn_file(self):
        try:
            file_object = open("./files/starfsmenn.txt", 'r', encoding='utf8')
            return file_object
        except FileNotFoundError:
            return None

    def write_starfsmenn_list(self, result_dict):
        self.result_dict = result_dict
        resultList = []
        try:
            file_object = open("./files/starfsmenn.txt", 'w', encoding='utf8')
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

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def open_farartaeki_file(self):
        try:
            file_object = open("./files/farartaeki.txt", 'r', encoding='utf8')
            return file_object
        except FileNotFoundError:
            return None

    def write_farartaeki_list(self, result_dict):
        self.result_dict = result_dict
        resultList = []
        try:
            file_object = open("./files/farartaeki.txt", 'w', encoding='utf8')
            for id in result_dict:
                area = result_dict[id][0]
                nafn = result_dict[id][1]
                numeraplata = result_dict[id][2]
                fratekid = result_dict[id][3]
                typa = result_dict[id][4]
                stadsetning = result_dict[id][5]
                vidhald = result_dict[id][6]
                litur = result_dict[id][7]
                argerd = result_dict[id][8]
                taxi = result_dict[id][9]
                km = result_dict[id][10]
                if len(result_dict) > 1:
                    file_object.writelines(str("{},{},{},{},{},{},{},{},{},{},{},{},\n".format(id,area,nafn,numeraplata,fratekid,typa,stadsetning,vidhald,litur,argerd,taxi,km)))
            file_object.close()
        except FileNotFoundError:
            return None

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def open_leiga_file(self):
        try:
            file_object = open("./files/leiga.txt", 'r', encoding='utf8')
            return file_object
        except FileNotFoundError:
            return None

    def write_leiga_list(self, result_dict):
        self.result_dict = result_dict
        resultList = []
        try:
            file_object = open("./files/leiga.txt", 'w', encoding='utf8')
            for id in result_dict:
                id_leigjandi = result_dict[id][0]
                id_starfsmadur = result_dict[id][1]
                kostnadur = result_dict[id][2]
                id_farartaeki = result_dict[id][3]
                id_afangastadir = result_dict[id][4]
                samningur_stofnadur = result_dict[id][5]
                byrjun_samningur = result_dict[id][6]
                endir_samningur = result_dict[id][7]
                pickup_timi = result_dict[id][8]
                rukkadur = result_dict[id][9]
                motaka = result_dict[id][10]
                if len(result_dict) > 1:
                    file_object.writelines(str("{},{},{},{},{},{},{},{},{},{},{},{},\n".format(id,id_leigjandi, id_starfsmadur, kostnadur,id_farartaeki, id_afangastadir,samningur_stofnadur,byrjun_samningur,endir_samningur,pickup_timi,rukkadur,motaka)))
            file_object.close()
        except FileNotFoundError:
            return None

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def open_leigjandi_file(self):
        try:
            file_object = open("./files/leigjandi.txt", 'r', encoding='utf8')
            return file_object
        except FileNotFoundError:
            return None

    def write_leigjandi_list(self, result_dict):
        self.result_dict = result_dict
        resultList = []
        try:
            file_object = open("./files/leigjandi.txt", 'w', encoding='utf8')
            for id in result_dict:
                nafn = result_dict[id][0]
                kennitala = result_dict[id][1]
                simanumer = result_dict[id][2]
                heimilisfang = result_dict[id][3]
                tolvupostur = result_dict[id][4]
                typa = result_dict[id][5]
                if len(result_dict) > 1:
                    file_object.writelines(str("{},{},{},{},{},{},{},\n".format(id,nafn,kennitala,simanumer,heimilisfang,tolvupostur,typa)))
            file_object.close()
        except FileNotFoundError:
            return None

