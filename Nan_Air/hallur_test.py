from logic.LogicMain import LogicMain
from data.DataMain import DataMain
from logic.annad import *
import os
lm = LogicMain()
buno = lm.change_contract(['1','1','17','25200','2','2','30-11-20','02-12-20','10-12-20','13:00','Órukkaður','Já',])
print(buno)

# print (os.getcwd())
# data = open('hallurtest.txt','r', encoding='utf-8')
# data = list(data)
# for i in data:
#     i = i.split(',''\n')
#     print(i)