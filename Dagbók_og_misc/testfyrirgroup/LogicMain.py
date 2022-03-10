from DataMain import DataMain

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

    def eyda_element(self, result_dict, id):
        self.result_dict = result_dict
        self.id = id
        result_dict.pop(id)

    def starfsmenn_read_list(self, result_dict):
        self.data.write_starfsmenn_list(result_dict)

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
    
    
    def add_starfsmenn_results(self, result_dict, id, nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning):
        self.result_dict = result_dict
        result_dict[id] = nafn, kennitala, heimilisfang, tolvupostur, simanumer, heimilissimi, stadsetning


#------------------------------------------------------------------------------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------------------------------------------------------------------------------

    def get_farartaeki(self, result_dict, id, area, nafn, numeraplata, fratekid, typa, stadsetning, vidhald, litur, argerd, taxi, km):
            result_list = []
            self.result_dict = result_dict
            self.id = id
            self.area = area
            self.nafn = nafn
            self.numeraplata = numeraplata
            self.fratekid = fratekid
            self.typa = typa
            self.stadsetning = stadsetning
            self.vidhald = vidhald
            self.litur = litur
            self.argerd = argerd
            self.taxi = taxi
            self.km = km
            result_dict[id] = area, nafn, numeraplata, fratekid, typa, stadsetning, vidhald, litur, argerd, taxi, km
            result_list.append(result_dict[id])
    
            return result_list

    def farartaeki_read_list(self, result_dict):
        self.data.write_farartaeki_list(result_dict)

    def get_farartaeki_file(self, result_dict):
        self.result_dict = result_dict
        resultList = []
        file_stream = self.data.open_farartaeki_file()
        for i in file_stream:
            i = i.split(",")
            id = int(i[0])
            area = int(i[1])
            nafn = i[2]
            numeraplata = i[3]
            fratekid = i[4] 
            typa = i[5] 
            stadsetning = i[6]
            vidhald = i[7]
            litur = i[8]
            argerd = i[9]
            taxi = int(i[10])
            km = int(i[11])
            result_dict[id] = area, nafn, numeraplata, fratekid, typa, stadsetning, vidhald, litur, argerd, taxi, km
        for id in result_dict:
            resultList.append(result_dict[id])
        return resultList
    
    
    def add_farartaeki_results(self, result_dict, id, area, nafn, numeraplata, fratekid, typa, stadsetning, vidhald, litur, argerd, taxi, km):
        self.result_dict = result_dict
        result_dict[id] = area, nafn, numeraplata, fratekid, typa, stadsetning, vidhald, litur, argerd, taxi, km

#------------------------------------------------------------------------------------------------------------------------------------------------------

    def get_leiga(self, result_dict, id, id_leigjandi, id_starfsmadur, kostnadur, id_farartaeki, id_afangastadir, samningur_stofnadur, byrjun_samningur, endir_samningur, pickup_timi, rukkadur, motaka):
            result_list = []
            self.result_dict = result_dict
            self.id = id
            self.id_leigjandi = id_leigjandi
            self.id_starfsmadur = id_starfsmadur
            self.kostnadur = kostnadur
            self.id_farartaeki = id_farartaeki
            self.id_afangastadir = id_afangastadir
            self.samningur_stofnadur = samningur_stofnadur
            self.byrjun_samningur = byrjun_samningur
            self.endir_samningur = endir_samningur
            self.pickup_timi = pickup_timi
            self.rukkadur = rukkadur
            self.motaka = motaka
            result_dict[id] = id_leigjandi, id_starfsmadur, kostnadur, id_farartaeki, id_afangastadir, samningur_stofnadur, byrjun_samningur, endir_samningur, pickup_timi, rukkadur, motaka
            result_list.append(result_dict[id])
    
            return result_list

    def leiga_read_list(self, result_dict):
        self.data.write_leiga_list(result_dict)

    def get_leiga_file(self, result_dict):
        self.result_dict = result_dict
        resultList = []
        file_stream = self.data.open_leiga_file()
        for i in file_stream:
            i = i.split(",")
            id = int(i[0])
            id_leigjandi = int(i[1])
            id_starfsmadur = int(i[2])
            kostnadur = int(i[3])
            id_farartaeki = int(i[4])
            id_afangastadir = int(i[5])
            samningur_stofnadur = i[6]
            byrjun_samningur = i[7] 
            endir_samningur = i[8] 
            pickup_timi = i[9]
            rukkadur = i[10]
            motaka = i[11]
            result_dict[id] = id_leigjandi, id_starfsmadur, kostnadur, id_farartaeki, id_afangastadir, samningur_stofnadur, byrjun_samningur, endir_samningur, pickup_timi, rukkadur, motaka
        for id in result_dict:
            resultList.append(result_dict[id])
        return resultList
    
    
    def add_leiga_results(self, result_dict, id, id_leigjandi, id_starfsmadur, kostnadur, id_farartaeki, id_afangastadir, samningur_stofnadur, byrjun_samningur, endir_samningur, pickup_timi, rukkadur, motaka):
        self.result_dict = result_dict
        result_dict[id] = id_leigjandi, id_starfsmadur, kostnadur, id_farartaeki, id_afangastadir, samningur_stofnadur, byrjun_samningur, endir_samningur, pickup_timi, rukkadur, motaka

#------------------------------------------------------------------------------------------------------------------------------------------------------

    def get_leigjandi(self, result_dict, id, nafn, kennitala, simanumer, heimilisfang, tolvupostur, typa):
            result_list = []
            self.result_dict = result_dict
            self.id = id
            self.nafn = nafn
            self.kennitala = kennitala
            self.simanumer = simanumer
            self.heimilisfang = heimilisfang
            self.tolvupostur = tolvupostur
            self.typa = typa
            result_dict[id] = nafn, kennitala, simanumer, heimilisfang, tolvupostur, typa
            result_list.append(result_dict[id])
    
            return result_list

    def leigjandi_read_list(self, result_dict):
        self.data.write_leigjandi_list(result_dict)

    def get_leigjandi_file(self, result_dict):
        self.result_dict = result_dict
        resultList = []
        file_stream = self.data.open_leigjandi_file()
        for i in file_stream:
            i = i.split(",")
            id = int(i[0])
            nafn = i[1]
            kennitala = i[2]
            simanumer = i[3]
            heimilisfang = i[4] 
            tolvupostur = i[5] 
            typa = i[6]
            result_dict[id] = nafn, kennitala, simanumer, heimilisfang, tolvupostur, typa
        for id in result_dict:
            resultList.append(result_dict[id])
        return resultList
    
    
    def add_leigjandi_results(self, result_dict, id, nafn, kennitala, simanumer, heimilisfang, tolvupostur, typa):
        self.result_dict = result_dict
        result_dict[id] = nafn, kennitala, simanumer, heimilisfang, tolvupostur, typa