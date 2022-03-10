from logic.LogicMain import LogicMain
lm = LogicMain()
infolist=["Daniel Makarena","200287-2219","Hilmarveig 5","danmakarena@nan.is","+47-79-69-69-69","+47-79-56-23-45","Longyearbyen"]
print(lm.change_select_vehicles("type","Fólksbíll",[None,None,None,None,None,None,None,None,None,"12",None,None]))
#["Bíll",False,"blár",2018,"bíll","IDK","Ford",0.20,"good"]
